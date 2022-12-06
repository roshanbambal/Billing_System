# gui building management
from tkinter import *
import tkinter.messagebox
import datetime
import time
import random



# creating button click numbers functions
#def btnclick(numbers):
 #   global operator
 #   operator = operator + str(numbers) # count =count + 1
 #   text_input.set(operator)

# creating button clear function

#def btncleardisplay():
  #  global operator
  #  operator = " "
  #  text_input.set(operator)

# creating button for calculaion of the addition , sub , mul , div
#def btnequalinput():
 #   global operator
  #  sumup = str(eval(operator))
   # text_input.set(sumup)
    #operator = ' '

#creating by clicking it has to enable textbox
def chkitem1():
    if (var1.get()==1):
        txtitem1.configure(state=NORMAL)
        txtitem1.focus()
        txtitem1.delete(0,END)
        E_item1.set(' ')
    elif (var1.get()==0):
        txtitem1.configure(state=DISABLED)
        E_item1.set('0')

def chkitem8():
    if (var8.get()==1):
        txtitem8.configure(state=NORMAL)
        txtitem8.focus()
        txtitem8.delete(0,END)
        E_item8.set(' ')
    elif (var8.get()==0):
        txtitem8.configure(state=DISABLED)
        E_item8.set('0')


def chkitem2():
    if (var2.get() == 1):
        txtitem2.configure(state=NORMAL)
        txtitem2.focus()
        txtitem2.delete(0, END)
        E_item2.set(' ')
    elif (var2.get() == 0):
        txtitem2.configure(state=DISABLED)
        E_item2.set('0')


def chkitem3():
    if (var3.get() == 1):
        txtitem3.configure(state=NORMAL)
        txtitem3.focus()
        txtitem3.delete(0, END)
        E_item3.set(' ')
    elif (var3.get() == 0):
        txtitem3.configure(state=DISABLED)
        E_item3.set('0')


def chkitem4():
    if (var4.get() == 1):
        txtitem4.configure(state=NORMAL)
        txtitem4.focus()
        txtitem4.delete(0, END)
        E_item4.set(' ')
    elif (var4.get() == 0):
        txtitem4.configure(state=DISABLED)
        E_item4.set('0')


def chkitem5():
    if (var5.get() == 1):
        txtitem5.configure(state=NORMAL)
        txtitem5.focus()
        txtitem5.delete(0, END)
        E_item5.set(' ')
    elif (var5.get() == 0):
        txtitem5.configure(state=DISABLED)
        E_item5.set('0')


def chkitem6():
    if (var6.get() == 1):
        txtitem6.configure(state=NORMAL)
        txtitem6.focus()
        txtitem6.delete(0, END)
        E_item6.set(' ')
    elif (var6.get() == 0):
        txtitem6.configure(state=DISABLED)
        E_item6.set('0')


def chkitem7():
    if (var7.get() == 1):
        txtitem7.configure(state=NORMAL)
        txtitem7.focus()
        txtitem7.delete(0, END)
        E_item7.set(' ')
    elif (var7.get() == 0):
        txtitem7.configure(state=DISABLED)
        E_item7.set('0')


def chkitem9():
    if (var9.get() == 1):
        txtitem9.configure(state=NORMAL)
        txtitem9.focus()
        txtitem9.delete(0, END)
        E_item9.set(' ')
    elif (var9.get() == 0):
        txtitem9.configure(state=DISABLED)
        E_item9.set('0')


def chkitem10():
    if (var10.get() == 1):
        txtitem10.configure(state=NORMAL)
        txtitem10.focus()
        txtitem10.delete(0, END)
        E_item10.set(' ')
    elif (var10.get() == 0):
        txtitem10.configure(state=DISABLED)
        E_item10.set('0')


def chkitem11():
    if (var11.get() == 1):
        txtitem11.configure(state=NORMAL)
        txtitem11.focus()
        txtitem11.delete(0, END)
        E_item11.set(' ')
    elif (var11.get() == 0):
        txtitem11.configure(state=DISABLED)
        E_item11.set('0')


def chkitem13():
    if (var13.get() == 1):
        txtitem13.configure(state=NORMAL)
        txtitem13.focus()
        txtitem13.delete(0, END)
        E_item13.set(' ')
    elif (var13.get() == 0):
        txtitem13.configure(state=DISABLED)
        E_item13.set('0')


def chkitem14():
    if (var14.get() == 1):
        txtitem14.configure(state=NORMAL)
        txtitem14.focus()
        txtitem14.delete(0, END)
        E_item14.set(' ')
    elif (var14.get() == 0):
        txtitem14.configure(state=DISABLED)
        E_item14.set('0')


def chkitem15():
    if (var15.get() == 1):
        txtitem15.configure(state=NORMAL)
        txtitem15.focus()
        txtitem15.delete(0, END)
        E_item15.set(' ')
    elif (var15.get() == 0):
        txtitem15.configure(state=DISABLED)
        E_item15.set('0')


def chkitem16():
    if (var16.get() == 1):
        txtitem16.configure(state=NORMAL)
        txtitem16.focus()
        txtitem16.delete(0, END)
        E_item16.set(' ')
    elif (var16.get() == 0):
        txtitem16.configure(state=DISABLED)
        E_item16.set('0')


def chkitem12():
    if (var12.get() == 1):
        txtitem12.configure(state=NORMAL)
        txtitem12.focus()
        txtitem12.delete(0, END)
        E_item12.set(' ')
    elif (var12.get() == 0):
        txtitem12.configure(state=DISABLED)
        E_item12.set('0')
# creating exit button code
def iExit():
    iExit=tkinter.messagebox.askyesno('Exit billing management system','confirm if you want to exit...')
    if iExit >0:
        root.destroy()
        return
#===============================================
def CostofItem():
    Product1 = float(E_item1.get())
    Product2 = float(E_item2.get())
    Product3 = float(E_item3.get())
    Product4 = float(E_item4.get())
    Product5 = float(E_item5.get())
    Product6 = float(E_item6.get())
    Product7 = float(E_item7.get())
    Product8 = float(E_item8.get())

    Product9  = float(E_item9.get())
    Product10 = float(E_item10.get())
    Product11 = float(E_item11.get())
    Product12 = float(E_item12.get())
    Product13 = float(E_item13.get())
    Product14 = float(E_item14.get())
    Product15 = float(E_item15.get())
    Product16 = float(E_item16.get())

    #Calculation Of Atom Of category

    PriceofDrink = (Product1 * 1.5)+(Product2 * 2.5)+(Product3 * 3.5)+(Product4 * 4.5)+(Product5 * 5.5)+(Product6 * 6.5)+(Product7 * 7.5)+(Product8 * 8.5)
    PriceofCake = (Product9 * 9.5)+(Product10 * 10.5)+(Product11 * 11.5)+(Product12 * 12.5)+(Product13 * 13.5)+(Product14 * 14.5)+(Product15 * 15.5)+(Product16 * 16.5)

    DrinkPrice = '₹', str("%.2f" %(PriceofDrink))
    CakePrice = '₹', str("%.2f" %(PriceofCake))

    CostofCakes.set(CakePrice)
    CostOfDrinks.set(DrinkPrice)

    SC ='₹', str("%.2f" %(5.00))
    ServiceCharge.set(SC)

    SubtotalofItems = '₹',str("%.2f" %(PriceofCake + PriceofDrink + 5.00))
    Subtotal.set(SubtotalofItems)

    Tax = '₹', str("%.2f" %((PriceofCake + PriceofDrink + 5.00)*0.08))
    PaidTax.set(Tax)

    TT =((PriceofCake + PriceofDrink + 5.00)+0.08)

    TC = '₹',str("%.2f" %(PriceofDrink + PriceofCake + 5.00 + TT))
    TotalCost.set(TC)

def Reset():
    PaidTax.set("")
    Subtotal.set("")
    TotalCost.set("")
    CostofCakes.set("")
    CostOfDrinks.set("")
    ServiceCharge.set("")

    txtreceipt.delete("1.0",END)

    E_item1.set("0")
    E_item2.set("0")
    E_item3.set("0")
    E_item4.set("0")
    E_item5.set("0")
    E_item6.set("0")
    E_item7.set("0")
    E_item8.set("0")

    E_item9.set("0")
    E_item10.set("0")
    E_item11.set("0")
    E_item12.set("0")
    E_item13.set("0")
    E_item14.set("0")
    E_item15.set("0")
    E_item16.set("0")

    txtitem1.configure(state=DISABLED)
    txtitem2.configure(state=DISABLED)
    txtitem3.configure(state=DISABLED)
    txtitem4.configure(state=DISABLED)
    txtitem5.configure(state=DISABLED)
    txtitem6.configure(state=DISABLED)
    txtitem7.configure(state=DISABLED)
    txtitem8.configure(state=DISABLED)

    txtitem9.configure(state=DISABLED)
    txtitem10.configure(state=DISABLED)
    txtitem11.configure(state=DISABLED)
    txtitem12.configure(state=DISABLED)
    txtitem13.configure(state=DISABLED)
    txtitem14.configure(state=DISABLED)
    txtitem15.configure(state=DISABLED)
    txtitem16.configure(state=DISABLED)

    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")

    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")

def Recept():
    txtreceipt.delete('1.0',END)
    x = random.randint(2837, 500876) #EX 34857
    randomref = str(x)
    Recept_Ref.set("Bill Number:"+ randomref)

    txtreceipt.insert(END, "\t*** BLACKEY BILLING MANAGEMENT SYSYEM ***" '\n')
    txtreceipt.insert(END, "\t-------------------------------------------"'\n')
    txtreceipt.insert(END, "\t\t\t"+ Recept_Ref.get()+'\n')
    txtreceipt.insert(END, "\t\t\t Bill Date:" '\n')
    txtreceipt.insert(END, "\t--------------------------------------------------"'\n')

    txtreceipt.insert(END, "\t\t ITEMS:"+ "QUANTITY of Items" '\n')
    txtreceipt.insert(END, "\t\t Item1:"+ E_item1.get()+ '\n')
    txtreceipt.insert(END, "\t\t Item2:"+ E_item2.get()+ '\n')
    txtreceipt.insert(END, "\t\t Item3:"+ E_item3.get()+ '\n')
    txtreceipt.insert(END, "\t\t Item4:"+ E_item4.get()+ '\n')
    txtreceipt.insert(END, "\t\t Item5:"+ E_item5.get()+ '\n')
    txtreceipt.insert(END, "\t\t Item6:"+ E_item6.get()+ '\n')
    txtreceipt.insert(END, "\t\t Item7:"+ E_item7.get()+ '\n')
    txtreceipt.insert(END, "\t\t Item8:"+ E_item8.get()+ '\n')
    txtreceipt.insert(END, "\t\t Item9:"+ E_item9.get()+ '\n')
    txtreceipt.insert(END, "\t\t Item10:"+ E_item10.get()+ '\n')
    txtreceipt.insert(END, "\t\t Item11:"+ E_item11.get()+ '\n')
    txtreceipt.insert(END, "\t\t Item12:"+ E_item12.get()+ '\n')
    txtreceipt.insert(END, "\t\t Item13:"+ E_item13.get()+ '\n')
    txtreceipt.insert(END, "\t\t Item14:"+ E_item14.get()+ '\n')
    txtreceipt.insert(END, "\t\t Item15:"+ E_item15.get()+ '\n')
    txtreceipt.insert(END, "\t\t Item16:"+ E_item16.get()+ '\n')

    txtreceipt.insert(END, "\t-------------------------------------------"'\n')
    txtreceipt.insert(END, "\t\t Cost Of Drinks:" + CostOfDrinks.get() + '\n')
    txtreceipt.insert(END, "\t\t Cost Of Cakes:" + CostofCakes.get() + '\n')
    txtreceipt.insert(END, "\t\t Service Charge:" + ServiceCharge.get() + '\n')
    txtreceipt.insert(END, "\t\t Subtotal:" + Subtotal.get() + '\n')
    txtreceipt.insert(END, "\t\t pid Tax:" + PaidTax.get() + '\n')
    txtreceipt.insert(END, "\t\t Total Cost:" + TotalCost.get() + '\n')
    txtreceipt.insert(END, "\n\n\n\n")
    txtreceipt.insert(END, "\t----------------** THANK YOU COME AGAIN **-----------------"'\n')




#===========================================================

# cretaing the window
root = Tk() # creating the window
root.title("billing management system") # creating window tittle at the top left side
root.geometry('1350x750')#creating and fixing the window size
root.config(background='azure') # window bg colour

#================================================================================
# Creating Variable to string variable of recept detail
CostofCakes = StringVar()
CostOfDrinks= StringVar()
ServiceCharge = StringVar()
PaidTax = StringVar()
Subtotal = StringVar()
TotalCost = StringVar()
DateofOrder = StringVar()
Recept_Ref = StringVar()



# creating top title frame : project title on top
tops =Frame(root,bg='cadet blue',bd=10,pady=5,relief=RIDGE)  # RIDGE, RAISED,FLAT,SUNKEN,GROOVE
tops.pack(side=TOP)

# adding title in the project in the tops frame
lbltitle=Label(tops,text="ALPHA Management system",bd=5,bg='cadet blue',font=('arial',30,'bold'),justify=CENTER,fg='black')
lbltitle.grid(row=0,column=0)

#creating receipt frame window in the right side
receipt_cal_f=Frame(root,bg='powder blue',bd=10,relief=RIDGE)
receipt_cal_f.pack(side=RIGHT)

#creating button frame in the window in the bottom right side(right main frame)
buttons_f =Frame(receipt_cal_f,bg='powder blue',bd=3,relief=RIDGE)
buttons_f.pack(side=BOTTOM)
# creating calculator frame in the window at the right side

cal_f=Frame(receipt_cal_f,bg='powder blue',bd=3,relief=RIDGE)
cal_f.pack(side=TOP)

# creating receipt frame at the right side
receipt_f=Frame(receipt_cal_f,bg='powder blue',bd=3,relief=RIDGE)
receipt_f.pack(side=BOTTOM)

# creating menu frame at left side (left side main menu)
menuframe=Frame(root,bg='powder blue',bd=5,relief=RIDGE)
menuframe.pack(side=LEFT)

# creating cost frame in the menu frame
cost_f=Frame(menuframe,bg='powder blue',bd=5,relief=RIDGE)
cost_f.pack(side=BOTTOM)

# creating drinks frame in menu frame
drinks_f=Frame(menuframe,bg='cadet blue',bd=5)
drinks_f.pack(side=TOP)

drinks_f=Frame(menuframe,bg='cadet blue',bd=5,relief=RIDGE)
drinks_f.pack(side=LEFT)

# creating cakes frame in menu frame
cakes_f=Frame(menuframe,bg='cadet blue',bd=5,relief=RIDGE)
cakes_f.pack(side=RIGHT)

# converting variables into INTVAR() of items:cat1
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()

var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

#creating set default value to the values to the set method

E_item1=StringVar()
E_item1.set('0')

E_item2=StringVar()
E_item2.set('0')

E_item3=StringVar()
E_item3.set('0')

E_item4=StringVar()
E_item4.set('0')

E_item5=StringVar()
E_item5.set('0')

E_item6=StringVar()
E_item6.set('0')

E_item7=StringVar()
E_item7.set('0')

E_item8=StringVar()
E_item8.set('0')

E_item9=StringVar()
E_item9.set('0')

E_item10=StringVar()
E_item10.set('0')

E_item11=StringVar()
E_item11.set('0')

E_item12=StringVar()
E_item12.set('0')

E_item13=StringVar()
E_item13.set('0')

E_item14=StringVar()
E_item14.set('0')

E_item15=StringVar()
E_item15.set('0')

E_item16=StringVar()
E_item16.set('0')

# crrating check box for drinking items (category 1)
item1=Checkbutton(drinks_f,variable=var1,text='Item 1',font=('arial',18,'bold'),bg='powder blue',onvalue=1, offvalue=0,command=chkitem1). grid(row=0,sticky=W)
item2=Checkbutton(drinks_f,variable=var2,text='Item 2',font=('arial',18,'bold'),bg='powder blue' ,onvalue=1, offvalue=0,command=chkitem2). grid(row=1,sticky=W)
item3=Checkbutton(drinks_f,variable=var3,text='Item 3',font=('arial',18,'bold'),bg='powder blue',onvalue=1, offvalue=0,command=chkitem3). grid(row=2,sticky=W)
item4=Checkbutton(drinks_f,variable=var4,text='Item 4',font=('arial',18,'bold'),bg='powder blue',onvalue=1, offvalue=0,command=chkitem4). grid(row=3,sticky=W)
item5=Checkbutton(drinks_f,variable=var5,text='Item 5',font=('arial',18,'bold'),bg='powder blue',onvalue=1, offvalue=0,command=chkitem4). grid(row=4,sticky=W)
item6=Checkbutton(drinks_f,variable=var6,text='Item 6',font=('arial',18,'bold'),bg='powder blue',onvalue=1, offvalue=0,command=chkitem6). grid(row=5,sticky=W)
item7=Checkbutton(drinks_f,variable=var7,text='Item 7',font=('arial',18,'bold'),bg='powder blue',onvalue=1, offvalue=0,command=chkitem7). grid(row=6,sticky=W)
item8=Checkbutton(drinks_f,variable=var8,text='Item 8',font=('arial',18,'bold'),bg='powder blue',onvalue=1, offvalue=0,command=chkitem8). grid(row=7,sticky=W)

# creating text boxes for drinking items at check boxes

txtitem1=(Entry(drinks_f,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_item1))
txtitem1.grid(row=0,column=1)
txtitem2=Entry(drinks_f,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_item2)
txtitem2.grid(row=1,column=1)
txtitem3=Entry(drinks_f,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_item3)
txtitem3.grid(row=2,column=1)
txtitem4=Entry(drinks_f,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_item4)
txtitem4.grid(row=3,column=1)
txtitem5=Entry(drinks_f,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_item5)
txtitem5.grid(row=4,column=1)
txtitem6=Entry(drinks_f,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_item6)
txtitem6.grid(row=5,column=1)
txtitem7=Entry(drinks_f,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_item7)
txtitem7.grid(row=6,column=1)
txtitem8=Entry(drinks_f,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_item8)
txtitem8.grid(row=7,column=1)

# creating food items check boxes(category 2)
item9=Checkbutton(cakes_f,variable=var9,text='Item 9',font=('arial',18,'bold'),bg='powder blue',onvalue=1, offvalue=0,command=chkitem9). grid(row=0,sticky=W)
item10=Checkbutton(cakes_f,variable=var10,text='Item 10',font=('arial',18,'bold'),bg='powder blue',onvalue=1, offvalue=0,command=chkitem10). grid(row=1,sticky=W)
item11=Checkbutton(cakes_f,variable=var11,text='Item 11',font=('arial',18,'bold'),bg='powder blue',onvalue=1, offvalue=0,command=chkitem11). grid(row=2,sticky=W)
item12=Checkbutton(cakes_f,variable=var12,text='Item 12',font=('arial',18,'bold'),bg='powder blue',onvalue=1, offvalue=0,command=chkitem12). grid(row=3,sticky=W)
item13=Checkbutton(cakes_f,variable=var13,text='Item 13',font=('arial',18,'bold'),bg='powder blue',onvalue=1, offvalue=0,command=chkitem13). grid(row=4,sticky=W)
item14=Checkbutton(cakes_f,variable=var14,text='Item 14',font=('arial',18,'bold'),bg='powder blue',onvalue=1, offvalue=0,command=chkitem14). grid(row=5,sticky=W)
item15=Checkbutton(cakes_f,variable=var15,text='Item 15',font=('arial',18,'bold'),bg='powder blue',onvalue=1, offvalue=0,command=chkitem15). grid(row=6,sticky=W)
item16=Checkbutton(cakes_f,variable=var16,text='Item 16',font=('arial',18,'bold'),bg='powder blue',onvalue=1, offvalue=0,command=chkitem16). grid(row=7,sticky=W)

# creating textbox for food items @ checkbox cat 2
txtitem9=(Entry(cakes_f,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_item9))
txtitem9.grid(row=0,column=1)
txtitem10=Entry(cakes_f,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_item10)
txtitem10.grid(row=1,column=1)
txtitem11=Entry(cakes_f,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_item11)
txtitem11.grid(row=2,column=1)
txtitem12=Entry(cakes_f,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_item12)
txtitem12.grid(row=3,column=1)
txtitem13=Entry(cakes_f,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_item13)
txtitem13.grid(row=4,column=1)
txtitem14=Entry(cakes_f,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_item14)
txtitem14.grid(row=5,column=1)
txtitem15=Entry(cakes_f,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_item15)
txtitem15.grid(row=6,column=1)
txtitem16=Entry(cakes_f,font=('arial',16,'bold'),bd=8,width=6,justify='left',state=DISABLED,textvariable=E_item16)
txtitem16.grid(row=7,column=1)

# creating drinks frame in the menu frame
lblcostofdrinks = Label(cost_f,text='cost of drinks',bg='powder Blue',font=('arial',14,'bold'),fg='black')
lblcostofdrinks.grid(row=0, column=0, sticky=W)
txtcostofdrinks = Entry(cost_f,font=('arial',14,'bold'),bd=6, bg='white',insertwidth=2,justify=RIGHT, textvariable=CostOfDrinks)
txtcostofdrinks.grid(row=0,column=1)
# creating cakes frame in the menu frame
lblcostofcakes = Label(cost_f,text='cost of cakes',bg='powder Blue',font=('arial',14,'bold'),fg='black')
lblcostofcakes.grid(row=1, column=0, sticky=W)
txtcostofcakes = Entry(cost_f,font=('arial',14,'bold'),bd=6, bg='white',insertwidth=2,justify=RIGHT, textvariable=CostofCakes)
txtcostofcakes.grid(row=1,column=1)
# creating charges frame in the menu frame
lblservicecharges = Label(cost_f,text='service charges',bg='powder Blue',font=('arial',14,'bold'),fg='black')
lblservicecharges.grid(row=2, column=0, sticky=W)
txtservicecharges = Entry(cost_f,font=('arial',14,'bold'),bd=6, bg='white',insertwidth=2,justify=RIGHT, textvariable=ServiceCharge)
txtservicecharges.grid(row=2,column=1)

lblpaidtax = Label(cost_f,text='paid tax',bg='powder Blue',font=('arial',14,'bold'),fg='black')
lblpaidtax.grid(row=0, column=2, sticky=W)
txtpaidtax = Entry(cost_f,font=('arial',14,'bold'),bd=6, bg='white',insertwidth=2,justify=RIGHT, textvariable=PaidTax)
txtpaidtax.grid(row=0,column=3)

lblsubtotal = Label(cost_f,text='sub total',bg='powder Blue',font=('arial',14,'bold'),fg='black')
lblsubtotal.grid(row=1, column=2, sticky=W)
txtsubtotal = Entry(cost_f,font=('arial',14,'bold'),bd=6, bg='white',insertwidth=2,justify=RIGHT, textvariable=Subtotal)
txtsubtotal.grid(row=1,column=3)

lbltotal = Label(cost_f,text='Total Cost',bg='powder Blue',font=('arial',14,'bold'),fg='black')
lbltotal.grid(row=2, column=2, sticky=W)
txttotalcost = Entry(cost_f,font=('arial',14,'bold'),bd=6, bg='white',insertwidth=2,justify=RIGHT, textvariable=TotalCost)
txttotalcost.grid(row=2,column=3)

# creating receipt box
txtreceipt =Text(receipt_f,width=60,height=12,bd=4,font=('arial',12,'bold'))
txtreceipt.grid(row=0,column=0)

# creating main buttons
btntotal=Button(buttons_f, padx=16,fg='black',font=('arial',16,'bold'),width=4,text='total', command=CostofItem)
btntotal.grid(row=0,column=0)

# creating main buttons
btnreceipt=Button(buttons_f, padx=16,fg='black',font=('arial',16,'bold'),width=4,text='Receipt', command=Recept)
btnreceipt.grid(row=0,column=1)

btnreset=Button(buttons_f, padx=16,fg='black',font=('arial',16,'bold'),width=4,text='Reset', command=Reset)
btnreset.grid(row=0,column=2)

btnexit=Button(buttons_f, padx=16,fg='black',font=('arial',16,'bold'),width=4,text='exit',command=iExit)
btnexit.grid(row=0,column=3)

btnprint=Button(buttons_f, padx=16,fg='black',font=('arial',16,'bold'),width=4,text='print')
btnprint.grid(row=0,column=4)



# creating calculator display
txtdisplay=Entry(cal_f,width=45,bg='white',bd=4,font=('arial',16,'bold'))
txtdisplay.grid(row=0,column=0,columnspan=4,padx=1)

# creating buttons row 1 with addition

btn7=Button(cal_f,width=4,bg='white',bd=4,font=('arial',16,'bold'),text='7')
btn7.grid(row=2,column=0)
btn8=Button(cal_f,width=4,bg='white',bd=4,font=('arial',16,'bold'),text='8')
btn8.grid(row=2,column=1)
btn9=Button(cal_f,width=4,bg='white',bd=4,font=('arial',16,'bold'),text='9')
btn9.grid(row=2,column=2)
btnadd=Button(cal_f,width=4,bg='white',bd=4,font=('arial',16,'bold'),text='+')
btnadd.grid(row=2,column=3)
btn6=Button(cal_f,width=4,bg='white',bd=4,font=('arial',16,'bold'),text='6')
btn6.grid(row=3,column=0)
btn5=Button(cal_f,width=4,bg='white',bd=4,font=('arial',16,'bold'),text='5')
btn5.grid(row=3,column=1)
btn4=Button(cal_f,width=4,bg='white',bd=4,font=('arial',16,'bold'),text='4')
btn4.grid(row=3,column=2)
btnsub=Button(cal_f,width=4,bg='white',bd=4,font=('arial',16,'bold'),text='-')
btnsub.grid(row=3,column=3)
btn3=Button(cal_f,width=4,bg='white',bd=4,font=('arial',16,'bold'),text='3')
btn3.grid(row=4,column=0)
btn2=Button(cal_f,width=4,bg='white',bd=4,font=('arial',16,'bold'),text='2')
btn2.grid(row=4,column=1)
btn1=Button(cal_f,width=4,bg='white',bd=4,font=('arial',16,'bold'),text='1')
btn1.grid(row=4,column=2)
btnmul=Button(cal_f,width=4,bg='white',bd=4,font=('arial',16,'bold'),text='*')
btnmul.grid(row=4,column=3)

btn0=Button(cal_f,width=4,bg='white',bd=4,font=('arial',16,'bold'),text='0')
btn0.grid(row=5,column=1)
btnclear=Button(cal_f,width=0,bg='white',bd=4,font=('arial',16,'bold'),text='CLR')
btnclear.grid(row=5,column=0)
btnequals=Button(cal_f,width=4,bg='white',bd=4,font=('arial',16,'bold'),text='=')
btnequals.grid(row=5,column=2)
btndiv=Button(cal_f,width=4,bg='white',bd=4,font=('arial',16,'bold'),text='%')
btndiv.grid(row=5,column=3)
mainloop()