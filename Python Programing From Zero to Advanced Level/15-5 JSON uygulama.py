import json
import os


class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users=[]
        self.isLogged=False
        self.currentUser={}
        #load users form .json file
        self.loadUsers()
    def __str__(self):
        for i in self.users:
            print(i)
    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json", "r",encoding="utf8") as f:
                users=json.load(f)
                for user in users:
                    user=json.loads(user)
                    newUsers=User(username=user["username"],password=user["password"],email=user["email"])   
                    self.users.append(newUsers)
                print(self.users)
    def register(self,user:User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanici olusturuldu.\n")
    def login(self,username,password):
        for user in self.users:
            if user.username == username and user.password==password:
                self.isLogged=True
                self.currentUser=user
                print("Giris yapildi.")
                break
    def logout(self):
        self.isLogged=False
        self.currentUser={}
        print("Cikis yapildi")
    def identity(self):
        if self.isLogged:
            print(f"username: {self.currentUser.username}")
        else:
            print("Giris yapilmadi")
    def savetoFile(self):
        liste=[]
        for user in self.users:
            liste.append(json.dumps(user.__dict__))
        with open ("users.json","w") as f:
            json.dump(liste,f) #class formatýný json formatýna ekleyemediðimiz için öncesinde self.users listeye dönüþüm yapýlmalý
repository=UserRepository()
while True:
    print(" Menu ".center(50,"-"))
    secim=input("1- Register\n2- Login\n3- Logout\n4- identity\n5- Exit\nSecim: ")
    if secim is "5":
        break
    else:
        if secim is "1":
            username=input("username: ")
            password=input("password: ")
            email=input("email: ")
            user=User(username=username, password=password, email=email)
            repository.register(user)
            print( repository.__str__())
        elif secim =="2":
            if repository.isLogged:
                print("zaten giris yapildi")
            else:
                username=input("Username: ")
                password=input("Password: ")
                repository.login(username,password)
        elif secim =="3":
            repository.logout()
        elif secim =="4":
            repository.identity()
        else:
            print("Gecersiz Secim!")
            
            