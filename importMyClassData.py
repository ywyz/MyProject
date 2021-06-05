import pymysql
from openpyxl import load_workbook
db = pymysql.connect(host="localhost", user="root", password="yw980924@163.com", database="student_information")
cursor = db.cursor()
filename = input("请拖入文件：")
wb = load_workbook(filename=filename)
ws = wb['Sheet1']
for row in ws.rows:
    if row[0].value == "入园儿童登记表" or row[0].value == "小一班" or row[0].value == "入托时间":
        continue
    elif row[0].value == 44075:
        SQLUpdate = "UPDATE student_basic set work_address = '%s' where studentName = '%s'" % \
                    (row[8].value, row[1].value)
        print("更新成功")
    elif row[0].value == 44248:
        name = row[1].value
        parentName = row[6].value
        parentNumber = row[11].value
        Grade = "小班"
        Class = "一班"
        Address = row[12].value
        workAddress = row[8].value
        SqlInsert = "INSERT INTO student_basic (studentname, grade, class, parentName_One, parentPhone_one, address, work_address) \
                          VALUES('%s', '%s', '%s','%s', '%s', '%s', '%s') " % \
                    (name, Grade, Class, parentName, parentNumber, Address, workAddress)
        cursor.execute(SqlInsert)
        db.commit()
    else:
        continue
    cursor.execute(SQLUpdate)
    db.commit()

db.close()
