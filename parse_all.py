import fitz
import json
import re
import os

pdf_path = r'c:\Users\LILI\OneDrive - PDK Jateng\Dokumen\OSN\BANK SOAL OSN SD.pdf'
base_dir = os.path.dirname(os.path.abspath(__file__))
out_dir = os.path.join(base_dir, 'data')
img_dir = os.path.join(base_dir, 'images')
os.makedirs(out_dir, exist_ok=True)
os.makedirs(img_dir, exist_ok=True)

doc = fitz.open(pdf_path)

def clean_line(l):
    return l.replace('\u200c', '').strip()

def get_page_lines(page_num_1based):
    page = doc[page_num_1based - 1]
    lines = [clean_line(l) for l in page.get_text().splitlines() if clean_line(l)]
    # filter out running headers/footers
    filtered = []
    for l in lines:
        if l in ['Kumpulan Soal OSN', 'Pusat Prestasi Nasional', 'Kumpulan Soal Olimpiade Sains Nasional', 'Jenjang SMP']:
            continue
        if re.match(r'^\d+$', l):
            continue
        if l.startswith('Soal OSN ') or l.startswith('Kunci Jawaban ') or l == 'Pilihan Jamak' or l == 'Soal Pilihan Jamak':
            continue
        filtered.append(l)
    return filtered

print("PDF opened successfully. Ready to parse sections.")
