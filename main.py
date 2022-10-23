from tkinter import *
import psycopg2try:

def search(id):
 conn = psycopg2.connect(dbname="schoolhouse", user="postgres",
                         password="", host="localhost", port="5432")
 cursor = conn.cursor()
 query = '''SELECT * FROM students where id=%s'''
 cursor.execute(query, (id))

 row = cursor.fetchone()
 print(row)
 display_search_result(row)

 conn.commit()
 conn.close()