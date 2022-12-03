import mysql.connector
from home import *

context = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MySQL12345!",
    database = "manga_site"
)

cursor = context.cursor()

greeting(cursor, context)