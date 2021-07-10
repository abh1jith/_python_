# Dice Rolling Simulator
"""
Dice Uni-codes:
0 : 🎲,
1 : ⚀,
2 : ⚁,
3 : ⚂,
4 : ⚃,
5 : ⚄,
6 : ⚅
"""

from tkinter import *



dice = {
    0 : '🎲',
    1 : '⚀',
    2 : '⚁',
    3 : '⚂',
    4 : '⚃',
    5 : '⚄',
    6 : '⚅'
}

def rolldice():
    from random import randint
    i = randint(1, 6)
    outcome = Label(text = dice[i], font = ('Times', 150), width = 2)
    outcome.grid(row = 1, column = 0)


Dice = Tk()
Text = Label(text = 'DICE SIMULATOR', font = ('Times', 30))
Start = Label(text = dice[0], font = ('Times', 150))
Creds = Label(text = '-By Abhijith', font = ('Times', 9))
RollButton = Button(text = "Roll", font =('Ariel', 20), command = rolldice)
Text.grid(row = 0, column = 0)
Start.grid(row = 1, column = 0)
RollButton.grid(row = 2, column = 0)
Creds.grid(row = 3, column = 0)

Dice.mainloop()
