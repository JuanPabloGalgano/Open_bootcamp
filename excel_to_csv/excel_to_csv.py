import pandas as pd
import openpyxl

# Lee el archivo Excel
df = pd.read_excel('excel_to_csv\\prueba.xlsx')

# Escribe el archivo CSV
df.to_csv('convertido.csv', index=False, encoding='utf-8')