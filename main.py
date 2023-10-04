from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
Builder.load_file("LoginPage.kv")

class LoginPageApp(App):
    def build(self):
        return LoginManager()

class LoginManager(ScreenManager):
    pass





class LoginPageScreen(Screen):
    #users = {"ItalianPlayer":"Fr3shPa$ta!"}

    def userinfo(self,username):
        if username == "ItalianPlayer":
            self.manager.current = "loggedinpage"
        else:
            #self.ids.invalid_information.text = "Invalid guess \n\n Try again"
            #self.ids.invalid_information.color = "red"
            pass





class AccountRegisterScreen(Screen):
    pass


class LoggedInScreen(Screen):
    def logout(self,bool):
        if bool:
            self.manager.current = "loginpage"

LoginPageApp().run()




#####deleted code#####

# TextInput:
#             id: user
#             hint_text: "Enter username"
#             size_hint: .25,.05
#             pos: "345dp","387dp"
#         TextInput:
#             id: pass
#             hint_text: "Enter password"
#             size_hint: .25,.05
#             pos: "345dp","337dp"
#
#         Button:
#             text: "Register new account"
#             pos: "365dp","286dp"
#             size_hint: .2,0.03
#
#         Button:
#             text: "Login"
#             size_hint: .25,.05
#             pos: "345dp","230dp"
#             on_release: root.userinfo(user.text)
#
#
#
#
# <LoggedInScreen>:
#     Label:
#         text: "Welcome"
#         size_hint: 1,.5
#         pos_hint: {"center_y":.6}
#     Button:
#         text: "Log Out"
#         size_hint: .15,.1
#         pos_hint: {"center_x":.5,"center_y":.2}
#         on_release: root.logout(True)