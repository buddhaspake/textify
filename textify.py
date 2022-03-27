from pathlib import Path
from pdf2image import convert_from_path

if __name__ == '__main__':
    try:
        IN_PATH = Path('input')
        PROC_PATH = Path('proc')
        OUT_PATH = Path('output')
        # Scan through PDFs
        for ifile in IN_PATH.glob('**/*.pdf'):
            procdir = PROC_PATH / '{ifile.stem}_pages'
            procdir.mkdir(parents=True, exists_ok=True)
            pages = convert_from_path
    except Exception as e:
        print(f'textify.py failed: {e}')
