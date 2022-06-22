from pathlib import Path


TEMPLATE_PATH = Path(__file__).absolute().parent.parent / "template"
OUTPUT_DIR = TEMPLATE_PATH.with_name("output")
OUTPUT_DIR.mkdir(exist_ok=True)
