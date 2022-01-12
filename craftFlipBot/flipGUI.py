#import flipBot as fP
import tkinter as tk
from tkinter import messagebox
import json, os
os.chdir('/Users/jpollack/Desktop/CodingFiles/craftFlipBot')
pricesFile = open('priceData.json', 'r')
prices = json.load(pricesFile)
pricesFile.close()
recipeFile = open('recipeData.json', 'r')
recipes = json.load(recipeFile)
recipeFile.close()

print(len(prices.keys()))
def printItem(item, type):
    if type == 'price':
        tk.messagebox.showinfo('Price', byPrice[item][0]+'\n'+str(byPrice[item][1]))
        print(recipes[byPrice[item][0]])
        for i in recipes[byPrice[item][0]].values():
            if i.split(':')[0] in prices:
                print(prices[i.split(':')[0]])
    elif type == 'percent':
        tk.messagebox.showinfo('Percent', byPercent[item][0]+'\n'+str(byPercent[item][1]))
        print(recipes[byPercent[item][0]])
        for i in recipes[byPercent[item][0]].values():
            if i.split(':')[0] in prices:
                print(prices[i.split(':')[0]])
    elif type == 'margin':
        tk.messagebox.showinfo('Margin', byMargin[item][0]+'\n'+str(byMargin[item][1]))
        print(recipes[byMargin[item][0]])
        for i in recipes[byMargin[item][0]].values():
            if i.split(':')[0] in prices:
                print(prices[i.split(':')[0]])

byPrice = sorted(prices.items(), key = lambda x: x[1]['cost'], reverse=True)
byPercent = sorted(prices.items(), key = lambda x: x[1]['priceMarginPercent'], reverse=True)
byMargin = sorted(prices.items(), key = lambda x: x[1]['priceMarginFlat'], reverse=True)

window = tk.Tk()

priceButtons = []
percentButtons = []
marginButtons = []
tk.Label(text='Price').grid(row=0, column=0, sticky=tk.EW)
tk.Label(text='Profit%').grid(row=0, column=1, sticky=tk.EW)
tk.Label(text='Profit').grid(row=0, column=2, sticky=tk.EW)
for i in range(10):
    priceButtons.append(tk.Button(text=byPrice[i][0], command=lambda:printItem(i, "price")))
    priceButtons[i].grid(row=i+1, column=0)
    percentButtons.append(tk.Button(text=byPercent[i][0], command=lambda:printItem(i, "percent")))
    percentButtons[i].grid(row=i+1, column=1)
    marginButtons.append(tk.Button(text=byMargin[i][0], command=lambda:printItem(i, "margin")))
    marginButtons[i].grid(row=i+1, column=2)
priceButtons[0].config(command=lambda:printItem(0, "price"))
priceButtons[1].config(command=lambda:printItem(1, "price"))
priceButtons[2].config(command=lambda:printItem(2, "price"))
priceButtons[3].config(command=lambda:printItem(3, "price"))
priceButtons[4].config(command=lambda:printItem(4, "price"))
priceButtons[5].config(command=lambda:printItem(5, "price"))
priceButtons[6].config(command=lambda:printItem(6, "price"))
priceButtons[7].config(command=lambda:printItem(7, "price"))
priceButtons[8].config(command=lambda:printItem(8, "price"))
priceButtons[9].config(command=lambda:printItem(9, "price"))
percentButtons[0].config(command=lambda:printItem(0, "percent"))
percentButtons[1].config(command=lambda:printItem(1, "percent"))
percentButtons[2].config(command=lambda:printItem(2, "percent"))
percentButtons[3].config(command=lambda:printItem(3, "percent"))
percentButtons[4].config(command=lambda:printItem(4, "percent"))
percentButtons[5].config(command=lambda:printItem(5, "percent"))
percentButtons[6].config(command=lambda:printItem(6, "percent"))
percentButtons[7].config(command=lambda:printItem(7, "percent"))
percentButtons[8].config(command=lambda:printItem(8, "percent"))
percentButtons[9].config(command=lambda:printItem(9, "percent"))
marginButtons[0].config(command=lambda:printItem(0, "margin"))
marginButtons[1].config(command=lambda:printItem(1, "margin"))
marginButtons[2].config(command=lambda:printItem(2, "margin"))
marginButtons[3].config(command=lambda:printItem(3, "margin"))
marginButtons[4].config(command=lambda:printItem(4, "margin"))
marginButtons[5].config(command=lambda:printItem(5, "margin"))
marginButtons[6].config(command=lambda:printItem(6, "margin"))
marginButtons[7].config(command=lambda:printItem(7, "margin"))
marginButtons[8].config(command=lambda:printItem(8, "margin"))
marginButtons[9].config(command=lambda:printItem(9, "margin"))
window.mainloop()
