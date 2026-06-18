import fitz
import os

def pdf_to_jpeg(pdf_path, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    pdf = fitz.open(pdf_path)

    for page_number in range(len(pdf)):

        page = pdf.load_page(page_number)

        pix = page.get_pixmap(matrix=fitz.Matrix(3,3))

        image_path = os.path.join(
            output_folder,
            f"page_{page_number + 1}.jpg"
        )

        pix.save(image_path)

    pdf.close()

    return output_folder