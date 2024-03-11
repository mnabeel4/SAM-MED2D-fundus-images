import os
import shutil

def organize_images_by_class(input_folder, output_folder):
    # List all files in the input folder
    image_files = os.listdir(input_folder)

    # Create class-specific folders and move images
    for image_file in image_files:
        if os.path.isfile(os.path.join(input_folder, image_file)):
            class_name = image_file.split('_')[-1].split('.')[0]  # Extract class name from filename

            # Create class-specific folder if it doesn't exist
            class_folder = os.path.join(output_folder, class_name)
            os.makedirs(class_folder, exist_ok=True)

            # Move image to the respective class folder
            shutil.move(os.path.join(input_folder, image_file), os.path.join(class_folder, image_file))

# Usage
input_images_folder = 'H:/workspace/Nabeel/SAM-Med2D/data-demo/data-demo/Lesions-dataset/original-labels'  # Update with the path to your input images folder
output_images_folder = 'H:/workspace/Nabeel/SAM-Med2D/data-demo/data-demo/separate-label-classes'  # Update with the path to your output images folder

organize_images_by_class(input_images_folder, output_images_folder)
