import os
import json

# Directory paths for images and masks
image_dir = 'H:/workspace/Nabeel/SAM-Med2D/data-demo/data-demo/Original_Images'
mask_dir = 'H:/workspace/Nabeel/SAM-Med2D/data-demo/data-demo/Microaneurysms_Masks'

# Dictionary to store image-to-mask mappings
image_mask_mapping = {}

# Traverse the image directory
for image_name in os.listdir(image_dir):
    if image_name.endswith('.jpg') or image_name.endswith('.png'):
        # Create the full image path
        image_path = os.path.join(image_dir, image_name)

        # Find all masks related to the image (modify this according to your mask naming convention)
        related_masks = []
        for mask_name in os.listdir(mask_dir):
            if mask_name.startswith(image_name.replace('.jpg', '')):
                mask_path = os.path.join(mask_dir, mask_name)
                related_masks.append(mask_path)

        if related_masks:
            image_mask_mapping[image_path] = related_masks

# Save the image-to-mask mapping as a JSON file
with open('H:/workspace/Nabeel/SAM-Med2D/data-demo/data-demo/image2label_train7.json', 'w') as json_file:
    json.dump(image_mask_mapping, json_file, indent=4)

print("JSON file created with image-to-mask mappings.")
