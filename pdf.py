import PyPDF2
import os

merger_object = PyPDF2.PdfMerger()  

pdf_files = [file for file in os.listdir(os.curdir) if file.endswith(".pdf")]

if not pdf_files:
    print("No PDF files!!!")
    exit(1)

for file in pdf_files:
    try:
        merger_object.append(file)
        print(f"Merging: {file}")
    except Exception as e:
        print(f"Error while merging {file}: {e}")

output_file = "assignment(merged).pdf"

try:
    merger_object.write(output_file)
    merger_object.close()
    print(f"PDFs merged successfully!!")
except Exception as e:
    print(f"Couldn't save merged PDF: {e}")
