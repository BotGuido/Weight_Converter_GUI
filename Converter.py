from tkinter import *
# Creating a GUI Window
window = Tk()
''' 
Next, we will be defining a function for the conversion process. 
Weight conversion means to multiply the value of a unit with 
the standard conversion value, so we will multiply it with the corresponding values.

Далее мы определим функцию для процесса преобразования.
Преобразование веса означает умножение веса единицы на
стандартное значение конверсии, поэтому мы умножим его на соответствующие значения.
'''
def from_kg():
    gram = float(e2_value.get())*1000
    pound = float(e2_value.get())*2.20462
    ounce = float(e2_value.get())*35.274
    t1.delete("1.0",END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)
'''
In the next section, we start giving the labels of the text fields.

В следующем разделе мы начнем давать метки текстовым полям.
'''
e1 = Label(window, text="Input the weight in KG")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text="Gram")
e4 = Label(window, text="Pound")
e5 = Label(window, text="Ounce")
'''
In this section, we will create three text fields where the output value will be displayed.

В этом разделе мы создадим три текстовых поля, в которых будет отображаться выходное значение.
'''
t1 = Text(window, height=5, width=30)
t2 = Text(window, height=5, width=30)
t3 = Text(window, height=5, width=30)
'''
Now, we will create a button, on clicking this button we call the from_kg 
function and display the values to the above text fields.

Теперь мы создадим кнопку, при нажатии на которую мы вызовем функцию from_kg 
и отобразим значения в вышеуказанных текстовых полях.
'''
b1 = Button(window, text="Convert", command=from_kg)
'''
In the last section, we will start giving the corresponding grid values 
and create the rows and columns for a better GUI.

В последнем разделе мы начнем задавать соответствующие значения сетки
и создавать строки и столбцы для лучшего графического интерфейса.
'''
e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)

window.mainloop()