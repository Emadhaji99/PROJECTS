from bidi.algorithm import get_display
import os
import arabic_reshaper
import csv 
import openpyxlss
#Extracting The Data From Main File

Main_file = r"C:\project\profession\Technology\Digital Technology\resume\Projects\Automation\Automation finance\Budgeting\expense.csv" 
with open(Main_file, mode="r", newline="", encoding="utf-8-sig") as csvfile: 
    reader = csv.DictReader(csvfile) 
    for row in reader:
        Type=row['مبلغ گردش بدهکار']
        if eval(Type)!=0:
            reshaped = arabic_reshaper.reshape(str(f"در تاریخ  {row["تاریخ"]}و  ساعت{row['زمان']}و این تراکنش به مبلغ برداشتی  {row['مبلغ گردش بدهکار']} به شرح {row['شرح']} برای چیه ?"))
            bidi_text = get_display(reshaped)
            Expense_Field=input(bidi_text).upper()
# Writing In Excell File 

        else:
                reshaped = arabic_reshaper.reshape(str(f"در تاریخ  {row["تاریخ"]}و  ساعت{row['زمان']}و این تراکنش به مبلغ وازیزی {row['مبلغ گردش بستانکار']} به شرح {row['شرح']} برای چیه ?"))
                bidi_text = get_display(reshaped)
                Income_Field=input(bidi_text).upper()

        
