#Create Excel File Through a Python Script
from openpyxl import Workbook
import time 

wb=Workbook()
sheet=wb.active

sheet["A1"]="Tamil"
sheet["B1"]="English"
sheet["C1"]="Maths"
sheet["D1"]="science"
sheet["E1"]="social science"


wb.save("index.xlsx")