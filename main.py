from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
Builder.load_file("LoginPage.kv")

users = {"Italian_player":"Fr3sh_pa$ta","CatMouseChase":"Tom&J3rry"}

class LoginPageApp(App):
    def build(self):
        return LoginManager()

class LoginManager(ScreenManager):
    pass

class LoginPageScreen(Screen):
    def userinfo(self,username,password):
        if username in users and password == users[username]:
            self.manager.current = "logged_in_page"
        else:
            self.ids.invalid_info.text = "Username or Password incorrect"
            self.ids.invalid_info.color = "red"

    def account_register(self,bool):
        if bool:
            self.manager.current = "register_page"



class AccountRegisterScreen(Screen):
    def create_account(self,user,password,confirm_password):
        numbers = "1234567890"
        special_char = "~!@#$%^&*_"
        for i in numbers:
            for j in special_char:
                if user not in users and i in password and j in password and password.isupper() == False and password.islower() == False and len(user)>=8 and len(password)>=8 and confirm_password == password:
                    users[user] = password
                    self.manager.current = "login_page"
                else:
                    self.ids.invalid_info.text = "Invalid"
                    self.ids.invalid_info.color = "red"


    def goback(self,bool):
        if bool:
            self.manager.current = "login_page"

class LoggedInScreen(Screen):
    def logout(self,bool):
        if bool:
            self.manager.current = "login_page"

LoginPageApp().run()