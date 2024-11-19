## pip install pymupdf4llm

import pymupdf4llm
import pathlib
#Extracting Text: 
md_text = pymupdf4llm.to_markdown("./documents/mfund.pdf")
print(md_text)

#store your Markdown file, e.g. store as a UTF8-encoded file.
#import pathlib
output_file = pathlib.Path("./documents/mfund.md")
output_file.write_bytes(md_text.encode())


#Table Extraction: Turning Tables into Data.
md_text_tables = pymupdf4llm.to_markdown(
    doc="input_tables.pdf" #"./documents/mfund.md"
)

md_text_tables

# Image Extraction: Bringing Images to Life
md_text_images = pymupdf4llm.to_markdown(
    doc="input_images.pdf", #"./documents/mfund.md"
    pages=[0, 2],
    page_chunks=True,
    write_images=True,
    image_path="images",
    image_format="png",
    dpi=300
)

#Document Structure: Secrets of Complex PDFs,create custom data structures for your LLM.
#(Detailed word-by-word extraction)
md_text_words = pymupdf4llm.to_markdown(
    doc="input.pdf",
    pages=[0, 1, 2],
    page_chunks=True,
    write_images=True,
    image_path="images",
    image_format="png",
    dpi=300,
    extract_words=True
)



