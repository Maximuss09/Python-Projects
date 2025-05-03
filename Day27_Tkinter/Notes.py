from tkinter import *

window = Tk()
window.title("The Impresive GUI Program")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)
 
"""----------Label----------"""
the_label = Label(text="I'm the Label", font=("Arial", 24, "bold"))
the_label["text"] = "I'm the Label"
#the_label.config(text="new Label") ""OTHER OPTION""

the_label.pack()
# the_label.place(x=0, y=0)
# the_label.grid(column=0, row=0)



"""-------------BUTTON-----------"""

def button_clicked ():
    print("I got clicked")
    new_text = input.get()
    the_label.config(text=new_text)

button = Button(text="Click on Me", command=button_clicked)

button.pack()
# button.grid(column=1, row=1)



"""---------------ENTRY------------"""

input = Entry(width=15)
print(input.get())

input.pack()
# input.grid(column=4, row=3) 

"""-------------NEW BUTTON-----------"""

# def New_button_clicked ():
#     print("I got clicked")
#     new_text = input.get()
#     the_label.config(text=new_text)

# button = Button(text="I'm the New B", command=New_button_clicked)
# button.grid(column=2, row=0)






window.mainloop()
