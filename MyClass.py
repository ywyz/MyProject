import pymysql
from openpyxl import load_workbook
db = pymysql.connect(host="localhost", user="root", password="yw980924@163.com", database="student_information")
cursor = db.cursor()
