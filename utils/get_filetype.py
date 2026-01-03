import os
import struct

def detect_file_type(file_path):
    """
    Detect if a file is PDF, Excel, Word, CSV, or plain text
    based on magic bytes and heuristics.
    Returns a string: 'pdf', 'excel', 'word', 'csv', 'text', or None
    """
    if not os.path.isfile(file_path):
        return None

    try:
        with open(file_path, "rb") as f:
            header = f.read(8)  
            if header.startswith(b"%PDF-"):
                return "pdf"
            if header.startswith(b"PK\x03\x04"):
                import zipfile
                f.seek(0)
                with zipfile.ZipFile(f) as z:
                    namelist = z.namelist()
                    if any(n.startswith("xl/") for n in namelist):
                        return "excel"
                    if any(n.startswith("word/") for n in namelist):
                        return "word"
                    return None

            if header[:2] == b"\xD0\xCF":
                return "excel_or_word" 

            f.seek(0)
            text_start = f.read(2048)
            try:
                decoded = text_start.decode("utf-8")
                if "," in decoded or "\t" in decoded:
                    return "csv"
                else:
                    return "text"
            except UnicodeDecodeError:
                return None

    except Exception:
        return None
