import xlsxwriter

workbook = xlsxwriter.Workbook('mon_excel.xlsx')
worksheet = workbook.add_worksheet()

format_total = workbook.add_format()
format_total.set_bold()
format_total.set_bg_color('yellow')

worksheet.write(0, 0, "Pomme")
worksheet.write(1, 0, "Poire")
worksheet.write(2, 0, "Kiwi")

worksheet.write(0, 1, 10)
worksheet.write(1, 1, 8)
worksheet.write(2, 1, 5)

worksheet.write(3, 0, "Total", format_total)
worksheet.write_formula(3, 1, 'SUM(B1:B3)', format_total)


workbook.close()

