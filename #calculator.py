"""Design a graphical user interface and familiarize yourself with a library like Tkinter.
This library allows you to create buttons to perform different operations and display results on screen"""


#CALCOLATRICE
def addizione():
    print("ADDIZIONE")
    n = float(input("INSERISCI UN NUMERO: "))
    t = 0 #TOTALE NUMERI INSERITI
    sum1 = 0
    while n != 0:
        sum1 = sum1 + n
        t +=1
        n = float(input("INSERISCI UN'ALTRO NUMERO: "))
    return [sum1, t]


def sottrazione ():
    print("SOTTRAZIONE")
    n = float(input("INSERISCI IL NUMERO: "))
    t = 0 #TOTALE NUMERI INSERITI
    sum2 = 0
    while n != 0:
        sum2 = sum2 - n 
        t += 1
        n = float(input("INSERISCI UN ALTRO NUMERO: "))
    return [sum2 , t]


def moltiplicazione ():
    print("MULTIPLICAZIONE")
    n = float(input("INSERISCI IL NUMERO: "))
    t = 0 #TOTALE NUMERI INSERITI
    sum3 = 0
    while n != 0:
        sum3 = sum3 * n
        t += 1
        n = float(input("INSERIRE UN'ALTRA NUMERO: "))
    return [sum3, t]

    
def media():
    an = []
    an = addizione()
    t = an [1]
    a = an [0]
    ans = a / t
    return [ans, t]

# main...
while True:
    list = []
    print(" IL MIO PRIMO PROGRAMMA PYTHON")
    print(" SEMPLICE CALCOLATRICE IN PYTHON DI ROBERO PIRRELLO")
    print(" Enter 'a' for addizione")
    print(" Enter 's' for sottrazione")
    print(" Enter 'm' for moltiplicazione")
    print(" Enter 'me' for media")
    print(" Enter 'q' for quit")
    c = input(" ")

    if c != 'q':

        if c == 'a':
            list = addizione()
            print("Sum = ", list[0], "total inputs", list[1])

        elif c == 's':
            list = sottrazione()
            print("Sum = ", list[0], "total inputs", list[1])

        elif c == 'm':
            list = moltiplicazione()
            print("Sum = ", list[0], "total inputs", list[1])

        elif c == 'me':
            list = media()
            print("Sum =", list[0], "total inputs", list[1])
        else:
            print("SCUSAMI, CARATTERE INVALIDE")
    else:

        break
