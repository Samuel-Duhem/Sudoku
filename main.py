from tkinter import Tk, Frame, Button, Label
from Sudoku import solve
from Board import Board
from multiple_choice import OptionDialog
from Generator import sudoku_generator
from random import randint
def color_picker(button,box):
    '''define the color based on the number of the box'''
    if box.occupant==0:
        button.config(bg='#b5a6c9')
    if box.occupant==1:
        button.config(bg='#6a4c93')
    if box.occupant==2:
        button.config(bg='#4267ac')
    if box.occupant==3:
        button.config(bg='#1982c4')
    if box.occupant==4:
        button.config(bg='#52a675')
    if box.occupant==5:
        button.config(bg='#8ac926')
    if box.occupant==6:
        button.config(bg='#c5ca30')
    if box.occupant==7:
        button.config(bg='#ffca3a')
    if box.occupant==8:
        button.config(bg='#ff924c')
    if box.occupant==9:
        button.config(bg='#ff595e')
        
my_game=Board()
def remplir(frame, my_game:Board, soluce: bool):
    buttons = []
    padx_values = {2: (1, 3), 3: (3, 1), 5: (1, 3), 6: (3, 1)}
    pady_values = {2: (1, 3), 3: (3, 1), 5: (1, 3), 6: (3, 1)}
    for c in range(9):
        row = []
        padx = padx_values.get(c, (1, 1))
        for r in range(9):
            pady = pady_values.get(r, (1, 1))
            occupant = my_game.terrain[r][c].occupant
            button = Button(
                frame,
                text=str(occupant),
                width=2,
                height=1
            )
            button.grid(row=r, column=c, padx=padx, pady=pady)
            row.append(button)
        buttons.append(row)
    for row in range(len(buttons)):
        for col in range(len(buttons[row])):
            if not soluce:
                buttons[row][col].config(command=lambda row=row, col=col: choix_nombre(buttons, row, col))
            color_picker(buttons[row][col], my_game.terrain[col][row])



def solution():
    global my_game
    print(my_game)
    my_game=solve(my_game)
    print(soluce)
    frame_soluce=Frame(root,  width=650,  height=400,  bg='#7f7f7f')
    frame_soluce.grid(row=0,  column=2,  padx=50,  pady=20)
    remplir(frame_soluce,soluce,soluce=True)

    bottom_frame_right  =  Frame(root,  width=200,  height=  400,  bg='#7f7f7f')
    bottom_frame_right.grid(row=1,  column=2,  padx=50,  pady=20)
    Button(bottom_frame_right,command=reset, text ='Réinitialiser le terrain').grid(row=0,column=5,padx=30,  pady=20)

def init():
    global my_game
    my_game=Board()
    # Create left and right frames
    bottom_frame  =  Frame(root,  width=200,  height=  400,  bg='#7f7f7f')
    bottom_frame.grid(row=1,  column=1,  padx=50,  pady=20)

    Button(bottom_frame, text ='Solution',command=solution).grid(row=0,column=1,padx=30,  pady=20)

    top_frame  =  Frame(root,  width=650,  height=400,  bg='#7f7f7f')
    top_frame.grid(row=0,  column=1,  padx=50,  pady=20)

    left_frame  =  Frame(root,  width=200,  height=400,  bg='#7f7f7f')
    left_frame.grid(row=0,  column=0,  padx=50,  pady=20)

    Label(left_frame,text='Choisir la difficulté').grid(row=0,column=0,padx=10,pady=10)

    for i in range(5):
        Button(left_frame,text=str(i+1),command=lambda i=i, top_frame=top_frame: generate(top_frame,i)).grid(row=i+1,column=0,padx=10,pady=10)
    remplir(top_frame,my_game,soluce=False)
    return (bottom_frame,top_frame,my_game)
root = Tk(screenName='Soduku')
root.title("Sudoku")
root.minsize(300,300)
root.eval('tk::PlaceWindow . center')
root.config(bg='#0A2342')
Gibberish=init()
bottom_frame=Gibberish[0]
top_frame=Gibberish[1]
my_game=Gibberish[2]
my_game.set_terrain([
        [0,0,0,0,0,0,6,0,2],
        [0,6,2,8,7,0,0,3,4],
        [3,4,1,9,0,0,0,7,8],
        [0,9,6,7,2,8,4,0,3],
        [0,0,4,6,0,3,0,1,0],
        [0,5,0,0,0,0,7,0,6],
        [7,0,9,1,0,6,2,0,5],
        [0,0,0,0,3,7,0,0,1],
        [0,1,5,2,8,9,0,6,0]
    ]
)

remplir(top_frame,my_game,False)
def generate(frame,i):
    global my_game
    global soluce
    if i==0:
        k=randint(20,34)
    elif i==1:
        k=randint(35,45)
    elif i ==2:
        k=randint(46,49)
    elif i==3:
        k=randint(50,53)
    elif i==4:
        k=randint(54,64)
    my_game=sudoku_generator(k)
    remplir(frame,my_game,False)
    print(my_game)
def choix_nombre(buttons,row,col):
    global my_game
    possible=my_game.terrain[row][col].possible
    dlg = OptionDialog(root,'Select a number',"Close= reset ",possible)
    buttons[row][col].config(text=str(dlg.result))
    my_game.terrain[col][row].arrival(dlg.result)
    if dlg.result!=0:
        my_game.terrain[col][row].base=True
    else :
        my_game.terrain[col][row].base=False

def reset():
    global bottom_frame, top_frame,my_game
    for widget in root.winfo_children():
        widget.destroy()

    # Call the init() function to reinitialize theBoard
    (bottom_frame, top_frame,my_game) = init()


root.mainloop()
# zéro == rien 
# générer une grille reset
# commentaires
# déffinir le terrain pour le résoudre soi même+ vérif coloré dessus
# vérif si la grille a une solution
#Qand on génère une grille, automatiquement stocker le résultat
