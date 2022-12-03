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

def home(cursor, context, choice = None):
    os.system('cls')
    for i, table in enumerate(tables):
        name = table.get('name')
        printColor(f'{i + 1} - {name}', c.CYAN)
    chosenNum = getInputInt('\nPlease Choose a Number Above') - 1
    # if user chooses to write to database
    if choice == 'w':
        write(cursor, context, chosenNum, choice)
    # if user chooses to read from database
    elif choice == 'r':
        read(cursor, context, chosenNum, choice)
    
        
    
def greeting(cursor, context):
    os.system('cls')
    printColor('\nWould you like to (r)ead or (w)rite?', c.HEADER)
    choice = input()
    if choice == 'r':
        printColor('\nHappy Reading!', c.BLUE)
        time.sleep(1.5)
        home(cursor, context, choice)
    elif choice == 'w':
        printColor('\nHappy Writing!', c.BLUE)
        time.sleep(1.5)
        home(cursor, context, choice)
    else:
        printColor('\nNot a valid option', c.WARNING)
        time.sleep(2.0)
        return greeting(cursor, context)
    
    
    
def write(cursor, context, chosenNum, choice):
    if chosenNum >= 0 and chosenNum < len(tables):
        result = tables[chosenNum]['inputGetter']()
        query = tables[chosenNum]['query'] 
        try:
            cursor.execute(query, result)
            context.commit()
            name = tables[chosenNum]['name']
            printColor(f'\n Data Saved to {name}', c.GREEN)
            time.sleep(2.0)
            return home(cursor, context, choice)
        except mysql.connector.Error as err:
            printColor(err, c.FAIL)
            input('\nPress Enter to Continue...')
            return home(cursor, context, choice)
    else:
        printColor('Not a valid number', c.WARNING)
        input('\nPress Enter to continue...')
        return home(cursor, context, choice)
    
    
    
def read(cursor, context, chosenNum, choice):
    if chosenNum >= 0 and chosenNum < len(tables):
        try:
            printTable(cursor, context, tables[chosenNum]['table'])
            printColor('\nPress Enter to Return to the Main Menu...')
            return home(cursor, context, choice)
        except mysql.connector.Error as err:
            printColor(err, c.FAIL)
            input('\nPress Enter to Continue...')
            return home(cursor, context, choice)
    else:
        printColor('Not a valid number', c.WARNING)
        input('\nPress Enter to continue...')
        return home(cursor, context, choice)