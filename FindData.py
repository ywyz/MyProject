import pymysql

db = pymysql.connect(host="localhost", user="root", password="yw980924@163.com", database="student_information")
cursor = db.cursor()


def returnName(name):
    print(name)
    return name


def returnParentName(ParentName):
    print(ParentName)
    return ParentName


def returnPhone(PhoneNumber):
    print(PhoneNumber)
    return PhoneNumber


def returnAddress(Address):
    print(Address)
    return Address


def getName():
    students_name = []
    name = input("请输入学生姓名：(q 退出)")
    while name != 'q':
        students_name.append(name)
        name = input("请输入学生姓名：(q 退出)")
    return students_name


def searchResult(students_name):
    if not students_name:
        print("姓名不能为空")
    else:
        for s_name in students_name:
            resultSearch = "select parentName_One, parentPhone_One, address from student_basic \
            where studentName = '%s' " % s_name
            cursor.execute(resultSearch)
            results = cursor.fetchall()
            for tuple1 in results:
                returnName(s_name)
                returnParentName(tuple1[0])
                returnPhone(tuple1[1])
                returnAddress(tuple1[2])

