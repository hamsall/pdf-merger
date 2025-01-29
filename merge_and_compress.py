from PyPDF2 import PdfMerger
import pikepdf
import os

# Merge PDFs first
pdfs = [f for f in os.listdir() if f.endswith(".pdf") and f != "merged.pdf"]
merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_uncompressed.pdf")
merger.close()

# Compress the merged file
with pikepdf.open("merged_uncompressed.pdf") as pdf:
    pdf.save(
        "merged_compressed.pdf",
        compress_streams=True,  # Compress text/streams
        linearize=True,         # Web optimization
        object_stream_mode=pikepdf.ObjectStreamMode.generate
    )

# Clean up temporary file
os.remove("merged_uncompressed.pdf")