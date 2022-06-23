
# Program extracting first column
import xlrd

from progress.models import Product
# from progress.models import FileModel
loc = ("/home/administrator/Projects/django-projects/progresstrade/media/products_informations_files/download_19.xls")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
 
for i in range(sheet.ncols):
    for j in range(sheet.nrows):
        Product.objects.create(
            
            category=sheet.cell_value(j, i) 
        )
        print(sheet.cell_value(j, i))
    print("------")

# def excel_upload(request):
#     loc = (f"/home/administrator/Projects/django-projects/progresstrade/media/{FileModel.objects.all().last().upload}")
#     wb = xlrd.open_workbook(loc)
#     sheet = wb.sheet_by_index(0)
#     sheet.cell_value(0,0)
#     for i in range(sheet.ncols):
#         for j in range(sheet.nrows):
#             print(sheet.cell_value(j, i))
    
