from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()

canvas = Canvas(root, width=500, height=500)
canvas.pack(padx=15, pady=15)
margin = 15


def draw_board():
    thick_line = False
    
    for x in range(10):
        if x % 3 == 0:
            line_colour = "blue"
        else:
            line_colour = "grey"

        if x == 3 or x == 6:
            thick_line = 3
        else:
            thick_line = 1

        canvas.create_line(margin, margin + x * 500/10, 470, margin + x * 500/10, fill=line_colour, width=thick_line)

        canvas.create_line(margin + x * 500/10, margin, margin + x * 500/10, 470, fill=line_colour, width=thick_line)


def input_buttons():
        w = 6
        frame = Frame(width=500, height=100)
        frame.pack(side=BOTTOM)
        button1 = Button(frame,text="1",width=w)
        button1.place(x=12, y = 0)
        button2 = Button(frame,text="2",width=w)
        button2.place(x=40,y=20)
        button3 = Button(frame,text="3",width=w)
        button3.place(x=60,y=20)
        button4 = Button(frame,text="4",width=w)
        button4.place(x=100, y=20)
        button5 = Button(frame,text="5",width=w)
        button5.place(x=120, y=20)
        button6 = Button(frame,text="6",width=w)
        button6.place(x=140, y=20)
        button7 = Button(frame,text="7",width=w)
        button7.place(x=160, y=20)
        button8 = Button(frame,text="8",width=w)
        button8.place(x=180, y=20)
        button9 = Button(frame,text="9",width=w)
        button9.place(x=200, y=20)
        undo = Button(frame, text="<--", width=w)
        undo.place(x=100, y= 40)
        redo = Button(frame, text="-->", width=w)
        redo.place(x=120, y=40)
   


root.mainloop() 

def input_numbers(self,board):
    for x in range(9):
        for i in range(9):
            if board[x][i] is not "0":
                number = board[x][i]
                x = margin + i * self.box_size + self.box_size/2
                y = margin + x * self.box_size + self.box_size/2
                if original_board[x][i] == board[x][i]:
                    text_colour = "black"
                else:
                    text_colour = "red"
                self.canvas.create_text(x,y,text=number, fill=text_colour)

#from tkinter import *
#from PIL import ImageTk, Image
#import os


img = ImageTk.PhotoImage(Image.open("sudoku.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()




def undo(self):
    if stack_num.empty == True:
        return

    previous_number = previous_num.pop()
    number = stack_num.pop()
    row = stack_row.pop()
    col = stack_column.pop()

    updated_board[int(b.row)][int(b.col)] = previous_number
    
    b.canvas.delete("all")
    b.draw_board()
    b.input_numbers(updated_board,original_board)

















