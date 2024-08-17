from fpdf import FPDF
import pandas as pd
import glob

files_path = glob.glob("invoices/*.xlsx")

for i in files_path:
    df = pd.read_excel(i, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

