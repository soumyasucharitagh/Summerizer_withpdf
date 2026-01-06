import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)
model.eval()

def generate_caption(image):
    inputs = processor(image, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption
