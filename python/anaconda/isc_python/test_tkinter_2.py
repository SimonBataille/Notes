import tkinter

fenetre=0
canvas=0

lastX=0
lastY=0

couleur='black'

def onClique(event):
     global lastX, lastY, canvas
     lastX = event.x
     lastY=event.y
     
def onBouge(event):
     global lastX, lastY, canvas
     canvas.create_line(lastX, lastY, event.x, event.y, fill=couleur, width=5)
     lastX = event.x
     lastY=event.y

def setCouleurNoir(event):
    global couleur
    couleur='black'

def setCouleurRouge(event):
    global couleur
    couleur='red'
    

def initFenetre():
    global fenetre, canvas
    fenetre = tkinter.Tk()
    fenetre.title('Dessin 1.0')
    
    canvas = tkinter.Canvas(fenetre, width=800, height=600, bg='white')
    canvas.pack()
    
    black_id = canvas.create_rectangle(10, 10, 30, 30, fill='black')
    canvas.tag_bind(black_id, '<Button-1>', setCouleurNoir)
    
    red_id = canvas.create_rectangle(10, 40, 30, 60, fill='red')
    canvas.tag_bind(red_id, '<Button-1>', setCouleurRouge)
    
    canvas.bind('<Button-1>', onClique)
    canvas.bind('<B1-Motion>', onBouge)
    

initFenetre()
