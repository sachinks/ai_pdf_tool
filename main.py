import sys
import os

from utils.pdf_utils import extract_text
from utils.chunk_utils import chunk_text
from utils.llm_utils import generate_response


OUTPUT_DIR = "output"
OUTPUT_FILE = "final_summary.txt"


def summarize_chunks(chunks, mode="summary"):

    summaries = []

    print(f"\nTotal chunks: {len(chunks)}")

    for index, chunk in enumerate(chunks, start=1):

        print(f"\nProcessing chunk {index}/{len(chunks)}")

        if mode == "bullets":

            prompt = f"""
            Summarize the following text strictly as bullet points.

            TEXT:
            {chunk}
            """

        else:

            prompt = f"""
            Summarize the following text concisely.

            TEXT:
            {chunk}
            """

        summary = generate_response(prompt)

        summaries.append(summary)

    return "\n".join(summaries)


def generate_final_summary(chunk_summaries):

    prompt = f"""
    Combine and refine the following summaries
    into one clean final summary.

    SUMMARIES:
    {chunk_summaries}
    """

    return generate_response(prompt)


def save_summary(summary):

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    output_path = os.path.join(
        OUTPUT_DIR,
        OUTPUT_FILE
    )

    with open(output_path,
              "w",
              encoding="utf-8") as file:

        file.write(summary)

    print(f"\nSummary saved to: {output_path}")


def main():

    if len(sys.argv) < 2:

        print("Usage:")
        print("python main.py <pdf_path> [summary|bullets]")

        sys.exit(1)

    pdf_path = sys.argv[1]

    mode = sys.argv[2] if len(sys.argv) > 2 else "summary"

    print("\n========== PDF SUMMARIZER ==========")

    print("\nExtracting text from PDF...")

    text = extract_text(pdf_path)

    if not text.strip():

        print("No text extracted from PDF.")
        sys.exit(1)

    print(f"\nExtracted text length: {len(text)}")

    print("\nCreating intelligent chunks...")

    chunks = chunk_text(text)

    print("\nGenerating chunk summaries...")

    chunk_summaries = summarize_chunks(chunks, mode)

    print("\nGenerating final summary...")

    final_summary = generate_final_summary(
        chunk_summaries
    )

    print("\n========== FINAL SUMMARY ==========\n")

    print(final_summary)

    save_summary(final_summary)


if __name__ == "__main__":
    main()