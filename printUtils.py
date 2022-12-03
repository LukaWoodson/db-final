import mysql.connector
class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BASE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def printColor(message, color):
    print(f'{color}{message}{colors.BASE}')
    
def printTable(cursor, results):    
    widths = []
    columns = []
    tavnit = '|'
    separator = '+' 
    
    maxValues = [0] * len(results[0])
    for row in results:
        for j, column in enumerate(row):
            maxValues[j] = max(maxValues[j], len(str(column)))

    for i, cd in enumerate(cursor.description):
        widths.append(max(maxValues[i], len(cd[0])))
        columns.append(cd[0])

    for w in widths:
        tavnit += ' %-'+'%ss |' % (w,)
        separator += '-'*w + '--+'

    print(f'\n{separator}')
    print(tavnit % tuple(columns))
    print(separator)
    for row in results:
        print(tavnit % row)
    print(separator)