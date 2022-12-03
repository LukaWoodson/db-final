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
    
def printTable(cursor, context, tableName):
    query = f'select * from {tableName}'
    cursor.execute(query)
    context.commit()
    results = cursor.fetchall()

    widths = []
    columns = []
    tavnit = '|'
    separator = '+' 

    for cd in cursor.description:
        widths.append(max(cd[2], len(cd[0])))
        columns.append(cd[0])

    for w in widths:
        tavnit += ' %-'+'%ss |' % (w,)
        separator += '-'*w + '--+'

    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in results:
        print(tavnit % row)
    print(separator)