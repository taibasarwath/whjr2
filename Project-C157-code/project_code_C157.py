from tkinter import *
from PIL import ImageTk, Image
import random
root=Tk()
root.title("Endless Pokemon Game")

root.geometry("800x600")
root.configure(background="orange")

img=ImageTk.PhotoImage(Image.open ("button.jpg"))

pikachu =ImageTk.PhotoImage(Image.open ("pikachu.jpg"))
bulbasour =ImageTk.PhotoImage(Image.open ("bulbasour.jpg"))
Charmender =ImageTk.PhotoImage(Image.open ("charmender.jpg"))
Squirtle =ImageTk.PhotoImage(Image.open ("squirtle.jpg"))
Ratata =ImageTk.PhotoImage(Image.open ("ratata.jpg"))
nidoking =ImageTk.PhotoImage(Image.open ("nidoking.jpg"))
jigglypuff =ImageTk.PhotoImage(Image.open ("jigglypuff.jpg"))
meowth =ImageTk.PhotoImage(Image.open ("meowth.jpg"))
Persion =ImageTk.PhotoImage(Image.open ("persion.jpg"))
abra =ImageTk.PhotoImage(Image.open ("abra.jpg"))
kadabra =ImageTk.PhotoImage(Image.open ("kadabra.jpg"))
Iyvasour =ImageTk.PhotoImage(Image.open ("Iyvasour.jpg"))

player1 = Label(root, text = "Player 1", bg = "red", fg = "white")
player1.place(relx = 0.1, rely = 0.3 , anchor =  CENTER)

player2 = Label(root, text = "Player 2", bg = "red", fg = "white")
player2.place(relx = 0.9, rely = 0.3 , anchor =  CENTER)

player_1_score_label = Label(root , bg = "royal blue", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4 , anchor =  CENTER)

player_2_score_label = Label(root , bg = "royal blue", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4 , anchor =  CENTER)


pokemon_list = [pikachu,bulbasour,Iyvasour,Charmender,Squirtle,Ratata,jigglypuff,meowth,Persion,abra ,
                kadabra]
power_list = [200,60,100,50,50,40,70,60,70,30,70]

label = Label(root)
label.place(relx = 0.5, rely = 0.5 , anchor =  CENTER)

player1_score = 0
def player1():
    global player1_score
    random_no = random.randint(0,10)
    random_pokemon = pokemon_list[random_no]
    label["image"]=random_pokemon
    
    random_power_list = power_list[random_no]
    player1_score = player1_score + random_power_list
    player_1_score_label["text"] = str( player1_score)

player_1_btn = Button(root, image = img, command = player1)
player_1_btn.place(relx = 0.1, rely = 0.6 , anchor =  CENTER)
    
player2_score = 0
def player2():
    global player2_score
    random_no2 = random.randint(0,10)
    random_pokemon2 = pokemon_list[random_no2]
    label["image"]=random_pokemon2
    
    random_power_list2 = power_list[random_no2]
    player2_score = player2_score + random_power_list2 
    player_2_score_label["text"] = str( player2_score)

player_2_btn = Button(root, image = img, command = player2)
player_2_btn.place(relx = 0.9, rely = 0.6 , anchor =  CENTER)

root.mainloop()