from getSqlData import *
import queries
import time
import os
from printUtils import colors as c, printColor, printTable
import mysql.connector

tables = [
    {
        'name': 'Users',
        'inputGetter': getUserInfo,
        'query': queries.users,
        'table': 'users'
    },
    {
        'name': 'Friendship',
        'inputGetter': getFriendshipInfo,
        'query': queries.friendship,
        'table': 'friendship'
    },
    {
        'name': 'List Type',
        'inputGetter': getListTypeInfo,
        'query': queries.listType,
        'table': 'listType'
    },
    {
        'name': 'Lists',
        'inputGetter': getListsInfo,
        'query': queries.lists,
        'table': 'lists'
    },
    {
        'name': 'Manga',
        'inputGetter': getMangaInfo,
        'query': queries.manga,
        'table': 'manga'
    },
    {
        'name': 'Included Manga',
        'inputGetter': getIncludedMangaInfo,
        'query': queries.includedManga,
        'table': 'includedManga'
    },
    {
        'name': 'Chapters',
        'inputGetter': getChaptersInfo,
        'query': queries.chapters,
        'table': 'chapters'
    }
]

def home():
    os.system('cls')
    for i, table in enumerate(tables):
        name = table.get('name')
        printColor(f'{i + 1} - {name}', c.CYAN)
    chosenNum = getInputInt('\nPlease Choose a Number Above') - 1
    if chosenNum >= 0 and chosenNum < len(tables): return chosenNum
    return home()
    
        
    
def greeting(cursor, context):
    os.system('cls')
    printColor('\nWould you like to (r)ead or (w)rite?', c.HEADER)
    choice = input()
    if choice == 'r':
        printColor('\nHappy Reading!', c.BLUE)
        time.sleep(1.5)
        index = home()
        read(cursor, context, index)
    elif choice == 'w':
        printColor('\nHappy Writing!', c.BLUE)
        time.sleep(1.5)
        index = home()
        write(cursor, context, index)
    else:
        printColor('\nNot a valid option', c.WARNING)
        time.sleep(2.0)
        return greeting(cursor, context)
    
    
    
def write(cursor, context, index):
    result = tables[index]['inputGetter']()
    query = tables[index]['query'] 
    try:
        cursor.execute(query, result)
        context.commit()
        name = tables[index]['name']
        printColor(f'\n Data Saved to {name}', c.GREEN)
        time.sleep(2.0)
        return greeting(cursor, context)
    except mysql.connector.Error as err:
        printColor(err, c.FAIL)
        input('\nPress Enter to Continue...')
        return greeting(cursor, context)
    
    
    
def read(cursor, context, index):
    tableName = tables[index]['table']
    try:
        query = f'select * from {tableName}'
        cursor.execute(query)
        context.commit()
        results = cursor.fetchall()
        printTable(cursor, results)
        printColor('\nPress Enter to Continue...', c.GREEN)
        input()
        return greeting(cursor, context)
    except mysql.connector.Error as err:
        printColor(err, c.FAIL)
        input('\nPress Enter to Continue...')
        return greeting(cursor, context)