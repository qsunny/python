import torch
import clip
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)
# 1. 返回可以用的模型
clip.available_models()
['RN50', 'RN101', 'RN50x4', 'RN50x16', 'RN50x64', 'ViT-B/32', 'ViT-B/16', 'ViT-L/14', 'ViT-L/14@336px']

# 2. 返回对应的模型和图像转换器
model, preprocess = clip.load("ViT-B/32")

# 3. preprocess将Image转换成tensor[3, 224, 224]，然后unsqueeze(0)转成[batch_size, 3, 3, 224]后才能输入模型
image = preprocess(Image.open("ddd.png")).unsqueeze(0)

# 4. 将多个句子[batch_size]的每个句子转换成向量[batch_size, context_length]
# 	每个句子开头加一个BOS(49406) EOS(49407)，然后填充到长度context_length（默认值为77）
# 	（若长度大于context_length-2，需设置参数truncate=True，然后返回值为BOS 内容 EOS，即EOS没有被切割掉）
text = clip.tokenize(["a diagram", "a dog", "a cat"]).to(device)  # [3, 77]

# 5. 获取多个图片的特征
image_features = model.encode_image(image)

# 6. 获取多个文本的特征
text_features = model.encode_text(text)

# 7. 获取 多个图片和多个文本 之间余弦相似度（0~1）
logits_per_image, logits_per_text = model(image, text)
