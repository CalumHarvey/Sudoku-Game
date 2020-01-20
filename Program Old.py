import random
from tkinter import *
import math

column_dict = {"A":"1", "B":"2", "C":"3", "D":"4", "E":"5", "F":"6", "G":"7", "H":"8", "I":"9"}


class boardUI:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root,height=480,width=500, highlightthickness=0)
        self.canvas.pack(fill=BOTH, side=TOP, padx=20, pady=20)
        self.root.resizable(width=False, height=False)
        self.margin = 20
        self.box_size = 450/9
        self.num = "0"
        self.row = "0"
        self.column = "0"
        self.col = "0"
        self.row = "0"

    def draw_board(self):
        thick_line = False
    
        for x in range(10):
            if x % 3 == 0:
                line_colour = "blue"
                thick_line = 3
                extra = 1
            else:
                line_colour = "grey"
                thick_line = 1
                extra = 0
    
            self.canvas.create_line(self.margin-extra, self.margin + x * 500/10, 470+extra, self.margin + x * 500/10, fill=line_colour, width=thick_line)
            self.canvas.create_line(self.margin + x * 500/10, self.margin, self.margin + x * 500/10, 470, fill=line_colour, width=thick_line)


    def input_numbers(self,board,original_board):
        for z in range(9):
            for i in range(9):
                if board[z][i] is not "0":
                    number = board[z][i]
                    x = self.margin + i * self.box_size + self.box_size/2
                    y = self.margin + z * self.box_size + self.box_size/2

                    if original_board[z][i] == number:
                        text_colour = "black"
                    else:
                        text_colour = "red"
            
                    self.canvas.create_text(x,y,text=number, fill=text_colour, font=("Ariel",16))




    def input_buttons(self):
            w = 6
            frame = Frame(self.root,width=470, height=100, padx=3)
            frame.pack(side=TOP)
            button1 = Button(frame,text="1",width=w,relief=GROOVE,command=self.num1)
            button1.place(x=0, y = 0)
            button2 = Button(frame,text="2",width=w,relief=GROOVE,command=self.num2)
            button2.place(x=50,y=0)
            button3 = Button(frame,text="3",width=w,relief=GROOVE,command=self.num3)
            button3.place(x=100,y=0)
            button4 = Button(frame,text="4",width=w,relief=GROOVE,command=self.num4)
            button4.place(x=150, y=0)
            button5 = Button(frame,text="5",width=w,relief=GROOVE,command=self.num5)
            button5.place(x=200, y=0)
            button6 = Button(frame,text="6",width=w,relief=GROOVE,command=self.num6)
            button6.place(x=250, y=0)
            button7 = Button(frame,text="7",width=w,relief=GROOVE,command=self.num7)
            button7.place(x=300, y=0)
            button8 = Button(frame,text="8",width=w,relief=GROOVE,command=self.num8)
            button8.place(x=350, y=0)
            button9 = Button(frame,text="9",width=w,relief=GROOVE,command=self.num9)
            button9.place(x=400, y=0)
            undo = Button(frame, text="Undo", width=w,relief=GROOVE,command=s.undo())
            undo.place(x=175, y=40)
            redo = Button(frame, text="Redo", width=w,relief=GROOVE)
            redo.place(x=225, y=40)
            back = Button(self.root,text="Back to Main Menu", width=15, relief=GROOVE,command=menu_main_board)
            back.place(x=50,y=575)


    def num1(self):
        self.num = "1"
        self.add_number()
        self.new_board()

    def num2(self):
        self.num = "2"
        self.add_number()
        self.new_board()

    def num3(self):
        self.num = "3"
        self.add_number()
        self.new_board()

    def num4(self):
        self.num = "4"
        self.add_number()
        self.new_board()

    def num5(self):
        self.num = "5"
        self.add_number()
        self.new_board()

    def num6(self):
        self.num = "6"
        self.add_number()
        self.new_board()

    def num7(self):
        self.num = "7"
        self.add_number()
        self.new_board()

    def num8(self):
        self.num = "8"
        self.add_number()
        self.new_board()

    def num9(self):
        self.num = "9"
        self.add_number()
        self.new_board()
    
    def cell_clicked(self,event):
        
        if event.x > 19 and event.x < 466 and event.y > 18 and event.y < 466:
            
            self.canvas.delete("outline")
            self.canvas.focus_set()

            row = math.floor((event.y-20)/50)
            col = math.floor((event.x-20)/50)
    
            if updated_board[row][col] == "0":
                self.row = row
                self.col = col
                print("row", row)
                print("col", col)

            self.canvas.create_rectangle(20+(50*col),20+(50*row),20+(50*col)+50,20+(50*row)+50,outline="red",tags="outline")


    def new_board(self):
        print("\n")
        check = checks(updated_board)
        s.record_changes(self.num,self.row,self.col)
        self.canvas.delete("all")
        self.draw_board()
        self.input_numbers(updated_board,original_board)

    
    def add_number(self):
        updated_board[int(self.row)][int(self.col)] = self.num

    def victory(self):
        self.canvas.delete("all")
        self.canvas.create_text(200, 200, text="Congrats")

def choose_difficulty():
    choose = Tk()
    choose.resizable(width=False, height=False)
    choose.geometry("400x200")
    label = Label(choose, text="Please select the difficulty that you want")
    label.pack(side=TOP,pady=30)
    diff1 = Button(choose,text="Easy",width=7,relief=GROOVE,command= lambda: diff_easy(choose))
    diff1.place(x=70,y=100)
    diff2 = Button(choose,text="Medium",width=7,relief=GROOVE,command= lambda: diff_med(choose))
    diff2.place(x=170,y=100)
    diff3 = Button(choose,text="Hard",width=7,relief=GROOVE,command= lambda: diff_hard(choose))
    diff3.place(x=270,y=100)
    choose.mainloop()
        

def diff_easy(choose):
    global difficulty
    difficulty = 1
    done = True
    choose.destroy()
    main()
        

def diff_med(choose):
    global difficulty
    difficulty = 2
    done = True
    choose.destroy()
    main()

def diff_hard(choose):
    global difficulty
    difficulty = 4
    done = True
    choose.destroy()
    main()


class menu:
    def __init__(self):
        self.menu = Tk()
        self.menu.resizable(width=False, height=False)
        self.frame = Frame(self.menu, height=500, width=500)
        self.frame.pack(side=TOP, fill=BOTH)

    def title(self):
        title = Label(self.menu, text="Sudoku", font=("Ariel", 50),fg="blue")
        title.place(x=135, y=50)

    def buttons(self):
        play = Button(self.frame, text="Play", width=14,height=3,relief=GROOVE,command= lambda: choose_difficulty())
        play.place(x=115, y=175)
        leaderboard = Button(self.frame, text="Leaderboard", width=14, height=3,relief=GROOVE)
        leaderboard.place(x=285, y=175)
        settings = Button(self.frame, text="Settings", width=14, height=3,relief=GROOVE)
        settings.place(x=115,y=300)
        help1 = Button(self.frame, text="Rules and Help", width=14, height=3,relief=GROOVE,command=main_help)
        help1.place(x=285,y=300)
        


class help:
    def __init__(self):
        self.help1 = Tk()
        self.help1.resizable(width=False, height=False)
        self.frame = Frame(self.help1, height=500, width=700)
        self.frame.pack(side=TOP, fill=BOTH)

    def make_page(self):
        rules_title = Label(self.frame, text="Rules", font=("Ariel", 16))
        rules_title.place(x=165,y=50)
        rules1 = Label(self.frame, text="1. Each puzzle consists of a 9x9 grid that must be conpleted in order to win the game" , font=("Ariel",10),wraplength=300)
        rules1.place(x=50,y=105)
        rules2 = Label(self.frame, text="2. Each row in the puzzle must have numbers 1-9 and have no duplicates" , font=("Ariel",10),wraplength=300)
        rules2.place(x=50,y=155)
        rules3 = Label(self.frame, text="3.Each column must have numbers 1-9 and have no duplicates" , font=("Ariel",10),wraplength=300)
        rules3.place(x=50,y=205)
        rules4 = Label(self.frame, text="4.Each 3x3 box must have numbers 1-9 and have no duplicates" , font=("Ariel",10),wraplength=300)
        rules4.place(x=50,y=255)

        title_help = Label(self.frame, text="Help", font=("Ariel", 16))
        title_help.place(x=500,y=50)
        help1 = Label(self.frame, text="1.To start a game, click play on the main menu and select a difficulty" , font=("Ariel",10),wraplength=300)
        help1.place(x=400,y=105)
        help1 = Label(self.frame, text="2.When playing the game first click a box and then click the number that you want to enter" , font=("Ariel",10),wraplength=300)
        help1.place(x=400,y=155)

        back_button = Button(self.frame,text="Back to Main Menu", width=15, relief=GROOVE,command= lambda: menu_main_help())
        back_button.place(x=50,y=400)
        self.help1.mainloop()
        

'''
INTERFACE FINISHED
'''

def read_board():
    global file_num
    global file

    

    if difficulty == 1:
        file_num = random.randint(1,3)
        #Remove file_num = 1 when all the boards are complete
        file = (str(file_num) + ".txt")
    elif difficulty == 2:
        file_num = random.randint(4,6)
        file = (str(file_num) + ".txt")
    elif difficulty == 4:
        file_num = 10
        file = str(file_num) + ".txt"
    else:
        file_num = random.randint(7,9)
        file = (str(file_num) + ".txt")
        
    board = get_board(file)
    return board
       
def get_board(file):
        
    f = open(file, "r")
    file = f.read()

    board = file.split()
    
    board1 = []
    for x in range(9):
        b = board[x].strip("\n")
        board1.append(b)

    board2 = []
    for x in range(9):
        board3 = board1[x].split(",")
        board2.append(board3)
    f.close()
    return board2



class Sudoku_board:
    def __init__(self,board,file_num):
        self.board = board
        if file_num == 1 or file_num == 2 or file_num == 3:
            self.difficulty = "Easy"
        elif file_num == 4 or file_num == 5 or file_num == 6:
            self.difficulty = "Medium"
        else:
            self.difficulty = "Hard"

    def print_board(self):
        counter = 0
        print("        ",self.difficulty)
        print("         Columns")
        print("       ABC DEF GHI")
        for i in range(11):
            if i ==3 or i ==7:
                print("       ---+---+---")
            else:
                counter2 = 0
                temp = []
                if i == 5:
                    temp.append("Rows 5 ")
                elif i >= 7:
                    temp.append("     ")
                    temp.append(i-1)
                    temp.append(" ")
                elif i >= 3:
                    temp.append("     ")
                    temp.append(i)
                    temp.append(" ")
                else:
                    temp.append("     ")
                    temp.append(i+1)
                    temp.append(" ")
                        
                for x in range(11):
                    if x ==3 or x==7:
                        temp.append("|")
                    elif self.board[counter][counter2] == "0":
                        temp.append("~")#change blank spaces in board
                        counter2 += 1
                    else:
                        temp.append(self.board[counter][counter2])
                        counter2 +=1
                print("".join(map(str,temp)))
                counter += 1
                
    #adding a number to the array
    def add_num(self):
        global input1
        numbers = ["0","1","2","3","4","5","6","7","8","9"]
        letters = ["A","B","C","D","E","F","G","H","I"]
        user_input = str(input("Please enter the number you want to enter, followed by the column and row that you want to input into. E.G. 8A1\n Or enter 0 enter  to make blank\n Or enter 'U' to undo: "))
        if user_input.upper() == "U":
            s.undo()
            return user_input
        elif user_input.upper() == "R":
            s.redo()
            return user_input
        
        input1 = list(user_input)
        input1[1].upper()
        """while board[int(column_dict[input1[1].upper()])-1][(int(input1[2]))-1] != "0":
            print(board[1-(int(column_dict[input1[1].upper()]))][1-(int(input1[2]))])
            input()
            print(int(column_dict[input1[1].upper()])-1)
            print(int(input1[2])-1)
            user_input = str(input("This is one of the original boxes, please select a new box E.G. 8A1: "))
            input1 = list(user_input)
        while len(input1) is not 3:
            user_input = str(input("Please re-enter the number you want to enter, followed by the column and row that you want to input into. E.G. 8A1: "))
            input1 = list(user_input)
        while input1[0] not in numbers:
            number = str(input("Please enter a valid number to input between 0-9: "))
            input1[0] = number
        while input1[1].upper() not in letters:
            letter = str(input("Please enter a valid column between A and I: "))
            input[1] = letter.upper()
        while input1[2] not in numbers:
            number = str(input("Please enter a valid row between 1-9: "))
            input1[2] = number
            #get column to reference to dictionary in order to append the user_board array
            """
        input1[1] = column_dict[input1[1].upper()]
        previous_num.push(self.board[int(input1[2])-1][int(input1[1])-1])
        self.board[int(input1[2])-1][int(input1[1])-1] = input1[0]#bug: changed from +1 to -1
        

    #Checking if the board is filled
    def box_filled(self,user_board):
        for i in range(9):
            for x in range(9):
                if user_board[i][x] == "0":
                    return False
        return True

    #Check that the rows are correct
    def row_check(self,user_board):
        for i in range(9):
            temp = []
            for x in range(9):
                if user_board[i][x] in temp:
                    return False
                else:
                    temp.append(user_board[i][x])
        return True

    #Check that the columns are correct
    def column_check(self,user_board):
        for i in range(9):
            temp = []
            for x in range(9):
                if user_board[x][i] in temp:
                    return False
                else:
                    temp.append(user_board[x][i])
        return True

    #Check that each 3x3 box is correct
    def box_check(self,user_board):
        row = 1
        column = 1
        while True:
            temp = []
            #My inner Ethan Hunt
            if column == 1:
                if row == 1:
                    for i in range(3):#rows
                        for x in range(3):#columns
                            if user_board[i][x] in temp:
                                return False
                                break
                            else:
                                temp.append(user_board[i][x])
                elif row == 2:
                    for i in range(3,6):#rows
                        for x in range(3):#columns
                            if user_board[i][x] in temp:
                                return False
                                break
                            else:
                                temp.append(user_board[i][x])
                else:
                    for i in range(6,9):#rows
                        for x in range(3):#columns
                            if user_board[i][x] in temp:
                                return False
                                break
                            else:
                                temp.append(user_board[i][x])
                        
            elif column == 2:
                if row == 1:
                    for i in range(3):
                        for x in range(3,6):
                            if user_board[i][x] in temp:
                                return False
                                break
                            else:
                                temp.append(user_board[i][x])
                elif row == 2:
                    for i in range(3,6):
                        for x in range(3,6):
                            if user_board[i][x] in temp:
                                return False
                                break
                            else:
                                temp.append(user_board[i][x])
                else:
                    for i in range(6,9):
                        for x in range(3,6):
                            if user_board[i][x] in temp:
                                return False
                                break
                            else:
                                temp.append(user_board[i][x])
                    
            else:
                if row == 1:
                    for i in range(3):
                        for x in range(6,9):
                            if user_board[i][x] in temp:
                                return False
                                break
                            else:
                                temp.append(user_board[i][x])
                elif row == 2:
                    for i in range(3,6):
                        for x in range(6,9):
                            if user_board[i][x] in temp:
                                return False
                                break
                            else:
                                temp.append(user_board[i][x])
                else:
                    for i in range(6,9):
                        for x in range(6,9):
                            if user_board[i][x] in temp:
                                return False
                                break
                            else:
                                temp.append(user_board[i][x])
                    
            if column == 3 and row != 3:
                column = 1
                row += 1
            elif column != 3:
                column += 1
            else:
                return True
                break

    def create_stacks(self):
        global stack_num
        global stack_row
        global stack_column
        global previous_num
        global redo_num
        global redo_row
        global redo_column
        global redo_previous_num
        stack_num = Stack(9)
        stack_row = Stack(9)
        stack_column = Stack(9)
        previous_num = Stack(9)
        redo_num = Stack(9)
        redo_row = Stack(9)
        redo_column = Stack(9)
        redo_previous_num = Stack(9)
        
                             
    def record_changes(self,num,row,col):
        stack_num.push(num)
        stack_row.push(row)
        stack_column.push(col)
        print(stack_num.s)
        print(stack_row.s)
        print(stack_column.s)
        print("\n")
        stack_num.ps()
        stack_row.ps()
        stack_column.ps()

    #almost completely useless
    def concat_str(self, column, number, row):
        user_input = (number + column + row)
        return user_input
    

     def undo(self):
        if stack_num.empty == True:
            return
        previous_number = previous_num.pop()
        print("prev_num", previous_number)
        number = stack_num.pop()
        print("number", number)
        column = stack_column.pop()
        print("column", column)
        row = stack_row.pop()
        print("row", row)
        updated_board[int(b.row)][int(b.col)] = previous_number
        b.canvas.delete("all")
        b.draw_board()
        b.input_numbers(updated_board,original_board)
        #self.redo_changes(number, column, row)

    def redo_changes(self, number, column, row):
        redo_num.push(number)
        redo_row.push(row)
        redo_column.push(column)

    def redo(self):
        number = redo_num.pop()
        column = redo_column.pop()
        row = redo_row.pop()
        if redo_num.empty == True:
            print("\nThere is nothing to redo\n")
            return
        user_input = self.concat_str(column, number, row)
        input1 = list(user_input)
        self.board[int(input1[2])-1][int(input1[1])-1] = str(input1[0])

        
class Stack:
    def __init__(self,size):
        self.size = size
        self.s = [0 for x in range(size)]
        self.sp = 0
        self.full = False
        self.empty = True
        self.counter = 0

        
    def ps(self):
        print("Stack: ")
        for x in range(self.counter, self.sp):
            if int(self.s[x]) > 0:
                print(x, "  ", self.s[x])


    def push(self, num):
        if self.sp == self.size:
            self.full_stack()
            print("run")
            
        print(num)    
        self.s[self.sp] = num
        print(num)
        self.sp += 1
        self.empty = False

    def pop(self):
        if self.sp == self.counter:
            self.empty = True
        else:
            self.sp -= 1
            return self.s[self.sp]

    def full_stack(self):
        self.s[0] = 0
        self.sp -= 1
        for x in range(1, self.size):
            self.temp = self.s[x]
            self.s[x-1] = self.temp
      
 
#Function that does all the checks 
def checks(board):
    filled = s.box_filled(board) 
    row = s.row_check(board)
    column = s.column_check(board)
    box = s.box_check(board)
    if filled == True:
        if row == True:
            if column == True:
                if box == True:
                    return True
                    
                else:
                     print("\nThere is a box wrong")
                     return False
                    #There is a box wrong
            else:
                print("\nThere are 2 or more of the same number in a column")
                return False
                    #There is a column wrong
        else:
            print("\nThere are 2 or more of the same number in a row")
            return False
    else:
        return False
                

"""
def main():
    global board
    global s
    board = read_board()
    original_board = board
    s = Sudoku_board(board,file_num)
    s.create_stacks()
    s.print_board()
    s.add_num()
    check = checks(board)
    s.record_changes()
    while check == False:
        s.print_board()
        user_input = s.add_num()
        check = checks(board)
        if user_input != "U":
            s.record_changes()
        
    print("Congratulations, You have completed the Sudoku")

"""

def main_help():
    m.menu.destroy()
    global h
    h = help()
    h.make_page()
    
def menu_main():
    global m
    m = menu()
    m.title()
    m.buttons()

def menu_main_board():
    b.root.destroy()
    global m
    m = menu()
    m.title()
    m.buttons()

def menu_main_help():
    h.help1.destroy()
    global m
    m = menu()
    m.title()
    m.buttons()

def main():
    m.menu.destroy()
    global updated_board
    global original_board
    global s
    global b
    b = boardUI()
    b.draw_board()
    updated_board = read_board()
    original_board = get_board(file)
    s = Sudoku_board(updated_board,file_num)
    s.create_stacks()
    b.input_numbers(updated_board,original_board)
    b.input_buttons()
    check = checks(updated_board)
    if check == False:
        b.root.bind("<Button-1>", b.cell_clicked)
        b.root.mainloop()
    else:
        b.victory()
        
menu_main()

#undo and redo - FIX - 0 doesnt go into the stacks not sure why
#if cell clicked isnt 0 make row and column nothing

        


                        
