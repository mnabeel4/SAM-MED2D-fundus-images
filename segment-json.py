import os
import cv2
import json

# Function to convert BMP masks with polygons to JSON annotations
def bmp_polygons_to_json(mask_directory, output_file):
    annotations = []

    mask_files = os.listdir(mask_directory)
    mask_files.sort()

    for mask_file in mask_files:
        mask_path = os.path.join(mask_directory, mask_file)

        # Read the mask
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

        # Find contours representing polygons
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Extract polygon vertices
        for contour in contours:
            contour_points = contour.squeeze().tolist()
            annotation = {"filename": mask_file, "regions": [{"shape_attributes": {"all_points_x": [], "all_points_y": []}}]}

            for point in contour_points:
                x, y = point
                annotation["regions"][0]["shape_attributes"]["all_points_x"].append(x)
                annotation["regions"][0]["shape_attributes"]["all_points_y"].append(y)

            annotations.append(annotation)

    # Save annotations to JSON file
    with open(output_file, 'w') as json_file:
        json.dump(annotations, json_file, indent=4)

# Example usage:
mask_dir = 'H:/workspace/Nabeel/SAM-Med2D/data_demo/json'
output_json = 'H:/workspace/Nabeel/SAM-Med2D/data_demo/json.json'
bmp_polygons_to_json(mask_dir, output_json)
