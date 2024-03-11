import cv2
import os

display_output_folder = "H:/workspace/Nabeel/SAM-Med2D/displayed_F4-images/"
output_folder = "H:/workspace/Nabeel/SAM-Med2D/displayed_F-images/"

output_files = os.listdir(output_folder)[:4]  # Get the first four files from the output folder

images = []
for img_file in output_files:
    output_img_path = os.path.join(output_folder, img_file)
    img = cv2.imread(output_img_path)
    images.append(img)

# Concatenate the four images horizontally
top_row = cv2.hconcat([images[0], images[1]])
bottom_row = cv2.hconcat([images[2], images[3]])

# Concatenate the top and bottom rows vertically
display_image = cv2.vconcat([top_row, bottom_row])

# Display the concatenated image
cv2.imshow("Four Images", display_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
