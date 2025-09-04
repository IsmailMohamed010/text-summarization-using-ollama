# AI Document Analyzer

This project provides an API service for summarizing text and extracting answers from uploaded documents (PDF, Word, and PowerPoint). It integrates with [Ollama](https://ollama.ai/) to generate summaries and responses using the `llama3.2:1b` model.  

The API is built with [Flask](https://flask.palletsprojects.com/), and supports structured text processing pipelines for professional developers building document intelligence or knowledge extraction tools.

---

## Techniques Used

- **[Flask request handling](https://flask.palletsprojects.com/en/latest/api/#incoming-request-data)** for managing JSON and file uploads.  
- **[File upload handling with Flask](https://flask.palletsprojects.com/en/latest/patterns/fileuploads/)** using `request.files` and safe persistence.  
- **[os.makedirs](https://docs.python.org/3/library/os.html#os.makedirs)** for ensuring upload directories exist without race conditions.  
- **[PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)** (`fitz`) for extracting text from PDFs.  
- **[python-docx](https://python-docx.readthedocs.io/)** for parsing Microsoft Word `.docx` files.  
- **[python-pptx](https://python-pptx.readthedocs.io/)** for extracting text from PowerPoint presentations.  
- **[Ollama generate API](https://github.com/ollama/ollama/blob/main/docs/api.md#generate-a-completion)** for prompt-based summarization and Q&A with the LLaMA model.  

---

## Interesting Non-Obvious Technologies

- **[Ollama](https://ollama.ai/)**: A local model runner for LLaMA, enabling inference without external APIs.  
- **[PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)**: Offers higher-quality text extraction from PDFs than many alternatives, especially when handling layout and embedded text objects.  
- **[python-pptx](https://python-pptx.readthedocs.io/)**: Often overlooked, but enables direct programmatic access to PowerPoint slide text.  

---

## Requirements

This project depends on the following Python packages:

- [Flask](https://flask.palletsprojects.com/)  
- [Ollama](https://ollama.ai/)  
- [PyMuPDF](https://pymupdf.readthedocs.io/) (`pymupdf`)  
- [python-docx](https://python-docx.readthedocs.io/)  
- [python-pptx](https://python-pptx.readthedocs.io/)  

All dependencies are listed in [`requirements.txt`](./requirements.txt).  

---

## Project Structure

```bash
.
├── API.py
├── app.py
├── uploaded_files/
```

- **[`API.py`](./API.py)** – Defines the Flask API endpoints (`/summarize`, `/analyze`) and manages request validation and file uploads.  
- **[`app.py`](./app.py)** – Handles text summarization, question answering, and extraction of text from different document formats.  
- **`uploaded_files/`** – Directory where uploaded documents are stored before being processed.  
