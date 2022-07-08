import xlsxwriter as xl
from parser_url import array

def writer(parametr):
    """Функция записи в excel файл."""
    book = xl.Workbook('C:\\Dev\\data.xlsx') #Не забудь указать актуальный путь!
    page = book.add_worksheet('Товар')

    row = 0
    column = 0
    page.set_column('A:A', 20)
    page.set_column('B:B', 20)
    page.set_column('C:C', 50)
    page.set_column('D:D', 50)

    for item in parametr():
        for i in range(4):
            page.write(row, column+i, item[0+i])
        row +=1

    book.close()

writer(array)
