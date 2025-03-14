from tkinter import *
from tkinter.messagebox import *
from Sudoku import *
from Jeu import *
from multiple_choice import *
from Generator import *
from random import randint
def color_picker(button,case):
    if case.occupant==0:
        button.config(bg='#b5a6c9')
    if case.occupant==1:
        button.config(bg='#6a4c93')
    if case.occupant==2:
        button.config(bg='#4267ac')
    if case.occupant==3:
        button.config(bg='#1982c4')
    if case.occupant==4:
        button.config(bg='#52a675')
    if case.occupant==5:
        button.config(bg='#8ac926')
    if case.occupant==6:
        button.config(bg='#c5ca30')
    if case.occupant==7:
        button.config(bg='#ffca3a')
    if case.occupant==8:
        button.config(bg='#ff924c')
    if case.occupant==9:
        button.config(bg='#ff595e')
        
monjeu=Jeu()
def remplir(frame,monjeu:Jeu,Soluce):
    buttons=[]
    for c in range(9):
        row = []
        if c==2:
            padx=(1,3)
        elif c==3:
            padx=(3,1)
        elif c==5:
            padx=(1,3)
        elif c==6:
            padx=(3,1)
        else:
            padx=(1,1)
        for r in range(9):
            if r==2:
                pady=(1,3)
            elif r==3:
                pady=(3,1)
            elif r==5:
                pady=(1,3)
            elif r==6:
                pady=(3,1)
            else:
                pady=(1,1)
            occupant=monjeu.terrain[r][c].occupant
            button = Button(
                frame,
                text=str(occupant),
                width=2,
                height=1
            )
            button.grid(row=r, column=c,padx=padx,pady=pady)
            row.append(button)
        buttons.append(row)
    for row in range(len(buttons)):
        for col in range(len(buttons[row])):
            if Soluce==False:
                buttons[row][col].config(command=lambda row=row, col=col: ChoixNombre(buttons,row, col))
            color_picker(buttons[row][col],monjeu.terrain[col][row])

def solution():
    global monjeu
    print(monjeu)
    monjeu,soluce=resoudre(monjeu)
    print(soluce)
    Frame_Soluce=Frame(root,  width=650,  height=400,  bg='#7f7f7f')
    Frame_Soluce.grid(row=0,  column=2,  padx=50,  pady=20)
    remplir(Frame_Soluce,soluce,Soluce=True)

    bottom_frame_right  =  Frame(root,  width=200,  height=  400,  bg='#7f7f7f')
    bottom_frame_right.grid(row=1,  column=2,  padx=50,  pady=20)
    Button(bottom_frame_right,command=reset, text ='Réinitialiser le terrain').grid(row=0,column=5,padx=30,  pady=20)

def init():
    global monjeu
    monjeu=Jeu()
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
    remplir(top_frame,monjeu,Soluce=False)
    return (bottom_frame,top_frame,monjeu)
root = Tk(screenName='Soduku')
root.title("Sudoku")
root.minsize(300,300)
root.eval('tk::PlaceWindow . center')
root.config(bg='#0A2342')
Gibberish=init()
bottom_frame=Gibberish[0]
top_frame=Gibberish[1]
monjeu=Gibberish[2]
monjeu.SetTerrain([
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

remplir(top_frame,monjeu,False)
def generate(frame,i):
    global monjeu
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
    monjeu=sudokuGenerator(k)
    remplir(frame,monjeu,False)
    print(monjeu)
def ChoixNombre(buttons,row,col):
    global monjeu
    possible=monjeu.terrain[row][col].possible
    dlg = OptionDialog(root,'Select a number',"Close= reset ",possible)
    buttons[row][col].config(text=str(dlg.result))
    monjeu.terrain[col][row].occupant=dlg.result
    if dlg.result!=0:
        monjeu.terrain[col][row].base=True
    else :
        monjeu.terrain[col][row].base=False

def reset():
    global bottom_frame, top_frame,monjeu
    for widget in root.winfo_children():
        widget.destroy()

    # Call the init() function to reinitialize the game
    (bottom_frame, top_frame,monjeu) = init()


root.mainloop()
# zéro == rien 
# générer une grille reset
# commentaires
# déffinir le terrain pour le résoudre soi même+ vérif coloré dessus
# vérif si la grille a une solution
