users = (
    "insert into users " 
    "(firstName, lastName, hashPassword) "
    "values (%(firstName)s, %(lastName)s, %(hashPassword)s)"
)

friendship = (
    "insert into friendship "
    "(friendedDate, firstUserID, secondUserID, accepted) " 
    "values (%(friendedDate)s, %(firstUserID)s, %(secondUserID)s, %(accepted)s)"
)

listType = (
    "insert into listType "  
    "(typeName) "
    "values (%(typeName)s)"  
)

lists = (
    "insert into lists "    
    "(userID, listType) "
    "values (%(userID)s, %(listType)s)" 
)

manga = (
    "insert into manga "    
    "(thumbnail, genre, rating, author, mangaName, progress) "
    "values (%(thumbnail)s, %(genre)s, %(rating)s, %(author)s, %(mangaName)s, %(progress)s)" 
)

includedManga = (
    "insert into includedManga "    
    "(listID, mangaID) "
    "values (%(listID)s, %(mangaID)s)" 
)

chapters = (
    "insert into chapters "    
    "(mangaID, chapterNumber, pdfFile) "
    "values (%(mangaID)s, %(chapterNumber)s, %(pdfFile)s)" 
)