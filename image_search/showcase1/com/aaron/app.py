from sentence_transformers import SentenceTransformer, util
from PIL import Image, ImageFile
from transformers import CLIPModel, CLIPTokenizer
import requests
import torch
from transformers import AutoConfig
from transformers import AutoModel
from  pprint import pprint



# Now we load and encode the images
def load_image(url_or_path):
    if url_or_path.startswith("http://") or url_or_path.startswith("https://"):
        return Image.open(requests.get(url_or_path, stream=True).raw)
    else:
        return Image.open(url_or_path)


if __name__ == "__main__":
    # We use the original clip-ViT-B-32 for encoding images
    # img_model = SentenceTransformer('clip-ViT-B-32')
    # img_model = SentenceTransformer('C:/Users/Administrator/Downloads/clip-ViT-B-32')
    img_model = AutoModel.from_pretrained("C:/Users/Administrator/Downloads/clip-ViT-B-32", trust_remote_code=True)

    # config = AutoConfig.from_pretrained('C:/Users/Administrator/Downloads/clip-ViT-B-32')
    # img_model = AutoModel.from_config(config)

    # Our text embedding model is aligned to the img_model and maps 50+
    # languages to the same vector space
    # text_model = SentenceTransformer('sentence-transformers/clip-ViT-B-32-multilingual-v1')
    # text_model = SentenceTransformer('C:\\Users\\Administrator\\Downloads\\clip-ViT-B-32-multilingual-v1')
    # config = AutoConfig.from_pretrained('C:/Users/Administrator/Downloads/clip-ViT-B-32-multilingual-v1')
    # text_model = AutoModel.from_config(config)

    # We load 3 images. You can either pass URLs or
    # a path on your disc
    img_paths = [
        # Dog image
        "https://unsplash.com/photos/QtxgNsmJQSs/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjM1ODQ0MjY3&w=640",

        # Cat image
        "https://unsplash.com/photos/9UUoGaaHtNE/download?ixid=MnwxMjA3fDB8MXxzZWFyY2h8Mnx8Y2F0fHwwfHx8fDE2MzU4NDI1ODQ&w=640",

        # Beach image
        "https://unsplash.com/photos/Siuwr3uCir0/download?ixid=MnwxMjA3fDB8MXxzZWFyY2h8NHx8YmVhY2h8fDB8fHx8MTYzNTg0MjYzMg&w=640"
    ]

    images = [load_image(img) for img in img_paths]
    print(images)

    # Map images to the vector space
    img_embeddings = img_model.encode(images)

    # Now we encode our text:
    texts = [
        "A dog in the snow",
        "Eine Katze",  # German: A cat
        "Una playa con palmeras."  # Spanish: a beach with palm trees
    ]

    # text_embeddings = text_model.encode(texts)

    # Compute cosine similarities:
    # cos_sim = util.cos_sim(text_embeddings, img_embeddings)

    # for text, scores in zip(texts, cos_sim):
    #     max_img_idx = torch.argmax(scores)
    #     print("Text:", text)
    #     print("Score:", scores[max_img_idx])
    #     print("Path:", img_paths[max_img_idx], "\n")
