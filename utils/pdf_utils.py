import pdfplumber


def extract_text(pdf_path):
    """
    Extract text from all pages in PDF.
    """

    full_text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:

            total_pages = len(pdf.pages)

            print(f"Total pages found: {total_pages}")

            for page_number, page in enumerate(pdf.pages, start=1):

                text = page.extract_text()

                if text:
                    full_text += text + "\n"

                print(f"Extracted page {page_number}")

    except Exception as e:
        raise Exception(f"PDF extraction failed: {e}")

    return full_text