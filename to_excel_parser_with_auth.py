import xlsxwriter as xl
from parser_with_auth import array

def writer(parametr):
    """Функция записи в excel файл."""
    book = xl.Workbook('C:\\Dev\\data_auth.xlsx') #Не забудь указать актуальный путь!
    page = book.add_worksheet('Wbnfns')

    row = 0
    column = 0
    page.set_column('A:A', 50)
    page.set_column('B:B', 20)
    page.set_column('C:C', 50)

    for item in parametr():
        for i in range(3):
            page.write(row, column+i, item[0+i])
        row +=1

    book.close()

writer(array)
