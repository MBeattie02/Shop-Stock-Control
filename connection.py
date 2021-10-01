import sqlite3

def Database():
    global conn, cursor
    conn = sqlite3.connect('supervalu.db')
    cursor = conn.cursor()

   
