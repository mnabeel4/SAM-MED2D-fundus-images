
import cv2
import os

input_folder = "H:/workspace/Nabeel/SAM-Med2D/data-demo/data-demo/trained-images"
output_folder = "H:/workspace/Nabeel/SAM-Med2D/displayed_images"
display_output_folder = "H:/workspace/Nabeel/SAM-Med2D/displayed_F-images/"

if not os.path.exists(display_output_folder):
    os.makedirs(display_output_folder)

image_files = os.listdir(input_folder)
for img_file in image_files:
    img_name = img_file.split('.')[0]
    input_img_path = os.path.join(input_folder, img_file)
    output_img_path = os.path.join(output_folder, f"{img_name}.png")

    input_img = cv2.imread(input_img_path)
    output_img = cv2.imread(output_img_path)

    # Concatenate images horizontally (side by side)
    concatenated_img = cv2.hconcat([input_img, output_img])

    # Save the displayed image
    display_output_path = os.path.join(display_output_folder, f"{img_name}.png")
    cv2.imwrite(display_output_path, concatenated_img)

print("All display images saved successfully!")
