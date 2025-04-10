import shutil
import time
import os
import threading
import multiprocessing
import tkinter as tk


calculation = ''
oSymbol = '*/+-^'

def intro():
    print('\n')
    #print("sLoWbRaIn.eXe".center(columns))
    print('      _       __          ___     _____       _____            __   __     ')
    print('     | |      \ \        / / |   |  __ \     |_   _|           \ \ / /     ')
    print('  ___| |     __\ \  /\  / /| |__ | |__) |__ _  | |  _ __    ___ \ V / ___  ')
    print(' / __| |    / _ \ \/  \/ / |  _ \|  _  // _` | | | |  _ \  / _ \ > < / _ \ ')
    print(' \__ \ |___| (_) \  /\  /  | |_) | | \ \ (_| |_| |_| | | ||  __// . \  __/ ')
    print(' |___/______\___/ \/  \/   |_.__/|_|  \_\__,_|_____|_| |_(_)___/_/ \_\___| ')
    print('\n')
    
    
    #print("braining")
    time.sleep(0.2)
    
    s = ""
    for x in range(38):
        s = s + ". "
        print(s, end='\r')
        time.sleep(0.02)
    os.system('cls')

def sOperation(x, y, o):
    if o == '+':
        return(x + y)
    if o == '-':
        return(x - y)
    if o == '*':
        return(x * y)
    if o == '/':
        return(x / y)
    if o == '^':
        c = x
        for i in range(int(y - 1)):
            x = x * c
        return x 

def operating(cleanO, n):
    print(f'n = {n}')
    o = cleanO[n]
    #find first number
    b = n - 1
    while oSymbol.find(cleanO[b]) == -1:
        b -= 1
        if b == -1:
            break
    b += 1
    x = cleanO[b:n]
    print(f'first num: {x}')
    
    #find second number
    e = n + 1
    while oSymbol.find(cleanO[e]) == -1:
        e += 1
        if e == len(cleanO):
            break
    y = cleanO[(n + 1):e]
    print(f'second num: {y}')
    
    #simple equation
    newNum = sOperation(float(x), float(y), o)
    print(f'newNum: {newNum}') 
    cleanO = cleanO[:b] + str(newNum) + cleanO[e:]
    print(f'new cleanO: {cleanO}')
    
    return cleanO  

def mainCalculation(userInput2):
    cleanO = userInput2
    print(cleanO)
    
    ss = cleanO.find('^')
    print(f'^ = {ss}')
    
    #power equation
    while ss != -1:
        print('squaring')
        cleanO = operating(cleanO, ss)
        ss = cleanO.find('^')
    
    #multiplication/division equation
    m = cleanO.find('*')
    print(f'm = {m}')
    d = cleanO.find('/')
    print(f'd = {d}')
    
    while m != -1 or d != -1:
    
        while m != -1 and d != -1:
            if m < d:
                print('multiplying first')
                cleanO = operating(cleanO, m)
                m = cleanO.find('*')
                d = cleanO.find('/')
            if d < m:
                print('dividing first')
                cleanO = operating(cleanO, d)
                m = cleanO.find('*')
                d = cleanO.find('/')
                
        while m != -1 and d == -1:
            print('multiplying only')
            cleanO = operating(cleanO, m)
            m = cleanO.find('*')
        while d != -1 and m == -1:
            print('dividing only')
            cleanO = operating(cleanO, d)
            d = cleanO.find('/')
        
    #addition/subtraction equation
    a = cleanO.find('+')
    print(f'a = {a}')
    s = cleanO.find('-')
    print(f's = {s}')
    
    while a != -1 or s > 0: 
        while a != -1 and s != -1:
            if a < s:
                print('adding first')
                cleanO = operating(cleanO, a)
                a = cleanO.find('+')
                s = cleanO.find('-')
            if s < a:
                print('subtracting first')
                cleanO = operating(cleanO, s)
                a = cleanO.find('+')
                s = cleanO.find('-')
                
        while a != -1 and s == -1:
            print('adding only')
            cleanO = operating(cleanO, a)
            a = cleanO.find('+')
        while s != -1 and a == -1:
            print('subtracting only')
            cleanO = operating(cleanO, s)
            s = cleanO.find('-')
            if s == 0:
                break
        if s == 0:
            break
        
    print(cleanO)
    return cleanO

def addToCalculator(symbol):
    global calculation
    calculation += str(symbol)
    result.delete(1.0, 'end')
    result.insert(1.0, calculation)

#backup function
'''
def evaluate():
    global calculation
    try:
        calculation = str(eval(calculation))
        result.delete(1.0, 'end')
        result.insert(1.0, calculation)
    except:
        clearField()
'''

def evaluate2():
    global calculation
    try:
        calculation = mainCalculation(calculation)
        print(calculation)
        result.delete(1.0, 'end')
        result.insert(1.0, calculation)
    except:
        clearField()

def clearField():
    global calculation
    calculation = ''
    result.delete(1.0, 'end')


intro()

#setup base box
m = tk.Tk()
m.title('slow brain')
m.geometry('220x155')

result = tk.Text(m, height = 1, width = 12, font = ("Arial", 24))
result.grid(columnspan = 6)

#buttons
bn1 = tk.Button(m, text = '1', command = lambda: addToCalculator(1), width = 4, font = ("Arial", 10))
bn1.grid(row = 4, column = 1)
bn2 = tk.Button(m, text = '2', command = lambda: addToCalculator(2), width = 4, font = ("Arial", 10))
bn2.grid(row = 4, column = 2)
bn3 = tk.Button(m, text = '3', command = lambda: addToCalculator(3), width = 4, font = ("Arial", 10))
bn3.grid(row = 4, column = 3)
bn4 = tk.Button(m, text = '4', command = lambda: addToCalculator(4), width = 4, font = ("Arial", 10))
bn4.grid(row = 3, column = 1)
bn5 = tk.Button(m, text = '5', command = lambda: addToCalculator(5), width = 4, font = ("Arial", 10))
bn5.grid(row = 3, column = 2)
bn6 = tk.Button(m, text = '6', command = lambda: addToCalculator(6), width = 4, font = ("Arial", 10))
bn6.grid(row = 3, column = 3)
bn7 = tk.Button(m, text = '7', command = lambda: addToCalculator(7), width = 4, font = ("Arial", 10))
bn7.grid(row = 2, column = 1)
bn8 = tk.Button(m, text = '8', command = lambda: addToCalculator(8), width = 4, font = ("Arial", 10))
bn8.grid(row = 2, column = 2)
bn9 = tk.Button(m, text = '9', command = lambda: addToCalculator(9), width = 4, font = ("Arial", 10))
bn9.grid(row = 2, column = 3)
bn0 = tk.Button(m, text = '0', command = lambda: addToCalculator(0), width = 4, font = ("Arial", 10))
bn0.grid(row = 5, column = 2)
bnA = tk.Button(m, text = '+', command = lambda: addToCalculator('+'), width = 4, font = ("Arial", 10))
bnA.grid(row = 5, column = 5)
bnS = tk.Button(m, text = '-', command = lambda: addToCalculator('-'), width = 4, font = ("Arial", 10))
bnS.grid(row = 4, column = 5)
bnM = tk.Button(m, text = '*', command = lambda: addToCalculator('*'), width = 4, font = ("Arial", 10))
bnM.grid(row = 3, column = 5)
bnD = tk.Button(m, text = '/', command = lambda: addToCalculator('/'), width = 4, font = ("Arial", 10))
bnD.grid(row = 2, column = 5)
bnE = tk.Button(m, text = '=', command = evaluate2, width = 4, font = ("Arial", 10))
bnE.grid(row = 5, column = 4)
bnP = tk.Button(m, text = '.', command = lambda: addToCalculator('.'), width = 4, font = ("Arial", 10))
bnP.grid(row = 5, column = 1)
bnO = tk.Button(m, text = '(', command = lambda: addToCalculator('('), width = 4, font = ("Arial", 10))
bnO.grid(row = 2, column = 4)
bnC = tk.Button(m, text = ')', command = lambda: addToCalculator(')'), width = 4, font = ("Arial", 10))
bnC.grid(row = 3, column = 4)
bnC = tk.Button(m, text = '^', command = lambda: addToCalculator('^'), width = 4, font = ("Arial", 10))
bnC.grid(row = 4, column = 4)
bnCE = tk.Button(m, text = 'CE', command = clearField, width = 4, font = ("Arial", 10))
bnCE.grid(row = 5, column = 3)

#main
m.mainloop()

