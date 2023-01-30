#import CLIP transformers
from sentence_transformers import SentenceTransformer, util

from core.config import CROPPED_PILL_PATH, MODEL_PATH
import glob
from PIL import Image
import os
import pickle
from loguru import logger
import torch


def load_sentence_model():
    # # Load the OpenAI CLIP Model
    if os.path.exists(MODEL_PATH):
        model = pickle.load(open(MODEL_PATH, 'rb'))
    else:
        message = "No model exists! Downloading..."
        logger.error(message)
        model = SentenceTransformer('clip-ViT-B-32')
        pickle.dump(model, open(MODEL_PATH, 'wb'))

    return model

# Next we encode each image
def encode_images(model):
    '''encodes the stored images'''

    image_names = glob.glob(f'{CROPPED_PILL_PATH}*.png')
    encoded_images = model.encode([Image.open(filepath) for filepath in image_names],
                                    batch_size=128, convert_to_tensor=True)
    return (encoded_images, image_names)

def run_clustering_model(encoded_images):
    
    processed_images = util.paraphrase_mining_embeddings(encoded_images)
    
    return processed_images

def find_closest_pills(model, uploaded_image_path):
    
    #add new image to existing encoded images
    encoded_images, image_names = encode_images(model)
    encoded_uploaded_image = model.encode(Image.open(uploaded_image_path), batch_size=128, convert_to_tensor=True)
    encoded_images = torch.vstack((encoded_images, encoded_uploaded_image))
    uploaded_idx = len(encoded_images) - 1
    image_names.append(uploaded_image_path)

    #run clustering model on all images including new
    processed_images = run_clustering_model(encoded_images)

    similar_images = []
    for score, image_id1, image_id2 in processed_images:
        if (image_id1 == uploaded_idx) or (image_id2 == uploaded_idx):
            print("\nScore: {:.3f}%".format(score))
            print(image_names[uploaded_idx])
            image_match = [image_names[image_id2 if image_id1 == uploaded_idx else image_id1], score]
            similar_images.append(image_match)
    
    return similar_images