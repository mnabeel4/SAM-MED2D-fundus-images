import xmltodict
import json

def xml_to_json(xml_file):
    with open(xml_file, 'r') as file:
        # Parse XML to OrderedDict
        xml_data = xmltodict.parse(file.read())

        # Convert OrderedDict to JSON
        json_data = json.dumps(xml_data, indent=4)

        # Save JSON data to a file
        output_file = xml_file.replace('.xml', '.json')
        with open(output_file, 'w') as output:
            output.write(json_data)

# Example usage:
xml_file = 'H:/workspace/Nabeel/SAM-Med2D/data_demo/voc_xml/optic-disc.xml'
xml_to_json(xml_file)
