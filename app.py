from flask import Flask, request, send_file
from docx import Document
import os

app = Flask(__name__)

@app.route('/generate-word-file', methods=['POST'])
def generate_word_file():
    data = request.json
    filename = data.get('filename', 'document.docx')
    content = data.get('content', '')

    # Create a Word document
    doc = Document()
    doc.add_heading('Generated Document', level=1)
    doc.add_paragraph(content)

    # Save the document
    filepath = os.path.join('files', filename)
    os.makedirs('files', exist_ok=True)
    doc.save(filepath)

    # Return the file
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)