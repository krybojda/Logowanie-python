import tkinter as tk
from tkinter import *
from functools import partial
from tkinter import messagebox
import mysql.connector



try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="logowanie_python"
    )
    print("Połączono z bazą")
except:
        print("Błąd łączenia z bazą")




def zaloguj(log1, has1):
    try:
        print(log1.get())
        print(has1.get())


        connect = conn.cursor()

        loginchk = log1.get()
        passchk = has1.get()

        query1 = "SELECT * FROM dane WHERE login=%s AND password=%s"
        val1 = (loginchk, passchk)
        connect.execute(query1, val1)
        
        #conn.commit()
        result = connect.fetchone()
        conn.close()
        connect.close()

        if result is not None:
            print("Poprawinie zalogowano")
            zalogowano(window, log1)
            #dodanie funkcji ktora ma sie wykonać po zalogowaniu
        else:
            print("Błąd logowania")
            blad_logowania(window, log1)

    except Exception as e:
        print("Błąd funkcji zaloguj: ", e)


def zalogowano(window, log1):
    try:
        zalogowano_okno = tk.Toplevel(window)
        zalogowano_okno.title("Zalogowano")
        zalogowano_okno.configure(background='lightblue')
    
        napis_zalogowano = tk.Label(zalogowano_okno, text="Poprawnie zalogowano: "+  log1.get())
        napis_zalogowano.pack(padx=20, pady=20)
        napis_zalogowano.configure(background='lightblue')
        print("Zalogowano: "+log1.get())
    except:
        print("error otwarcia okna zalogowania")


def blad_logowania(window, log1):
    try:
        niezalogowano_okno = tk.Toplevel(window)
        niezalogowano_okno.title("Błąd logowania")
        niezalogowano_okno.configure(background='lightblue')
    
        napis_zalogowano = tk.Label(niezalogowano_okno, text="Błąd logowania")
        napis_zalogowano.pack(padx=20, pady=20)
        napis_zalogowano.configure(background='lightblue')
    except:
        print("error otwarcia okna niezalogowania")




def register(window):

    try:
        register_okno = tk.Toplevel(window)
        register_okno.title("Rejestracja")
        register_okno.geometry("400x280")
        register_okno.maxsize(400, 280)
        register_okno.configure(background='lightblue')

        register_okno.columnconfigure(0, weight=1)
        register_okno.columnconfigure(1, weight=1)

        

        napis = tk.Label(register_okno, text="Rejestracja", font=("Times_New_Roman, 25"), bg="lightblue")
        napis.grid(column=0, row=0, columnspan=4, sticky=tk.EW, padx=0, pady=20)

        
        tmp111 = tk.Label(register_okno, text="                     ", font=("Arial, 14"), bg="lightblue")
        tmp111.grid(column=3, row=1, sticky=tk.E, padx=0, pady=0)
        email_reg = tk.Label(register_okno, text="E-mail:", anchor="e", justify="right", width=8, font=("Arial, 14"), bg="lightblue")
        email_reg.grid(column=1, row=1, sticky=tk.EW, padx=0, pady=5)
        email1_reg = StringVar()
        email_reg = tk.Entry(register_okno, width=15, textvariable=email1_reg, font=("Arial, 14"))
        email_reg.grid(column=2, row=1, sticky=tk.EW, padx=0, pady=5)


        tmp11 = tk.Label(register_okno, text="                     ", font=("Arial, 14"), bg="lightblue")
        tmp11.grid(column=3, row=1, sticky=tk.E, padx=0, pady=0)
        loginname_reg = tk.Label(register_okno, text="Login:", anchor="e", justify="right", width=8, font=("Arial, 14"), bg="lightblue")
        loginname_reg.grid(column=1, row=2, sticky=tk.EW, padx=0, pady=5)
        log1_reg = StringVar()
        login_reg = tk.Entry(register_okno, width=15, textvariable=log1_reg, font=("Arial, 14"))
        login_reg.grid(column=2, row=2, sticky=tk.EW, padx=0, pady=5)


        tmp22 = tk.Label(register_okno, text="                     ", font=("Arial, 14"), bg="lightblue")
        tmp22.grid(column=3, row=2, sticky=tk.E, padx=0, pady=0)
        hasloname_reg = tk.Label(register_okno, text="Password:", anchor="e", justify="right", width=8, font=("Arial, 14"), bg="lightblue")
        hasloname_reg.grid(column=1, row=3, sticky=tk.EW, padx=0, pady=5)
        has1_reg = StringVar()
        haslo_reg = tk.Entry(register_okno, show="*", width=15, textvariable=has1_reg, font=("Arial, 14"))
        haslo_reg.grid(column=2, row=3, sticky=tk.EW, padx=0, pady=5)

        register_reg= tk.Button(register_okno, text="Potwierdź", command=lambda: sprawdzanie(register_okno,email_reg, log1_reg, haslo_reg), width=12, height=1)
        register_reg.grid(column=0, row=4, columnspan=4, padx=10, pady=30)

        

    except:
        print("error z funkcją register()")



    def sprawdzanie(register_okno,email1_reg, log1_reg, haslo_reg):
        
        connect = conn.cursor()

        query = "INSERT INTO dane (email, login, password) VALUES (%s, %s, %s)"
        val = (email1_reg.get(), log1_reg.get(), haslo_reg.get())
        connect.execute(query, val)
        
        conn.commit()

        conn.close()
        connect.close()
        

        if True:
            potwierdzenie(register_okno, log1_reg)
        else:
            zaprzeczenie(register_okno)





def potwierdzenie(register_okno, log1_reg):
    try:
        dobrze = tk.Toplevel(register_okno)
        dobrze.title("Zarejestrowano")
        dobrze.configure(background='lightblue')
    
        napis_dobrze = tk.Label(dobrze, text="Poprawnie zarejestrowano konto: "+  log1_reg.get())
        napis_dobrze.pack(padx=20, pady=20)
        napis_dobrze.configure(background='lightblue')
        print("Poprawnie otworzono okno z potwierdzeniem")
        print("Zarejestrowano konto: "+log1_reg.get())
    except:
        print("error otwarcia okna z potwierdzeniem")

def zaprzeczenie(register_okno):
    try:
        zle = tk.Toplevel(register_okno)
        zle.title("Błąd w rejestracji")
        zle.configure(background='lightblue')
    
        zle_napis = tk.Label(zle, text="Nie zarejestowano!")
        zle_napis.pack(padx=20, pady=20)
        zle_napis.configure(background='lightblue')
        print("Poprawnie otworzono okno z zaprzeczeniem")
    except:
        print("error otwarcia okna z zaprzeczeniem")




window = tk.Tk()
window.title("Logowanie")
window.geometry("500x300")
window.maxsize(500, 300)
window.configure(background='lightblue')

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

title = tk.Label(window, text="Logowanie", font=("Times_New_Roman, 30"), bg="lightblue")
title.grid(column=0, row=0, columnspan=4, sticky=tk.EW, padx=0, pady=20)




tmp1 = tk.Label(window, text="                     ", font=("Arial, 14"), bg="lightblue")
tmp1.grid(column=3, row=1, sticky=tk.E, padx=0, pady=0)
loginname = tk.Label(window, text="Login:", anchor="e", justify="right", width=8, font=("Arial, 14"), bg="lightblue")
loginname.grid(column=1, row=1, sticky=tk.EW, padx=0, pady=5)
log1 = StringVar()
login = tk.Entry(window, width=15, textvariable=log1, font=("Arial, 14"))
login.grid(column=2, row=1, sticky=tk.EW, padx=0, pady=5)


tmp2 = tk.Label(window, text="                     ", font=("Arial, 14"), bg="lightblue")
tmp2.grid(column=3, row=2, sticky=tk.E, padx=0, pady=0)
hasloname = tk.Label(window, text="Password:", anchor="e", justify="right", width=8, font=("Arial, 14"), bg="lightblue")
hasloname.grid(column=1, row=2, sticky=tk.EW, padx=0, pady=5)
has1 = StringVar()
haslo = tk.Entry(window, show="*", width=15, textvariable=has1, font=("Arial, 14"))
haslo.grid(column=2, row=2, sticky=tk.EW, padx=0, pady=5)

registerb= tk.Button(window, text="Register", command=lambda: register(window), width=12, height=1)
registerb.grid(column=0, row=3, columnspan=2, padx=10, pady=30)

zaloguj = partial(zaloguj, log1, has1)

loginb= tk.Button(window, text="Login", command= zaloguj, width=12, height=1)
loginb.grid(column=2, row=3, columnspan=2, padx=10, pady=30)


window.mainloop()