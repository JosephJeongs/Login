from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
Builder.load_file("LoginPage.kv")

users = {"Italianplayer":"Fr3shpa$ta","CatMouseChase":"Tom&J3rry"}

class LoginPageApp(App):
    def build(self):
        return LoginManager()

class LoginManager(ScreenManager):
    pass

class LoginPageScreen(Screen):

    def userinfo(self,username,password):
            if username in users and password == users[username]:
                self.manager.current = "loggedinpage"
    def accountregister(self,bool):
        if bool:
            self.manager.current = "registerpage"



class AccountRegisterScreen(Screen):
    def createaccount(self,user,password,confirmpassword):
        numbers = "1234567890"
        specialchar = "~!@#$%^&*"
        if user not in users:
            for i in numbers:
                for j in specialchar:
                    if i in password:
                        if j in password:
                            if password.isupper() == False and password.islower() == False:
                                if len(user)>=8 and len(password)>=8:
                                    if confirmpassword == password:
                                        self.manager.current = "loginpage"

    def goback(self,bool):
        if bool:
            self.manager.current = "loginpage"



class LoggedInScreen(Screen):
    def logout(self,bool):
        if bool:
            self.manager.current = "loginpage"

LoginPageApp().run()