def drawLines():
    line_row = ''
    line_col = ''
    for i in range(0,61):
        line_row += '-'
        if ( i % 10 == 0 ):
            line_col += '|'
        else:
            line_col += ' '
    print(line_row)

    for i in range(0,5):
        print(line_col)

for i in range(0,6):
    drawLines()


