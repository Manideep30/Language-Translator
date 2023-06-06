from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES


root=Tk()
root.title('Language Translator by Manideep')
root.geometry('800x400')

def show():
    v1=combo_first.get()
    v2=combo_second.get()
    first_lan.config(text=v1)
    second_lan.config(text=v2)
    root.after(1000,show)

def translate():
    trans=Translator()
    trans_lang=trans.translate(input_text.get(1.0,END),src=combo_first.get(),dest=combo_second.get())

    output_text.delete(1.0,END)
    output_text.insert(END,trans_lang.text)


def clear():
    output_text.delete(1.0,END)
    input_text.delete(1.0,END)


def exit():
    root.destroy()


bg_img=PhotoImage(file=r'C:\Users\lenovo\OneDrive\Desktop\background.png')

lab=Label(root,image=bg_img)
lab.pack()

convert_img=PhotoImage(file=r'C:\Users\lenovo\OneDrive\Desktop\convert.png')
close_img=PhotoImage(file=r'C:\Users\lenovo\OneDrive\Desktop\close.png')
exit_img=PhotoImage(file=r'C:\Users\lenovo\OneDrive\Desktop\exit.png')


first_lan=Label(root,text='English',font=('Engraves','30','bold'),fg='#5582f9',bg='white')
first_lan.place(x=90,y=50)

second_lan=Label(root,text='Hindi',font=('Engraves','30','bold'),fg='#5582f9',bg='white')
second_lan.place(x=550,y=50)

language=list(LANGUAGES.values())

combo_first=ttk.Combobox(root,values=language)
combo_first.place(x=90,y=105)
combo_first.set('English')

combo_second=ttk.Combobox(root,values=language)
combo_second.place(x=520,y=105)
combo_second.set('Telugu')

input_text=Text(root,height=3,width=20)
input_text.place(x=90,y=125)

output_text=Text(root,height=3,width=20)
output_text.place(x=520,y=125)

convert=Button(root,text='Convert',image=convert_img,command=translate)
convert.place(x=90,y=300)

clear=Button(root,text='Close',image=close_img,command=clear)
clear.place(x=350,y=300)

exit=Button(root,text='exit',image=exit_img,command=exit)
exit.place(x=600,y=300)


show()
mainloop()

