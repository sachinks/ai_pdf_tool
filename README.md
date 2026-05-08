# AI PDF Tool

A command-line tool that summarizes PDF documents using a local LLM via [Ollama](https://ollama.com). It extracts text from a PDF, splits it into overlapping chunks, summarizes each chunk, then combines them into a single final summary.

## How It Works

1. **Extract** — `pdfplumber` reads all pages from the PDF
2. **Chunk** — text is split into 4000-character overlapping chunks (500-char overlap), respecting paragraph and sentence boundaries
3. **Summarize** — each chunk is sent to the local Ollama model (default: `mistral`)
4. **Combine** — chunk summaries are merged into one final summary
5. **Save** — the result is written to `output/final_summary.txt`

## Requirements

- Python 3.12+
- [Ollama](https://ollama.com) installed and running locally
- Mistral model pulled: `ollama pull mistral`

## Installation

```bash
# Clone the repo
git clone <repo-url>
cd ai_pdf_tool

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python main.py <pdf_path> [mode]
```

| Argument   | Description                                      | Default   |
|------------|--------------------------------------------------|-----------|
| `pdf_path` | Path to the PDF file to summarize                | required  |
| `mode`     | Output style: `summary` (paragraph) or `bullets` | `summary` |

### Examples

```bash
# Paragraph summary
python main.py samples/sample_report.pdf

# Bullet-point summary
python main.py samples/sample_report.pdf bullets
```

The final summary is printed to the terminal and saved to `output/final_summary.txt`.

## Project Structure

```
ai_pdf_tool/
├── main.py                 # Entry point — orchestrates the full pipeline
├── requirements.txt        # Dependencies (pdfplumber, ollama)
├── utils/
│   ├── pdf_utils.py        # PDF text extraction with pdfplumber
│   ├── chunk_utils.py      # Overlapping text chunking logic
│   └── llm_utils.py        # Ollama LLM interface
├── samples/                # Sample PDFs for testing
└── output/                 # Generated summaries (created at runtime)
```

## Configuration

To use a different Ollama model, change `MODEL_NAME` in `utils/llm_utils.py`:

```python
MODEL_NAME = "mistral"  # e.g. "llama3", "gemma", "phi3"
```

Chunk size and overlap can be adjusted in `utils/chunk_utils.py`:

```python
CHUNK_SIZE = 4000
OVERLAP_SIZE = 500
```

## Dependencies

| Package      | Purpose                        |
|--------------|--------------------------------|
| `pdfplumber` | Extract text from PDF files    |
| `ollama`     | Python client for Ollama API   |

## License

See [LICENSE](LICENSE).
