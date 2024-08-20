from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

files_path = glob.glob("invoices/*.xlsx")

for i in files_path:
    df = pd.read_excel(i, sheet_name="Sheet 1")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(i).stem
    invoice_no, date = filename.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice No.{invoice_no}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}")

    pdf.output(f"results/{filename}.pdf")

