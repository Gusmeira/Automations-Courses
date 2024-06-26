from fpdf import FPDF
import pandas as pd

df = pd.read_excel('Automations/PDFs/PDF Creator - Pandas/data.xlsx')

for index, row in df.iterrows():
    pdf = FPDF(orientation='P',
               unit='pt',
               format='A5')
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=20)
    pdf.cell(w=0, h=50, txt=row['name'], align='C', ln=3)

    for column in df.columns:
        pdf.set_font(family='Times', style='B', size=12)
        pdf.cell(w=80, h=20, txt=f'{column.capitalize()}:')
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=0, h=20, txt=row[column], ln=1)

    pdf.output(f'Automations/PDFs/PDF Creator - Pandas/{row['name']}.pdf')