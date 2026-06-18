from flask import Flask, render_template, request, redirect, url_for

from converter import pdf_to_jpeg
import zipfile
import os
# from flask import redirect, url_for

from flask import after_this_request
from flask import send_file

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        status=None,
        filename=None,
        uploaded_file=None
    )

@app.route("/upload", methods=["POST"])

def upload():
    try:


        pdf = request.files.get("pdf_file")

        if pdf is None:
            return render_template(
                "index.html",
                status="No file received."
            )

    

        if pdf.filename == "":
            return render_template(
                "index.html",
                status="Please select a file."
            )

        if not pdf.filename.lower().endswith(".pdf"):
            return render_template(
                "index.html",
                status="Please upload a PDF file only."
            )

        pdf_path = "uploads/" + pdf.filename

        pdf.save(pdf_path)

        for file in os.listdir("outputs"):
            os.remove(os.path.join("outputs", file))

        pdf_to_jpeg(pdf_path, "outputs")

        zip_path = "converted_images.zip"

        with zipfile.ZipFile(zip_path, "w") as zipf:

            for file in os.listdir("outputs"):

                file_path = os.path.join("outputs", file)

                zipf.write(
                    file_path,
                    arcname=file
                )
    
    
        
        return redirect(url_for("success"))
    
    except Exception as e:

        return render_template(
            "index.html",
            status=f"Error: {str(e)}"
        )

@app.route("/success")
def success():

    return render_template(
        "index.html",
        status="PDF Converted Successfully!",
        filename="converted_images.zip",
        uploaded_file="Ready for Download"
    )

@app.route("/download")
def download():

    @after_this_request
    def cleanup(response):

        for file in os.listdir("uploads"):
            os.remove(os.path.join("uploads", file))

        for file in os.listdir("outputs"):
            os.remove(os.path.join("outputs", file))

        return response

    return send_file(
        "converted_images.zip",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)