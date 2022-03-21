from tkinter import *

root = Tk()
root.title("Sales Application")
root.geometry("400x400")
root.configure(background = "yellow")

label_month = Label(root)
label_profit = Label(root)

label_max_profit = Label(root)
label_min_profit = Label(root)



month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)

label_month["text"] = "Months :" + str(month)
label_profit["text"] = "Profits :" +str(profits)

def maxProfit():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    max_profit_month = month[max_profit_index]
    label_max_profit['text'] = "Maximum profit of "+str(max_profit)+" was given in the month of "+str(max_profit_month)
def minProfit():
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    min_profit_month = month[min_profit_index]
    label_min_profit['text'] = "Minimum profit of "+str(min_profit)+" was given in the month of "+str(min_profit_month)

label_month.place(relx=0.5, rely=0.2, anchor=CENTER)
label_profit.place(relx=0.5, rely=0.3, anchor=CENTER)

btn_max = Button(root, text="Show Max Profiable Month", command=maxProfit, bg = "Royal blue", fg = "white")
btn_min = Button(root, text="Show Min Profiable Month", command=minProfit, bg = "Royal blue", fg = "white")

btn_max.place(relx=0.5, rely=0.4, anchor=CENTER)

label_max_profit.place(relx=0.5, rely=0.5, anchor=CENTER)

btn_min.place(relx=0.5, rely=0.6, anchor=CENTER)

label_min_profit.place(relx=0.5, rely=0.7, anchor=CENTER)


root.mainloop()