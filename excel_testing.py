# check the default.xlsx file is present in the same directory
# if not present, create a new file with the name default.xlsx
# and append the dictionary data to the file


import os
import openpyxl

# check the default.xlsx file is present in the same directory

if os.path.isfile('default.xlsx'):
    print('File exists')
else:
    print('File does not exist')
    wb = openpyxl.Workbook()
    wb.save('default.xlsx')


super_list = [(11,21,3),(41,5,6),(71,8,9)]
# and append super_list to the file
wb = openpyxl.load_workbook('default.xlsx')
sheet = wb.active
for row in super_list:
    sheet.append(row)
wb.save('default.xlsx')

