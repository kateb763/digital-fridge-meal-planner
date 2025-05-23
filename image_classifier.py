from transformers import AutoImageProcessor, ResNetForImageClassification
from PIL import Image
import torch

class ImageClassifier:
    def __init__(self, image=None):
        self.image = image

    def recognize_food_item(self): 
        processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
        model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")
        inputs = processor(self.image, return_tensors="pt")

        with torch.no_grad():
            logits = model(**inputs).logits

        predicted_label = logits.argmax(-1).item()
        food_name = model.config.id2label[predicted_label]
        return food_name