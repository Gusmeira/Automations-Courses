import tabula
import pandas as pd

table = tabula.read_pdf('Automations/PDFs/PDF Extraction - Tables/weather.pdf',
                        pages=1)
print(table)

table[0].to_csv('Automations/PDFs/PDF Extraction - Tables/weather.csv',
                index=None)