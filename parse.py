import pymupdf4llm
import pathlib

md_text = pymupdf4llm.to_markdown(
    doc="/Users/csinger/projects/agentic-tutor/content/physics1.pdf",
    pages=[x for x in range(0, 30)],
    page_chunks=False,
    write_images=True,
    image_path="content/images",
    image_format="jpg",
    dpi=200,
    extract_words=False,
)

pathlib.Path("output/physics1.md").write_bytes(md_text.encode())
