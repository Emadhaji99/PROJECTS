import openpyxl

wb=openpyxl.load_workbook("SAMPEL.xlsx")
Sheet=wb["Sheet1"]
coloumn=Sheet["B"]
for cell in coloumn:
        if ":" in str(cell.value):
                Row=cell.row
                c_coloumn=cell.column
                Sheet.cell(
                        column=int(c_coloumn),
                           row=int(Row)+1,
                           value="salam"
                           )
wb.save("SAMPEL.xlsx")