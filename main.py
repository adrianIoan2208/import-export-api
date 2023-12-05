from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET
import pandas as pd
from io import StringIO

app = Flask(__name__)

# Endpoint for uploading XML files
@app.route('/upload-xml', methods=['POST'])
def upload_xml():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    xml_file = request.files['file']
    if xml_file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Validate file extension or MIME type for XML
    if not xml_file.filename.endswith('.xml') or xml_file.mimetype != 'text/xml':
        return jsonify({'error': 'Invalid file type. Please upload an XML file'})

    # Process XML file and transform data into your custom format
    transformed_data = process_xml(xml_file)

    # Example response
    return jsonify({'result': transformed_data})

# Endpoint for uploading CSV files
@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    # if 'username.csv' not in request.files:
    #     return jsonify({'error': 'No file part'})

    csv_file = request.files['username.csv']
    if csv_file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Validate file extension or MIME type for CSV
    if not csv_file.filename.endswith('.csv') or csv_file.mimetype != 'text/csv':
        return jsonify({'error': 'Invalid file type. Please upload a CSV file'})

    # Process CSV file and transform data into your custom format
    transformed_data = process_csv(csv_file)

    # Example response
    return jsonify({'result': transformed_data})

# Sample function to process XML data
def process_xml(xml_file):
    # Process XML file and transform data into your custom format
    # Example: Using ElementTree for parsing XML
    root = ET.parse(xml_file).getroot()
    data = []
    for child in root:
        # Process XML data as needed
        # Example: Extracting specific elements
        item = {
            'name': child.find('name').text,
            'value': child.find('value').text
            # Add more fields as required
        }
        data.append(item)

    return {'formatted_data': data}

# Sample function to process CSV data
def process_csv(csv_file):
    # Process CSV file and transform data into your custom format
    # Example: Using pandas for parsing CSV
    csv_text = csv_file.stream.read().decode('utf-8-sig')
    df = pd.read_csv(StringIO(csv_text))
    data = df.to_dict('records')

    return {'formatted_data': data}

if __name__ == '__main__':
    app.run(debug=True)
