from fpdf import FPDF
import os
from sys import exit

clear = lambda: os.system('cls')

clear()

pdf = FPDF()
pdf.add_page()
pdf.add_font('DejaVu', '', 'fonts/DejaVuSansCondensed.ttf', uni=True)

def choose():
    clear()
    way = input('Введите режим работы:\n1 - быстрый режим, создаёт pdf файл из вводимых в консоль строк\n2 - дополненый режим, создаёт pdf файл из текстового файла input.txt (параметры заполнения в README.)\n|')

    if way not in ['1', '2']:
        print('\nТакого варианта не существует! Напишите 1 или 2.\n\n')
        choose()
    
    outname = input('\nВведите название итогового pdf файла: |')

    if way == '1':
        firstway(outname)

def firstway(outname):
    clear()
    try:
        lncount = int(input('\nВведите количество заголовков: |'))
    except ValueError:
        print('\nВы ввели не число а текст!')
        firstway(outname)
    
    if lncount == 0:
        print('Вы ввели 0, будет создан пустой файл!')
        firstway()

    for line in range(lncount):
        title = input(f'Введите заголовок №{line + 1}: |')
        paragraph = input(f'Введите параграф №{line + 1}: |')
        pdf.set_font("DejaVu", size = 15)
        pdf.multi_cell(0, 30, txt = title, align = 'C')
        pdf.set_font("DejaVu", size = 12)
        pdf.multi_cell(0, 10, txt = f'      {paragraph}', align = 'J')
    
    pdf.output(f"{outname}.pdf")

    print(f'Документ готов! Смотрите файл {outname}.pdf')

    exit()


choose()

# pdf.set_text_color(79, 90, 97)