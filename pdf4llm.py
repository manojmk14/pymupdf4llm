import pymupdf4llm
md_text = pymupdf4llm.to_markdown("./documents/sbi-liquid-fund.pdf")
print(md_text)