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
https://github.com/UKPLab/sentence-transformers/blob/master/examples/applications/image-search/Image_Duplicates.ipynb
https://unsplash.com/data

"""

if __name__ == "__main__":
    # First, we load the respective CLIP model
    model = SentenceTransformer('clip-ViT-B-32')

    # Next, we get about 25k images from Unsplash
    img_folder = 'photos/'
    if not os.path.exists(img_folder) or len(os.listdir(img_folder)) == 0:
        os.makedirs(img_folder, exist_ok=True)

        photo_filename = 'unsplash-25k-photos.zip'
        if not os.path.exists(photo_filename):  # Download dataset if does not exist
            util.http_get('http://sbert.net/datasets/' + photo_filename, photo_filename)

        # Extract all images
        with zipfile.ZipFile(photo_filename, 'r') as zf:
            for member in tqdm(zf.infolist(), desc='Extracting'):
                zf.extract(member, img_folder)

    # Now, we need to compute the embeddings
    # To speed things up, we destribute pre-computed embeddings
    # Otherwise you can also encode the images yourself.
    # To encode an image, you can use the following code:
    # from PIL import Image
    # img_emb = model.encode(Image.open(filepath))

    use_precomputed_embeddings = True

    if use_precomputed_embeddings:
        emb_filename = 'unsplash-25k-photos-embeddings.pkl'
        if not os.path.exists(emb_filename):  # Download dataset if does not exist
            util.http_get('http://sbert.net/datasets/' + emb_filename, emb_filename)

        with open(emb_filename, 'rb') as fIn:
            img_names, img_emb = pickle.load(fIn)
        print("Images:", len(img_names))
    else:
        img_names = list(glob.glob('photos/*.jpg'))
        print("Images:", len(img_names))
        img_emb = model.encode([Image.open(filepath) for filepath in img_names], batch_size=128, convert_to_tensor=True,
                               show_progress_bar=True)

    # Now we run the clustering algorithm
    # With the threshold parameter, we define at which threshold we identify
    # two images as similar. Set the threshold lower, and you will get larger clusters which have
    # less similar images in it (e.g. black cat images vs. cat images vs. animal images).
    # With min_community_size, we define that we only want to have clusters of a certain minimal size

    duplicates = util.paraphrase_mining_embeddings(img_emb)

    # duplicates contains a list with triplets (score, image_id1, image_id2) and is scorted in decreasing order

    for score, idx1, idx2 in duplicates[0:10]:
        print("\nScore: {:.3f}".format(score))
        print(img_names[idx1])
        display(IPImage(os.path.join(img_folder, img_names[idx1]), width=200))
        print(img_names[idx2])
        display(IPImage(os.path.join(img_folder, img_names[idx2]), width=200))