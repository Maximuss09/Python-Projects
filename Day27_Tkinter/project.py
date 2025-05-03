from tkinter import *

window = Tk()
window.title("Mile to Km Convert")
window.minsize(width=350, height=150)
window.config(padx=20, pady=20)


"""-------INPUT---------"""
input = Entry(width=10)
print(input.get())

input.grid(column=1, row=0) 


"""-------LABELS---------"""
#MILES
Lable_miles = Label(text="Miles", font=("Arial", 20))
Lable_miles.grid(column=2, row=0)

#EQUAL TO
label_equal_to = Label(text= "is equal to: ", font= ("Arial", 18))
label_equal_to.grid(column=0, row=1)

#KM
label_km =  Label(text= "Km ", font= ("Arial", 18))
label_km.grid(column=2, row=1)


"""-------OUTPUT---------"""

lable_converted = Label(text= "0")
lable_converted.grid(column=1, row=1)


"""-------BUTTON---------"""

def button_convert ():
    print("working")
    number_to_convert = float(input.get())
    converted_num = number_to_convert*1.609
    lable_converted.config(text= f"{converted_num:.3f}") 

button = Button(text="Calculate", command=button_convert)
button.grid(column=1, row=2)





window.mainloop()