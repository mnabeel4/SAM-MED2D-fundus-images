import json
import os

# Directory paths for masks and images
masks_directory = 'H:/workspace/Nabeel/SAM-Med2D/data-demo/data-demo/trained-masks/'
images_directory = 'H:/workspace/Nabeel/SAM-Med2D/data-demo/data-demo/trained-images'

# Fetching all files in the masks directory
mask_files = os.listdir(masks_directory)

# Creating a dictionary with masks as keys and corresponding images as values
data = {os.path.join(masks_directory, mask_file): os.path.join(images_directory, mask_file) for mask_file in mask_files}

# Define the output JSON file path
output_json_path = 'H:/workspace/Nabeel/SAM-Med2D/data-demo/data-demo/masks_to_images.json'

# Write the data dictionary to a JSON file
with open(output_json_path, 'w') as json_file:
    json.dump(data, json_file)

print(f"Data written to {output_json_path}")
