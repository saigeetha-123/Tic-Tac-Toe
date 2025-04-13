from tkinter import *
from tkinter import messagebox

def ButtonClick(button):
    global X_O, flag
    if button["text"] == "":
        button["bg"] = "#800080"
        button["text"] = "X" if X_O else "O"
        X_O = not X_O
        flag += 1
        CheckForWin()
    else:
        messagebox.showinfo("Tic Tac Toe", "Player has already entered!")

def CheckForWin():
    wins = [
        (button1, button2, button3),
        (button4, button5, button6),
        (button7, button8, button9),
        (button1, button4, button7),
        (button2, button5, button8),
        (button3, button6, button9),
        (button1, button5, button9),
        (button3, button5, button7)
    ]

    for a, b, c in wins:
        if a["text"] == b["text"] == c["text"] and a["text"] != "":
            messagebox.showinfo("Tic Tac Toe", f"Player {a['text']} has Won")
            reset_game()
            return

    if flag == 9:
        messagebox.showinfo("Tic Tac Toe", "Game is Tied!")
        reset_game()

def reset_game():
    global X_O, flag
    for btn in [button1, button2, button3, button4, button5, button6, button7, button8, button9]:
        btn.config(text="", bg="#a4f4f9", state=NORMAL)  # Updated to original color
    X_O = True
    flag = 0

main = Tk()
main.title("Tic Tac Toe")
main.configure(bg="#b9f2ff")  # Optional: window background

X_O = True
flag = 0

button1 = Button(main, text="", font=("arial", 60, "bold"), bg="#a4f4f9", fg="white", width=3, command=lambda: ButtonClick(button1))
button1.grid(row=0, column=0)

button2 = Button(main, text="", font=("arial", 60, "bold"), bg="#a4f4f9", fg="white", width=3, command=lambda: ButtonClick(button2))
button2.grid(row=0, column=1)

button3 = Button(main, text="", font=("arial", 60, "bold"), bg="#a4f4f9", fg="white", width=3, command=lambda: ButtonClick(button3))
button3.grid(row=0, column=2)

button4 = Button(main, text="", font=("arial", 60, "bold"), bg="#a4f4f9", fg="white", width=3, command=lambda: ButtonClick(button4))
button4.grid(row=1, column=0)

button5 = Button(main, text="", font=("arial", 60, "bold"), bg="#a4f4f9", fg="white", width=3, command=lambda: ButtonClick(button5))
button5.grid(row=1, column=1)

button6 = Button(main, text="", font=("arial", 60, "bold"), bg="#a4f4f9", fg="white", width=3, command=lambda: ButtonClick(button6))
button6.grid(row=1, column=2)

button7 = Button(main, text="", font=("arial", 60, "bold"), bg="#a4f4f9", fg="white", width=3, command=lambda: ButtonClick(button7))
button7.grid(row=2, column=0)

button8 = Button(main, text="", font=("arial", 60, "bold"), bg="#a4f4f9", fg="white", width=3, command=lambda: ButtonClick(button8))
button8.grid(row=2, column=1)

button9 = Button(main, text="", font=("arial", 60, "bold"), bg="#a4f4f9", fg="white", width=3, command=lambda: ButtonClick(button9))
button9.grid(row=2, column=2)

main.mainloop()
