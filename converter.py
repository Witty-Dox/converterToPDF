from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.add_font('DejaVu', '', 'fonts/DejaVuSansCondensed.ttf', uni=True)
pdf.set_font("DejaVu", size = 15)

def choose():
    way = input('Введите режим работы:\n1 - быстрый режим, создаёт pdf файл из вводимых в консоль строк\n2 - дополненый режим, создаёт pdf файл из текстового файла input.txt (параметры заполнения в README.)\n|')

    if way not in ['1', '2']:
        print('\nТакого варианта не существует! Напишите 1 или 2.\n\n')
        choose()
    
    outname = input('\nВведите название итогового pdf файла: |')

    if way == '1':
        firstway(outname)

def firstway(outname):
    try:
        lncount = int(input('\nВведите количество заголовков: |'))
    except ValueError:
        print('\nВы ввели не число а текст!')
        firstway
    if lncount == None:
        print('Вы ничего не ввели!')
    for line in range(lncount):
        print(line)

choose()


# pdf.set_text_color(79, 90, 97)

# pdf.multi_cell(0, 30, txt = "GeeksforGeeks", align = 'C')
 
# pdf.multi_cell(0, 10, txt = "", align = 'C')

# pdf.output(".pdf")