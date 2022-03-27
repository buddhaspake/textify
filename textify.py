from pathlib import Path
from datetime import datetime
from pdf2image import convert_from_path
from pytesseract import image_to_string


# Utility functions
def tstamp():
    try:
        now = datetime.now()
        return now.strftime('%Y%m%d_%H%M%S')
    except Exception as e:
        raise Exception(f'tstamp() failed: {e}')


if __name__ == '__main__':
    try:
        SCAN_DPI = 250
        IMAGE_FORMAT = 'png'
        IN_PATH = Path('input')
        PROC_PATH = Path('proc')
        OUT_PATH = Path('output')
        # Scan through PDFs
        for ifile in IN_PATH.glob('**/*.pdf'):
            # A. Make directories
            procdir = PROC_PATH / f'{ifile.stem}_{tstamp()}'
            procdir.mkdir(parents=True, exist_ok=True)
            outpath = \
                (OUT_PATH / ifile.relative_to(IN_PATH)) \
                .with_suffix('.txt')
            outpath.parent.mkdir(parents=True, exist_ok=True)
            # B. Convert to pages
            pages = convert_from_path(
                str(ifile),
                dpi=SCAN_DPI,
                output_folder=str(procdir),
                fmt=IMAGE_FORMAT,
                output_file='page',
                paths_only=True
            )
            images_fpath = procdir / '_images.txt'
            with open(images_fpath, 'w', encoding='utf-8') as ifptr:
                ifptr.write('\n'.join(pages))
            # C. Perform OCR
            file_text = None
            try:
                file_text = image_to_string(str(images_fpath), lang='eng')
                with open(outpath, 'w', encoding='utf-8') as ofptr:
                    ofptr.write(file_text)
            except Exception as e:
                raise Exception(f'OCR failed: {e}')
    except Exception as e:
        print(f'textify.py failed: {e}')
