import tkinter
from tkinter import *
from tkinter.ttk import *
import speech_recognition as sr
import pyaudio
import time
import random



r = sr.Recognizer()

# ---------------------------------------------------------------------------------------------------------------------

Main_window = Tk()
Main_window.minsize(height=500, width=300)

background_image = PhotoImage(file="McDonalds1.png", master=Main_window)
background_label = Label(Main_window, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0, relwidth=1, relheight=1)


label = Label(Main_window)
button1 = Button(Main_window)
button2 = Button(Main_window)
button3 = Button(Main_window)
button4 = Button(Main_window)
buttonGoToCart = Button(Main_window)
buttonCancel = Button(Main_window)
labeltotal = Label(Main_window)

# ---------------------------------------------------------------------------------------------------------------------

Cheese_window = Tk()
Cheese_window.minsize(height=500, width=300)
Cheese_window.withdraw()

background_image1 = PhotoImage(file="McDonalds1.png", master=Cheese_window)
background_label1 = Label(Cheese_window, image=background_image1)
background_label1.image = background_image1
background_label1.place(x=0, y=0, relwidth=1, relheight=1)

label2 = Label(Cheese_window)
label3 = Label(Cheese_window)
labelAdded = Label(Cheese_window)
buttonAddtoCart = Button(Cheese_window)
buttonBack = Button(Cheese_window)

# ---------------------------------------------------------------------------------------------------------------------

Chicken_window = Tk()
Chicken_window.minsize(height=500, width=300)
Chicken_window.withdraw()

background_image2 = PhotoImage(file="McDonalds1.png", master=Chicken_window)
background_label2 = Label(Chicken_window, image=background_image2)
background_label2.image = background_image2
background_label2.place(x=0, y=0, relwidth=1, relheight=1)

label4 = Label(Chicken_window)
label5 = Label(Chicken_window)
labelAdded1 = Label(Chicken_window)
buttonAddtoCart1 = Button(Chicken_window)
buttonBack1 = Button(Chicken_window)

# ---------------------------------------------------------------------------------------------------------------------

BigMac_window = Tk()
BigMac_window.minsize(height=500, width=300)
BigMac_window.withdraw()

background_image3 = PhotoImage(file="McDonalds1.png", master=BigMac_window)
background_label3 = Label(BigMac_window, image=background_image3)
background_label3.image = background_image3
background_label3.place(x=0, y=0, relwidth=1, relheight=1)

label6 = Label(BigMac_window)
label7 = Label(BigMac_window)
labelAdded2 = Label(BigMac_window)
buttonAddtoCart2 = Button(BigMac_window)
buttonBack2 = Button(BigMac_window)

# ---------------------------------------------------------------------------------------------------------------------

MacRoyal_window = Tk()
MacRoyal_window.minsize(height=500, width=300)
MacRoyal_window.withdraw()

background_image4 = PhotoImage(file="McDonalds1.png", master=MacRoyal_window)
background_label4 = Label(MacRoyal_window, image=background_image4)
background_label4.image = background_image4
background_label4.place(x=0, y=0, relwidth=1, relheight=1)

label8 = Label(MacRoyal_window)
label9 = Label(MacRoyal_window)
labelAdded3 = Label(MacRoyal_window)
buttonAddtoCart3 = Button(MacRoyal_window)
buttonBack3 = Button(MacRoyal_window)

# ---------------------------------------------------------------------------------------------------------------------

To_Cart = Tk()
To_Cart.minsize(height=500, width=300)
To_Cart.withdraw()

background_image5 = PhotoImage(file="McDonalds1.png", master=To_Cart)
background_label5 = Label(To_Cart, image=background_image5)
background_label5.image = background_image5
background_label5.place(x=0, y=0, relwidth=1, relheight=1)

labelCartTotal = Label(To_Cart)
buttonCancelCart = Button(To_Cart)
butttonCheckout = Button(To_Cart)

cart1 = Label(To_Cart)
cart2 = Label(To_Cart)
cart3 = Label(To_Cart)
cart4 = Label(To_Cart)

# ---------------------------------------------------------------------------------------------------------------------

Cheackout_window = Tk()
Cheackout_window.minsize(height=500, width=300)
Cheackout_window.withdraw()

background_image6 = PhotoImage(file="McDonalds1.png", master=Cheackout_window)
background_label6 = Label(Cheackout_window, image=background_image6)
background_label6.image = background_image6
background_label6.place(x=0, y=0, relwidth=1, relheight=1) #for each item in order


class CheeseBurger:
    name = 'Cheese Burger'
    price = 420


class ChickenBurger:
    name = 'Chicken Burger'
    price = 420


class BigMacBurger:
    name = 'Big Mac Burger'
    price = 920


class MacRoyalBurger:
    name = 'Mac Royal Burger'
    price = 970


order = []

totals = []


def total(int):
    sum = 0
    totals.append(int)
    for x in totals:
        sum = sum + x

    return sum


def tabBack():
    Cheese_window.withdraw()
    Chicken_window.withdraw()
    BigMac_window.withdraw()
    MacRoyal_window.withdraw()
    Main_window.deiconify()
    tab1()


def addCheese():
    labelAdded.config(text=('Cheese burger added to cart -- ' + str(CheeseBurger.price) + 'ft' + ' -- Total is: ' + str(total(CheeseBurger.price)) + ' ft'))
    labelAdded.pack(side=BOTTOM)
    order.append(CheeseBurger)
    print(order)
    tabCheese()

    #Cheese_window.after(700, Speak())

def tabCheese():
    Main_window.withdraw()
    Cheese_window.deiconify()

    label2.config(text='Add Cheese burger to cart?')
    label2.pack()

    label3.config(text=(str(CheeseBurger.price) + ' ft'))
    label3.pack()

    labelAdded.config(text=('Cheese burger added to cart -- ' + str(CheeseBurger.price) + 'ft' + ' -- Total is: ' + str(total(0)) + ' ft'))
    labelAdded.pack(side=BOTTOM)

    buttonAddtoCart.config(text='Add cheese burger to cart', command=addCheese)
    buttonAddtoCart.pack()

    buttonBack.config(text='Go back', command=tabBack)
    buttonBack.pack()
    buttonexp = Button(Cheese_window, text='speak', command=Speak)

    Cheese_window.after(700, buttonexp.invoke)
    Cheese_window.mainloop()


def addChicken():
    labelAdded1.config(text=('Chicken burger added to cart -- ' + str(ChickenBurger.price) + 'ft' + ' -- Total is: ' + str(total(ChickenBurger.price)) + ' ft'))
    labelAdded1.pack(side=BOTTOM)
    order.append(ChickenBurger)
    print(order)
    tabChicken()

def tabChicken():
    Main_window.withdraw()
    Chicken_window.deiconify()

    label4.config(text='Add Chicken Burger to cart?')
    label4.pack()

    label5.config(text=(str(ChickenBurger.price) + ' ft'))
    label5.pack()

    labelAdded1.config(text=('Chicken burger added to cart -- ' + str(ChickenBurger.price) + 'ft' + ' -- Total is: ' + str(total(0)) + ' ft'))
    labelAdded1.pack(side=BOTTOM)

    buttonAddtoCart1.config(text='Add chicken burger to cart', command=addChicken)
    buttonAddtoCart1.pack()

    buttonBack1.config(text='Go back', command=tabBack)
    buttonBack1.pack()

    buttonexp = Button(Chicken_window, text='speak', command=Speak)

    Chicken_window.after(700, buttonexp.invoke)
    Chicken_window.mainloop()


def addBig():
    labelAdded2.config(text=('Big Mac burger added to cart -- ' + str(BigMacBurger.price) + 'ft' + ' -- Total is: ' + str(total(BigMacBurger.price)) + ' ft'))
    labelAdded2.pack(side=BOTTOM)
    order.append(BigMacBurger)
    print(order)
    tabBig()

def tabBig():
    Main_window.withdraw()
    BigMac_window.deiconify()

    label6.config(text='Add Big Mac burger to cart?')
    label6.pack()

    label7.config(text=(str(BigMacBurger.price) + ' ft'))
    label7.pack()

    labelAdded2.config(text=('Big Mac burger added to cart -- ' + str(BigMacBurger.price) + 'ft' + ' -- Total is: ' + str(total(0)) + ' ft'))
    labelAdded2.pack(side=BOTTOM)

    buttonAddtoCart2.config(text='Add big mac burger to cart', command=addBig)
    buttonAddtoCart2.pack()

    buttonBack2.config(text='Go back', command=tabBack)
    buttonBack2.pack()

    buttonexp = Button(BigMac_window, text='speak', command=Speak)

    BigMac_window.after(700, buttonexp.invoke)
    BigMac_window.mainloop()


def addRoyal():
    labelAdded3.config(text=('Mac Royal burger added to cart -- ' + str(MacRoyalBurger.price) + 'ft' + ' -- Total is: ' + str(total(MacRoyalBurger.price)) + ' ft'))
    labelAdded3.pack(side=BOTTOM)
    order.append(MacRoyalBurger)
    print(order)
    tabRoyal()

def tabRoyal():
    Main_window.withdraw()
    MacRoyal_window.deiconify()

    label8.config(text='Add Mac Royal burger to cart?')
    label8.pack()

    label9.config(text=(str(MacRoyalBurger.price) + ' ft'))
    label9.pack()

    labelAdded3.config(text=('Mac Royal burger added to cart -- ' + str(MacRoyalBurger.price) + 'ft' + ' -- Total is: ' + str(total(0)) + ' ft'))
    labelAdded3.pack(side=BOTTOM)

    buttonAddtoCart3.config(text='Add Mac Royal burger to cart', command=addRoyal)
    buttonAddtoCart3.pack()

    buttonBack3.config(text='Go back', command=tabBack)
    buttonBack3.pack()

    buttonexp = Button(MacRoyal_window, text='speak', command=Speak)

    MacRoyal_window.after(700, buttonexp.invoke)
    MacRoyal_window.mainloop()


def cancelCart():
    To_Cart.withdraw()
    Cheackout_window.withdraw()
    order.clear()
    totals.clear()
    Main_window.deiconify()
    print(order)
    tab1()

def checkoutOrder():
    To_Cart.withdraw()
    Cheackout_window.deiconify()

    total = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0

    for item in order:

        if (item == CheeseBurger):
            count1 = count1 + 1
        elif (item == ChickenBurger):
            count2 = count2 + 1
        elif (item == BigMacBurger):
            count3 = count3 + 1
        else:
            count4 = count4 + 1

        total = total + item.price
        print(item.name)

    Label200 = Label(Cheackout_window, text=('PAYMENT SUCCESSFUL'))
    Label200.pack()


    if (count1 != 0):
        Label10 = Label(Cheackout_window, text=(str(count1) + 'x ' + CheeseBurger.name + '------------------------------- ' + str(CheeseBurger.price) + ' ft'))
        Label10.pack()

    if (count2 != 0):
        Label20 = Label(Cheackout_window, text=(str(count2) + 'x ' + ChickenBurger.name + '------------------------------- ' + str(ChickenBurger.price) + ' ft'))
        Label20.pack()

    if (count3 != 0):
        Label30 = Label(Cheackout_window, text=(str(count3) + 'x ' + BigMacBurger.name + '------------------------------- ' + str(BigMacBurger.price) + ' ft'))
        Label30.pack()

    if (count4 != 0):
        Label30 = Label(Cheackout_window, text=(str(count4) + 'x ' + MacRoyalBurger.name + '------------------------------- ' + str(MacRoyalBurger.price) + ' ft'))
        Label30.pack()

    Label100 = Label(Cheackout_window,text=('YOUR ORDER NUMBER IS: '), font=("Arial", 10))
    Label100.pack()

    Label100 = Label(Cheackout_window, text=(str(random.randint(800,1000))), font=("Arial", 30))
    Label100.pack()

    print('Printing...............')


def tabCart():
    Main_window.withdraw()
    To_Cart.deiconify()

    cart1.config(text='')
    cart1.pack()
    cart2.config(text='')
    cart2.pack()
    cart3.config(text='')
    cart3.pack()
    cart4.config(text='')
    cart4.pack()

    total = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for item in order:

        if (item == CheeseBurger):
            count1 = count1 + 1
        elif (item == ChickenBurger):
            count2 = count2 + 1
        elif (item == BigMacBurger):
            count3 = count3 + 1
        else:
            count4 = count4 + 1

        total = total + item.price

    if (count1 != 0):
        cart1.config(text=(str(count1) + 'x ' + CheeseBurger.name + ': ' + str(CheeseBurger.price) + ' ft'))
        cart1.pack()

    if (count2 != 0):
        cart2.config(text=(str(count2) + 'x ' + ChickenBurger.name + ': ' + str(ChickenBurger.price) + ' ft'))
        cart2.pack()

    if (count3 != 0):
        cart3.config(text=(str(count3) + 'x ' + BigMacBurger.name + ': ' + str(BigMacBurger.price) + ' ft'))
        cart3.pack()

    if (count4 != 0):
        cart4.config(text=(str(count4) + 'x ' + MacRoyalBurger.name + ': ' + str(MacRoyalBurger.price) + ' ft'))
        cart4.pack()

    labelCartTotal.config(text=('Total: ' + str(total) + 'ft'))
    labelCartTotal.pack()

    buttonCancelCart.config(text='Cancel order', command=cancelCart)
    buttonCancelCart.pack()

    butttonCheckout.config(text='Checkout', command=checkoutOrder)
    butttonCheckout.pack()

    buttonexp = Button(To_Cart, text='speak', command=Speak)

    To_Cart.after(700, buttonexp.invoke)

    To_Cart.mainloop()

def close():
    Main_window.destroy()
    Cheese_window.destroy()
    Chicken_window.destroy()
    BigMac_window.destroy()
    MacRoyal_window.destroy()
    To_Cart.destroy()
    order.clear()
    print(order)

def tab1():
    label.config(text='Thank you for calling McBot')
    label.pack()

    button1.config(text='Cheese burger', command=tabCheese)
    button1.pack()

    button2.config(text='Chicken burger', command=tabChicken)
    button2.pack()

    button3.config(text='Big Mac', command=tabBig)
    button3.pack()

    button4.config(text='Mac Royal', command=tabRoyal)
    button4.pack()

    buttonGoToCart.config(text="Go to Cart", command=tabCart)
    buttonGoToCart.pack()

    buttonCancel.config( text='Cancel order', command=close)
    buttonCancel.pack()

    labeltotal.config(text=('TOTAL: ' + str(total(0)) + ' ft'))
    labeltotal.pack(side=BOTTOM)

    buttonexp = Button(Main_window, text='speak', command= Speak)

    Main_window.after(700, buttonexp.invoke)
    Main_window.mainloop()


    #Main_window.quit()
    #Main_window.deiconify()

#tab1()

def Speak():
    print('Listening...............')
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        text = str(r.recognize_google(audio, language="en-US")).lower()
        print(text)


        if (text == 'cheeseburger' or text == 'cheese burger'):
            tabCheese()
        elif (text == 'chickenburger' or text == 'chicken burger'):
            tabChicken()
        elif (text == 'big mac' or text == 'bigmacburger' or text == 'big mac burger'):
            tabBig()
        elif (text == 'mac royal burger' or text == 'mac royal'):
            tabRoyal()


        elif (text == 'back' or text == 'go back'):
            tabBack()


        elif (text == 'add cheeseburger' or text == 'add cheeseburger to cart' or text == 'add one more cheeseburger' or text == 'add another cheeseburger'):
            addCheese()
        elif (text == 'add chicken burger' or text == 'add chicken burger to cart' or text == 'add one more chicken burger' or text == 'add another chicken burger'):
            addChicken()
        elif (text == 'add big mac' or text == 'add big mac burger' or text == 'add big mac burger to cart'  or text == 'add big mac to cart' or text == 'add one more big mac'):
            addBig()
        elif (text == 'add mac royal' or text == 'add mac royal burger' or text == 'add mac royal burger to cart'  or text == 'add one more mac royal'):
            addRoyal()


        elif (text == 'go to cart'):
            tabCart()

        elif (text == 'checkout' or text == 'check out'):
            checkoutOrder()
        elif (text == 'cancel order' or text == 'restart' or text == 'cancel'):
            cancelCart()


        elif (text == 'close'):
            close()
        else:
            print('Sorry couldnt understand')
            Speak()

with sr.Microphone() as source:
    print('Listening...............')
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

    if (text == 'hello' or text == 'hey Mac' or text == 'haymac' or text == "hi Mac" or text == "Mac"):
        print('Hey there!')
        print('What would you like to order?')
        tab1()

