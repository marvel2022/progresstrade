import xlrd
 
loc = ("/home/administrator/Projects/django-projects/progresstrade/progress")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 
sheet.cell_value(0, 0)
 
print(sheet.row_values(1))