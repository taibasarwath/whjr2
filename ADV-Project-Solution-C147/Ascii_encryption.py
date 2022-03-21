from tkinter import *
#Uncomment the following line if you have MacOS
#Ask the student to write the following line if the student has MacOS
#from tkmacosx import *

root=Tk()
root.title("Encryption with Ascii Code")

root.geometry("400x400")
root.configure(background = 'lightblue1')

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label = Label(root, text = "Name in Ascii : ", bg="light cyan", fg="black")
label2 = Label(root, text = "Encrypted Name :", bg="light cyan", fg="black")

def asciiConverter():
    input_word = str(enter_word.get())
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + "  "
        ascii = int(ord(letter))
        encrypted = ascii - 1
        label2["text"] += str(chr(encrypted))
        

            
btn=Button(root,text="Display the Ascii Code and Encrypted value",command=asciiConverter, bg='royalblue', fg = 'white')
btn.place(relx=0.5,rely=0.5,anchor=CENTER)


label.place(relx=0.5,rely=0.6,anchor=CENTER)
label2.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()
