from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModel
from transformers import T5Model
from transformers import AutoProcessor


from transformers import AutoConfig
config = AutoConfig.from_pretrained('C:/Users/Administrator/Downloads/clip-ViT-B-32')
model = AutoModel.from_config(config)



# tokenizer = AutoTokenizer.from_pretrained("C:/Users/Administrator/Downloads/clip-ViT-B-32")
# model = AutoModelForSeq2SeqLM.from_pretrained("C:/Users/Administrator/Downloads/clip-ViT-B-32")

# tokenizer = AutoTokenizer.from_pretrained("C:/Users/Administrator/Downloads/clip-ViT-B-32")
# model = AutoProcessor.from_pretrained("C:/Users/Administrator/Downloads/clip-ViT-B-32")

# tokenizer.save_pretrained("C:/Users/Administrator/Downloads/model")
# model.save_pretrained("C:/Users/Administrator/Downloads/model")

# tokenizer = AutoTokenizer.from_pretrained("C:/Users/Administrator/Downloads/model")
# model = AutoModel.from_pretrained("C:/Users/Administrator/Downloads/model")
print(model)