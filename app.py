from flask import Flask, request, send_file
from io import BytesIO
import docx

app = Flask(__name__)

@app.route('/generate-word-file', methods=['POST'])
def generate_word_file():
    data = request.get_json()
    filename = data.get('filename', 'output.docx')
    content = data.get('content', '')

    # Create a Word file in memory
    buffer = BytesIO()
    doc = docx.Document()
    doc.add_paragraph(content)
    doc.save(buffer)
    buffer.seek(0)

    # Return the file as a response
    return send_file(
        buffer,
        as_attachment=True,
        download_name=filename,
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )

if __name__ == '__main__':
    app.run(debug=True)