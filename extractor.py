import PyPDF2
import re

def extract_foa_data(pdf_path):
    print(f"Loading FOA Document: {pdf_path}...")
    
    # 1. Ingest the PDF (The 'Semantic' first step)
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        return f"Error reading PDF: {e}"

    print("Document Ingested! Running simulated LLM extraction...\n")
    
    # 2. Simulated Entity Extraction (This is where the LLM goes in the final project)
    # We use basic regex here just to prove the pipeline architecture works
    extracted_data = {
        "Document Length": f"{len(text)} characters",
        "Potential Deadlines": set(re.findall(r'(?i)(?:deadline|due date).*?(\w+ \d{1,2}, \d{4}|\d{1,2}/\d{1,2}/\d{2,4})', text)),
        "Mentions of Funding/Money": set(re.findall(r'\$\d+(?:,\d{3})*(?:\.\d{2})?(?:\s*[mb]illion)?', text))
    }
    
    return extracted_data

# Run the pipeline
if __name__ == "__main__":
    pdf_filename = "sample_grant.pdf"
    results = extract_foa_data(pdf_filename)
    
    print("--- EXTRACTION RESULTS ---")
    for key, value in results.items():
        print(f"{key}: {value}")
    print("--------------------------")