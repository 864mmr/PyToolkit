# Universal Unit Convertor

from tkinter import Tk, Menu, StringVar, DoubleVar, Label, Button, Entry
from tkinter.ttk import Combobox

# Conversion dictionary (Units based on Google's Unit Convertor)
# Format: {"Unit Type" : {"Unit" : [func, inverse of func], "Unit" : [...]}}
# One of the units is a "pivot" (in each group). Thus, "Pivotal Unit" : [identity func, identity func]
cdict = {
    "Length": {
        "Metres": [lambda x: x, lambda x: x], # Metre is a pivot, for  example
        "Yards": [lambda x: 1.09361 * x, lambda x: x / 1.09361],
        "Feet": [lambda x: 3.28084 * x, lambda x: x / 3.28084],
        "Centimetres": [lambda x: 100 * x, lambda x: x / 100],
        "Kilometres": [lambda x: x / 1000, lambda x: x * 1000],
        "Miles": [lambda x: x / 1609.34, lambda x: x * 1609.34]
    },
    
    "Temperature": {
        "Degree Celsius": [lambda x: x, lambda x: x],
        "Degree Fahrenheit": [lambda x: 1.8 * x + 32, lambda x: (x - 32) / 1.8],
        "Kelvin": [lambda x: x + 273.15, lambda x: x - 273.15],
    },

    "Area": {
        "Square Metres": [lambda x: x, lambda x: x],
        "Square Kilometres": [lambda x: x / (10**6), lambda x: x * (10**6)],
        "Square Miles": [lambda x: x / (2.59*(10**6)), lambda x: x * (2.59*(10**6))],
        "Acres": [lambda x: x / 4046.86, lambda x: x * 4046.86]
    },

    "Mass": {
        "Kilograms": [lambda x: x, lambda x: x],
        "Tonnes": [lambda x: x / 1000, lambda x: x * 1000],
        "Pounds": [lambda x: x * 2.20462, lambda x: x / 2.20462],
        "Grams": [lambda x: x * 1000, lambda x: x / 1000]
    },

    "Time" : {
        "Seconds": [lambda x: x, lambda x: x],
        "Minutes": [lambda x: x / 60, lambda x: x * 60],
        "Hours": [lambda x: x / 3600, lambda x: x * 3600],
        "Days": [lambda x: x / 86400, lambda x: x * 86400],
        "Weeks": [lambda x: x / 604800, lambda x: x * 604800],
        "Months": [lambda x: x/(2.62*(10**6)), lambda x: x * (2.62*(10**6))],
        "Years": [lambda x: x/(3.154*(10**7)), lambda x: x * (3.154*(10**7))]
    },

    "Speed" : {
        "Metres/Second" : [lambda x: x, lambda x: x],
        "Kilometres/Hour" : [lambda x: x * 3.6, lambda x: x / 3.6],
        "Miles/Hour" : [lambda x: x * 2.23694, lambda x: x / 2.23694],
        "Foot/Second" : [lambda x: x * 3.28084, lambda x: x / 3.28084],
        "Knot" : [lambda x: x * 1.94384, lambda x: x / 1.94384]
    }
}

# GUI Elements
def setUnitCb(*args):
    cbUnitFrom['values'] = tuple(cdict[quantVar.get()].keys())
    cbUnitTo['values'] = tuple(cdict[quantVar.get()].keys())

root = Tk()
root.resizable(width=False, height=False)
root.title("Universal Unit Convertor")
defaultFont = ("Segoe UI Light", 16)

# Text labels
Label(root, text="Quantity Type:", font = defaultFont).grid(row=0, column=0)
Label(root, text="Convert:", font = defaultFont).grid(row=1, column=0, sticky = 'w')
Label(root, text="  to  ", font = defaultFont).grid(row=1, column=3)
Label(root, text="    ").grid(row=1, column=6)

# Quantity Section
quantVar = StringVar()
cbQuantity = Combobox(root, textvariable = quantVar, state="readonly", values=[x for x in cdict.keys()],
                      font = defaultFont, width = 25)
cbQuantity.bind("<<ComboboxSelected>>", setUnitCb) # Binds Convert and To Fields upon quantity selected
cbQuantity.grid(row=0, column=1)

# Value Entry
val = DoubleVar()
Entry(root, textvariable = val, width = 26, font = defaultFont).grid(row=1, column=1)

# From Field
fromVar = StringVar()
cbUnitFrom = Combobox(root, textvariable = fromVar, state="readonly", font = defaultFont)
cbUnitFrom.grid(row=1, column=2)

# To Field
toVar = StringVar()
cbUnitTo = Combobox(root, textvariable = toVar, state="readonly", font = defaultFont)
cbUnitTo.grid(row=1, column=4, columnspan = 2)
    
# Calculate Button and function
def calc(*args):
    # Converts fromVar Unit to Pivot Unit and then to desired toVar Unit
    try:
        result = cdict[quantVar.get()][toVar.get()][0](cdict[quantVar.get()][fromVar.get()][1](val.get()))
        resultVar.set("{} {} {} {}".format("{0:.10f}".format(val.get()), fromVar.get(),
                                           "= {0:.10f}".format(result), toVar.get()))
    except:
        resultVar.set("Error: invalid field input")
    
Button(root, text="Calculate", command = calc, width = 15, height = 1,
       font = defaultFont).grid(row=2, columnspan = 8)

# Swap Button and function
def swap(*args):
    global fromVar; global toVar
    toVar, fromVar = fromVar, toVar
    cbUnitTo['textvariable'] = toVar
    cbUnitFrom['textvariable'] = fromVar
    
Button(root, text="Swap", command = swap, width = 8, height = 1,
       font = defaultFont).grid(row=1, column=7)
    
# Result Display
resultVar = StringVar()
resultLabel = Label(root, textvariable = resultVar, height = 2,
                    font = defaultFont).grid(row=3, column = 0, columnspan = 8)

# Menu Bar
menubar = Menu(root)
menubar.add_cascade(label = "Exit", command = root.destroy)
root.config(menu = menubar)

root.mainloop()
