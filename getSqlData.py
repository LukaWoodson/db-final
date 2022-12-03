from getInput import *
from datetime import date

def getUserInfo():
    return {
        'firstName': getInputStr('\nFirst Name'),
        'lastName': getInputStr('Last Name'),
        'hashPassword': getInputStr('Password')
    }

def getFriendshipInfo():
    return {
        'friendedDate': date.today(),
        'firstUserID': getInputInt('\nFirst User ID'),
        'secondUserID': getInputInt('Second User ID'),
        'accepted': getInputBool('Has Been Accepted (y or n)'),
    }

def getListTypeInfo():
    return{
        'typeName': getInputStr('\nList Type'),
    }

def getListsInfo():
    return {
        'userID': getInputInt('\nUser ID'),
        'listType': getInputStr('List Type'),
    }

def getMangaInfo():
    return {
    'thumbnail': getInputStr('\nThumbnail Path'),
    'genre': getInputStr('Genre'),
    'rating': getInputInt('Rating (0 - 10)'),
    'author': getInputStr('Author'),
    'mangaName': getInputStr('Manga Name'),
    'progress': getInputInt('Progress')
}

def getIncludedMangaInfo():
    return {
        'listID': getInputInt('\nList ID'),
        'mangaID': getInputInt('Manga ID'),
    }

def getChaptersInfo():
    return {
        'mangaID': getInputInt('\nManga ID'),
        'chapterNumber': getInputInt('Chapter Number (Greater than 0)'),
        'pdfFile': getInputStr('PDF File Path'),
    }