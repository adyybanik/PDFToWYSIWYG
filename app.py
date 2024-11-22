import fitz  # PyMuPDF for PDF parsing
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/convert', methods=['POST'])
def convert_pdf():
    pdf_file = request.files['pdf']
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    html_content = ""

    for page in doc:
        html_content += f"<div>{page.get_text('html')}</div>"

    doc.close()
    return render_template('editor.html', content=html_content)

if __name__ == "__main__":
    app.run(debug=True)
