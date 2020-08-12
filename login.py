from tkinter import*
from PIL import ImageTk
class Login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+50+50")
        
        #---images---
        self.bg_icon=ImageTk.PhotoImage(file="bg.png")
        self.user_icon=PhotoImage(file="user.png")
        self.user_icon=PhotoImage(file="password.jpg")

        title=Label(self.root,text="login System",font=("times new roman",40,"bold"))
        title.place(x=0,y=0,relwidth=1)


        




root=Tk()
obj=Login_system(root)
root.mainloop()