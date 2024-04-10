from sentence_transformers import SentenceTransformer, util
from PIL import Image
import glob
import torch
import pickle
import zipfile
from IPython.display import display
from IPython.display import Image as IPImage
import os
from tqdm.autonotebook import tqdm

"""
https://github.com/UKPLab/sentence-transformers/blob/master/examples/applications/image-search/README.md
https://unsplash.com/data

"""

if __name__ == "__main__":
    # Load CLIP model
    model = SentenceTransformer("clip-ViT-B-32")

    # Encode an image:
    img_emb = model.encode(Image.open("two_dogs_in_snow.jpg"))

    # Encode text descriptions
    text_emb = model.encode(
        ["Two dogs in the snow", "A cat on a table", "A picture of London at night"]
    )

    # Compute cosine similarities
    cos_scores = util.cos_sim(img_emb, text_emb)
    print(cos_scores)