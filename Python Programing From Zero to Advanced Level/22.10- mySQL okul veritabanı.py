from datetime import date

import mysql.connector

from connection import connection


class student:
    connection=connection
    mycursor=connection.cursor()
    def __init__(self,studentnumber,name,surname,birthdate,gender):
        self.studentnumber=studentnumber
        self.name=name
        self.surname=surname
        self.birthdate=birthdate
        self.gender=gender
    mycursor.rowcount
    def savestudent(self):
        sql="INSERT INTO student(studentnumber,name,surname,birthdate,gender) VALUES(%s,%s,%s,%s,%s)"
        value=(self.studentnumber,self.name,self.surname,self.birthdate,self.gender)
        student.mycursor.execute(sql,value)
        try:
            student.connection.commit()
            print(f"{student.mycursor.rowcount} tane kayıt eklendi")
        except mysql.connector.Error as err:
            print("hata: ",err)
        finally:
            print("işlem sonlandırıldı.")
            student.connection.close()
    def deleteStudent():
        pass
    @staticmethod
    def savestudents(studentlist):
        sql="INSERT INTO student(studentnumber,name,surname,birthdate,gender) VALUES(%s,%s,%s,%s,%s)"
        values=studentlist
        student.mycursor.executemany(sql,values) #çoklu ekleme olacağı için many kullanılır
        
        try:
            student.connection.commit()
            print(f"{student.mycursor.rowcount} tane kayıt eklendi")
        except mysql.connector.Error as err:
            print("hata: ",err)
        finally:
            print("işlem sonlandırıldı.")
            student.connection.close()
    def getallstudentlog(self):
        # sql="select count(id) from student"
        # sql="select * from student"
        # sql="select studentnumber,name,surname from student"
        # sql="select name,surname from student where gender='K'"
        # sql="select * from student where birthdate= 2005 and name='Ali'"
                # sql="select * from student where YEAR(birthdate)= 2005 and name='Ali'"
        # sql="select name,surname from student where name LIKE '%a%'  and  surname LIKE '%a%'"
        # sql="select count(id) from student where gender='E'"
        sql="select name,surname from student where gender='K' order by name asc"

        student.mycursor.execute(sql)
        result=student.mycursor.fetchall()
        print(result)
    @staticmethod
    def getstudentbyid(id):
        sql="select * from student where id=%s"
        value=(id,)
        student.mycursor.execute(sql,value)
        try:
            return student.mycursor.fetchone()
        except mysql.connector.Error as err:
            print("Error ", err)
        finally:
            print("operation is done")
            student.connection.close()
    def updatestudent(self):
        sql="update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values=(self.studentnumber, self.name, self.surname, self.birthdate,self.gender, self.id)
        student.mycursor.execute(sql,values)
        
        try:
            student.connection.commit()
            print(f"{student.mycursor.rowcount} tane kayıt güncellendi")
        except mysql.connector.Error as err:
            print("hata: ",err)
# ahmet=student(301,"Ahmet","Yılmaz",date(2005, 5, 17),"E")
# ahmet.savestudent()

# studentlist = [
#     ("301","Ahmet","Yılmaz",date(2005, 5, 17),"E"),
#     ("302","Ali","Can",date(2005, 6, 17),"E"),
#     ("303","Canan","Tan",date(2005, 7, 7),"K"),
#     ("304","Ayşe","Taner",date(2005, 9, 23),"K"),
#     ("305","Bahadır","Toksöz",date(2004, 7, 27),"E"),
#     ("306","Ali","Cenk",date(2003, 8, 25),"E")
# ]
# student.savestudents(studentlist)

print(student.getstudentbyid(4))