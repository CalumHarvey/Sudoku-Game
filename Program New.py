import random
from tkinter import *
import math

hint_board = []
ran = False
sec = 0
hint_pressed = False
clockstop = None
initial = True
completed = None



column_dict = {"A":"1", "B":"2", "C":"3", "D":"4", "E":"5", "F":"6", "G":"7", "H":"8", "I":"9"}


class boardUI: #Board UI object
    def __init__(self):
        self.root = Tk()
        w = 540
        h = 620
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.canvas = Canvas(self.root,height=480,width=500, highlightthickness=0)
        self.canvas.pack(fill=BOTH, side=TOP, padx=20, pady=20)
        self.root.resizable(width=False, height=False)
        self.margin = 20
        self.box_size = 450/9
        self.num = "0"
        self.col = None
        self.row = None

    def draw_board(self): #Creates the board
        thick_line = False
    
        for x in range(10):
            if x % 3 == 0:
                line_colour = "black"
                thick_line = 3
                extra = 1
            else:
                line_colour = "grey"
                thick_line = 1
                extra = 0
    
            self.canvas.create_line(self.margin-extra, self.margin + x * 500/10, 470+extra, self.margin + x * 500/10, fill=line_colour, width=thick_line)
            self.canvas.create_line(self.margin + x * 500/10, self.margin, self.margin + x * 500/10, 470, fill=line_colour, width=thick_line)


    def input_numbers(self,board,origin_board): #Puts the numbers into the board 
        global hint_pressed
        global initial
        global superhints
        x = 0
        y = 0
        number = None
        text_colour = None
        for z in range(9):
            for i in range(9):
                if board[z][i] is not "0":
                    number = updated_board[z][i]
                    x = self.margin + i * self.box_size + self.box_size/2
                    y = self.margin + z * self.box_size + self.box_size/2

                    
                    if initial == False:
                        s_hints = s.super_hints(z,i)

                    if origin_board[z][i] == "0":
                        text_colour = "blue"

                    if original_board[z][i] == updated_board[z][i]:
                        text_colour = "black"
                    
                    elif hint_pressed == True and board[z][i] != solution_board[z][i]:
                        text_colour = "red"
                        
                    if initial == False:
                        if superhints == "True" and s_hints == True:
                            text_colour = "red"
                    
                    
                self.canvas.create_text(x,y,text=number, fill=text_colour, font=("Ariel",16))
        hint_pressed = False
        initial = False



    def input_buttons(self):
            multiplier = 45.8
            add = 38
            w = 5
            self.button0 = Button(self.root,text=" ",width=w,relief=GROOVE,command=lambda:self.num0())
            self.button0.place(x=38, y = 515)
            self.button1 = Button(self.root,text="1",width=w,relief=GROOVE,command=lambda:self.num1())
            self.button1.place(x=multiplier+add, y = 515)
            self.button2 = Button(self.root,text="2",width=w,relief=GROOVE,command=lambda:self.num2())
            self.button2.place(x=multiplier*2+add,y=515)
            self.button3 = Button(self.root,text="3",width=w,relief=GROOVE,command=lambda:self.num3())
            self.button3.place(x=multiplier*3+add,y=515)
            self.button4 = Button(self.root,text="4",width=w,relief=GROOVE,command=lambda:self.num4())
            self.button4.place(x=multiplier*4+add, y=515)
            self.button5 = Button(self.root,text="5",width=w,relief=GROOVE,command=lambda:self.num5())
            self.button5.place(x=multiplier*5+add, y=515)
            self.button6 = Button(self.root,text="6",width=w,relief=GROOVE,command=lambda:self.num6())
            self.button6.place(x=multiplier*6+add, y=515)
            self.button7 = Button(self.root,text="7",width=w,relief=GROOVE,command=lambda:self.num7())
            self.button7.place(x=multiplier*7+add, y=515)
            self.button8 = Button(self.root,text="8",width=w,relief=GROOVE,command=lambda:self.num8())
            self.button8.place(x=multiplier*8+add, y=515)
            self.button9 = Button(self.root,text="9",width=w,relief=GROOVE,command=lambda:self.num9())
            self.button9.place(x=multiplier*9+add, y=515)
            self.undo = Button(self.root, text="Undo", width=w,relief=GROOVE,command= lambda: s.undo())
            self.undo.place(x=multiplier*4+add, y=550)
            self.redo = Button(self.root, text="Redo", width=w,relief=GROOVE, command= lambda: s.redo())
            self.redo.place(x=multiplier*5+add, y=550)
            if hints_active == "True":
                self.hint = Button(self.root, text="Check", width=w,relief=GROOVE,command= lambda: s.hint())
                self.hint.place(x=multiplier*7+add, y=550)
            back = Button(self.root,text="Back to Main Menu", width=15, relief=GROOVE,command=menu_main_board)
            back.place(x=50,y=575)


    def num0(self):
        if ran == False:
            return
        elif original_board[self.row][self.col] != "0":
            return
        self.test()
        self.num = "0"
        self.add_number()
        self.new_board()

    def num1(self):
        if ran == False:
            return
        elif original_board[self.row][self.col] != "0":
            return
        self.test()
        self.num = "1"
        self.add_number()
        self.new_board()

    def num2(self):
        if ran == False:
            return
        elif original_board[self.row][self.col] != "0":
            return
        self.test()
        self.num = "2"
        self.add_number()
        self.new_board()

    def num3(self):
        if ran == False:
            return
        elif original_board[self.row][self.col] != "0":
            return
        self.test()
        self.num = "3"
        self.add_number()
        self.new_board()

    def num4(self):
        if ran == False:
            return
        elif original_board[self.row][self.col] != "0":
            return
        self.test()
        self.num = "4"
        self.add_number()
        self.new_board()

    def num5(self):
        if ran == False:
            return
        elif original_board[self.row][self.col] != "0":
            return
        self.test()
        self.num = "5"
        self.add_number()
        self.new_board()

    def num6(self):
        if ran == False:
            return
        elif original_board[self.row][self.col] != "0":
            return
        self.test()
        self.num = "6"
        self.add_number()
        self.new_board()

    def num7(self):
        if ran == False:
            return
        elif original_board[self.row][self.col] != "0":
            return
        self.test()
        self.num = "7"
        self.add_number()
        self.new_board()

    def num8(self):
        if ran == False:
            return
        elif original_board[self.row][self.col] != "0":
            return
        self.test()
        self.num = "8"
        self.add_number()
        self.new_board()

    def num9(self):
        if ran == False:
            return
        elif original_board[self.row][self.col] != "0":
            return
        self.test()
        self.num = "9"
        self.add_number()
        self.new_board()

    def test(self):
        #print("Row: ", self.row)
        #print("Col: ", self.col)
        prev_row = self.row
        prev_col = self.col

        
    def cell_clicked(self,event):
        global ran
        if completed == True:
            return
        self.canvas.focus_set()
        if event.x > 19 and event.x < 466 and event.y > 18 and event.y < 466:

            ran = True

            self.canvas.delete("outline")

            row = math.floor((event.y-20)/50)
            col = math.floor((event.x-20)/50)

            self.row = int(row)
            self.col = int(col)


            self.canvas.create_rectangle(20+(50*col),20+(50*row),20+(50*col)+50,20+(50*row)+50,outline="red",tags="outline",width=3)


    def new_board(self):
        global check
        check = checks(updated_board)
        s.record_changes(self.num,self.row,self.col)
        self.canvas.delete("all")
        if check == False:
            self.draw_board()
            self.input_numbers(updated_board,original_board)
            self.canvas.create_rectangle(20+(50*self.col),20+(50*self.row),20+(50*self.col)+50,20+(50*self.row)+50,outline="red",tags="outline",width=3)
        else:
            self.victory()

    
    
    def add_number(self):
        previous_num.push(updated_board[self.row][self.col])
        updated_board[int(self.row)][int(self.col)] = self.num

    def delete_board(self):
        self.canvas.delete()
        self.button0.place_forget()
        self.button1.place_forget()
        self.button2.place_forget()
        self.button3.place_forget()
        self.button4.place_forget()
        self.button5.place_forget()
        self.button6.place_forget()
        self.button7.place_forget()
        self.button8.place_forget()
        self.button9.place_forget()
        self.undo.place_forget()
        self.redo.place_forget()
        if hints_active == True:
            self.hint.place_forget()

    def add_to_leaderboard(self,e,add_leaderboard):
        f = open("leaderboard.txt", "a")
        name = e.get()
        if len(name) > 8:
            f.close()
            e = Entry(self.root)
            e.place(x=270,y=257)
            error = Label(self.root, text="Make it less than 8 characters",font=("Comic Sans MS",12), fg="Red")
            error.place(x=100,y=310)
            add_leaderboard.destroy()
            add_leaderboard = Button(self.root, relief=GROOVE, text="Submit",command=lambda: self.add_to_leaderboard(e,add_leaderboard))
            add_leaderboard.place(x=350,y=350)
        elif len(name) < 1:
            f.close()
            e = Entry(self.root)
            e.place(x=270,y=257)
            error = Label(self.root, text="You must input something",font=("Comic Sans MS",12), fg="Red")
            error.place(x=100,y=310)
            add_leaderboard.destroy()
            add_leaderboard = Button(self.root, relief=GROOVE, text="Submit",command=lambda: self.add_to_leaderboard(e,add_leaderboard))
            add_leaderboard.place(x=350,y=350)

        else:
            input_leaderboard = (str(name) + "," + str(sec) + "," + str(difficulty) + "\n")
            f.write(input_leaderboard)
            f.close()
            confirmation = Label(self.root, text="Your name has been entered into the leaderboard", font=("Comic Sans MS",12))
            confirmation.place(x=80,y=350)
            add_leaderboard.place_forget()
        

    def victory(self):
        global clockstop
        global completed
        completed = True
        clockstop = True
        self.delete_board()
        if hints_active == True:
            self.hint.place_forget()
        self.canvas.create_text(250, 200, text="Congrats", font=("Comic Sans MS",14))
        
        enter_name = Label(self.root, text="Please enter your name:",font=("Comic Sans MS",12))
        max_characters = Label(self.root, text="Max characters 8", font=("Comic Sans MS",12))
        max_characters.place(x=80,y=280)
        e = Entry(self.root)
        enter_name.place(x=80,y=250)
        e.place(x=270,y=257)

        if superhints == "True":
            label = Label(self.root, text="You cannot enter the leaderboard if cheats are enabled",font=("Comic Sans MS",12))
            label.place(x=80,y=300)
        else:
            add_leaderboard = Button(self.root, relief=GROOVE, text="Submit",command=lambda: self.add_to_leaderboard(e,add_leaderboard))
            add_leaderboard.place(x=350,y=350)
            

            
def choose_difficulty():
    choose = Tk()
    w = 400
    h = 200
    ws = choose.winfo_screenwidth()
    hs = choose.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    choose.geometry('%dx%d+%d+%d' % (w, h, x, y))
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
    diff4 = Button(choose, text="Test", width=7, relief=GROOVE, command= lambda: diff_test(choose))
    diff4.place(x=170, y=150)
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
    difficulty = 3
    done = True
    choose.destroy()
    main()

def diff_test(choose):
    global difficulty
    difficulty = 4
    done = True
    choose.destroy()
    main()


def clock():
    global sec
    global clockstop
    clockstop = False
    sec = 0
    def tick():
        global clockstop
        global sec
        if clockstop == True:
            return

        else:
            sec += 1
            time['text'] = sec
            time.after(1000, tick)
            if sec > 9 and sec < 98: #if sec is 2 digits then move the "s" over to make room for it
                seconds_label.place(x=295,y=10)

            if sec > 99 and sec < 998: #if sec is 3 digits then move the "s" over to make room for it
                seconds_label.place(x=300,y=10)
            
            elif sec > 999: #if sec is 4 digits then move the "s" over to make room for it, this is precautionary 
                seconds_label.place(x=305,y=10)

    time = Label(b.root, fg='black')
    time.place(x=278,y=10)
    timer_label = Label(b.root, text="Timer:")
    timer_label.place(x=238, y=10)
    seconds_label = Label(b.root, text="s")
    seconds_label.place(x=287,y=10)

    #setting up the positions for the timer that it initializes with
    
    tick()

def secondstominutes(secs):
        mins = int(secs)/60
        mins = math.floor(mins)
        #seconds = secs % 60
        seconds = int(secs) - (int(secs) // 60 * 60)
        concat = str(mins) + ":" + str(seconds)
        return concat 



class menu:
    def __init__(self):
        self.menu = Tk()
        w = 500
        h = 500
        ws = self.menu.winfo_screenwidth()
        hs = self.menu.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.menu.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.menu.resizable(width=False, height=False)
        self.frame = Frame(self.menu, height=500, width=500)
        self.frame.pack(side=TOP, fill=BOTH)

    def title(self):
        title = Label(self.menu, text="Sudoku", font=("Ariel", 50),fg="blue")
        title.place(x=135, y=50)

    def buttons(self):
        play = Button(self.frame, text="Play", width=14,height=3,relief=GROOVE,command= lambda: choose_difficulty())
        play.place(x=115, y=175)
        leaderboard = Button(self.frame, text="Leaderboard", width=14, height=3,relief=GROOVE, command= lambda: main_leaderboard())
        leaderboard.place(x=285, y=175)
        settings = Button(self.frame, text="Settings", width=14, height=3,relief=GROOVE, command= lambda: main_settings())
        settings.place(x=115,y=300)
        help1 = Button(self.frame, text="Rules and Help", width=14, height=3,relief=GROOVE,command= lambda: main_help())
        help1.place(x=285,y=300)
        quit_button = Button(self.frame, text="Quit", width=6, relief=GROOVE, command=lambda: end())
        quit_button.place(x=410, y=440)

        


class help2:
    def __init__(self):
        self.help1 = Tk()
        self.help1.resizable(width=False, height=False)
        self.frame = Frame(self.help1, height=500, width=700)
        self.frame.pack(side=TOP, fill=BOTH)
        w = 700
        h = 500
        ws = self.help1.winfo_screenwidth()
        hs = self.help1.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.help1.geometry('%dx%d+%d+%d' % (w, h, x, y))

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


class settings: #Settings Window object
    def __init__(self):
        self.settings = Tk()
        w = 500
        h = 500
        ws = self.settings.winfo_screenwidth()
        hs = self.settings.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.settings.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.settings.resizable(width=False, height=False)
        self.frame = Frame(self.settings, height=500, width=500)
        self.frame.pack(side=TOP, fill=BOTH)
        settings_title = Label(self.frame, text="Settings", font=("Ariel", 20))
        settings_title.place(x=190,y=50)
        self.done = False

    def buttons(self):
        global superhints
        global warning
        if self.done == False:
            if hints_active == "True":
                hint_message = Label(self.frame, text="Currently check are: enabled", font=("Ariel",12),wraplength=300)
            else:
                hint_message = Label(self.frame, text="Currently check are: disabled", font=("Ariel",12),wraplength=300)
                
            hints_on = Button(self.frame,text="On", width=6, relief=GROOVE, command=lambda: self.hints_on(hint_message))
            hints_off = Button(self.frame,text="Off", width=6, relief=GROOVE, command=lambda: self.hints_off(hint_message))
            hints = Label(self.frame, text="Check On or Off:", font=("Ariel",14),wraplength=300)
            hints.place(x=100, y=115)
            hint_message.place(x=100, y=145)
        
            hints_on.place(x=250,y=117)
            hints_off.place(x=300,y=117)

            stacklength_setting = Label(self.frame, text="Length of Undo and Redo:",font=("Ariel",14),wraplength=300)
            stacklength_setting.place(x=100,y=190)
            
            
            length1 = Button(self.frame, text="10", width=6, relief=GROOVE,command=lambda:self.change1(cur_length))
            length2 = Button(self.frame, text="15", width=6, relief=GROOVE,command=lambda:self.change2(cur_length))
            length3 = Button(self.frame, text="20", width=6, relief=GROOVE,command=lambda:self.change3(cur_length))
            length4 = Button(self.frame, text="25", width=6, relief=GROOVE,command=lambda:self.change4(cur_length))

            cur_length = Label(self.frame, text="Current Length is:"+str(stacklength), font=("Ariel",12),wraplength=300)
            cur_length.place(x=100, y=260)

            length1.place(x=100,y=230)
            length2.place(x=150,y=230)
            length3.place(x=200,y=230)
            length4.place(x=250,y=230)

            super_hints_label = Label(self.frame, text="Cheats:",font=("Ariel",14),wraplength=300)
            super_hints_label.place(x=100,y=305)

            s_hints_on = Button(self.frame, text="On", width=6, relief=GROOVE,command=lambda:self.super_hints_on(super_hint_message))
            s_hints_off = Button(self.frame, text="Off", width=6, relief=GROOVE,command=lambda:self.super_hints_off(super_hint_message))
            s_hints_on.place(x=175,y=307)
            s_hints_off.place(x=225,y=307)

            if superhints == "True":
                super_hint_message = Label(self.frame, text="Currently cheats are: enabled",font=("Ariel",12),wraplength=300)
                warning = Label(self.frame, text="Warning: Your cannot be in the leaderboard with this setting enabled.",font=("Ariel",10),wraplength=300,fg="red")
                warning.place(x=100, y=360)
            else:
                super_hint_message = Label(self.frame, text="Currently cheats are: disabled",font=("Ariel",12),wraplength=300)
            super_hint_message.place(x=100, y=335)

            help_hint = Button(self.frame, text="?",width=3, relief=GROOVE,command=lambda: self.help_hints())
            help_length = Button(self.frame, text="?",width=3, relief=GROOVE,command=lambda: self.help_length())
            help_cheat = Button(self.frame, text="?",width=3, relief=GROOVE, command=lambda: self.help_cheat())

            help_hint.place(x=400,y=115)
            help_length.place(x=400,y=190)
            help_cheat.place(x=400,y=305)

            clear_leaderboard = Button(self.frame, text="Clear Leaderboard", relief=GROOVE, command= lambda: self.clear_leaderboard())
            clear_leaderboard.place(x=350,y=425)
          
        
            back = Button(self.frame, text="Back to Main Menu", width=15, relief=GROOVE,command= lambda: menu_main_settings())
            back.place(x=50,y=400)

    def clear_leaderboard(self):
        f = open("leaderboard.txt", "w+")
        f.close()


    def change1(self,cur_length):
        global stacklength
        stacklength = 10
        self.write_stacklength()
        cur_length.destroy()
        cur_length = Label(self.frame, text="Current Length is: 10", font=("Ariel",12),wraplength=300)
        cur_length.place(x=100, y=260)

    def change2(self,cur_length):
        global stacklength
        stacklength = 15
        self.write_stacklength()
        cur_length.destroy()
        cur_length = Label(self.frame, text="Current Length is: 15", font=("Ariel",12),wraplength=300)
        cur_length.place(x=100, y=260)

    def change3(self,cur_length):
        global stacklength
        stacklength = 20
        self.write_stacklength()
        cur_length.destroy()
        cur_length = Label(self.frame, text="Current Length is: 20", font=("Ariel",12),wraplength=300)
        cur_length.place(x=100, y=260)

    def change4(self,cur_length):
        global stacklength
        stacklength = 25
        self.write_stacklength()
        cur_length.destroy()
        cur_length = Label(self.frame, text="Current Length is: 25", font=("Ariel",12),wraplength=300)
        cur_length.place(x=100, y=260)
        

    def hints_on(self,hint_message):
        global hints_active
        self.done = True
        hints_active = "True"
        hint_message.destroy()
        hint_message_on = Label(self.frame, text="Currently hints are: enabled ", font=("Ariel",12),wraplength=300)
        hint_message_on.place(x=100, y=145)
        self.write_settings()

    def hints_off(self,hint_message):
        global hints_active
        self.done = True
        hints_active = "False"
        hint_message.destroy()
        hint_message_off = Label(self.frame, text="Currently hints are: disabled", font=("Ariel",12),wraplength=300)
        hint_message_off.place(x=100, y=145)
        self.write_settings()

    def super_hints_on(self,super_hints_message):
        global superhints
        global warning
        superhints = "True"
        super_hints_message.destroy()
        super_hints_message = Label(self.frame, text="Currently cheats are: enabled ", font=("Ariel",12),wraplength=300)
        super_hints_message.place(x=100, y=335)
        warning = Label(self.frame, text="Warning: Your cannot be in the leaderboard with this setting enabled.",font=("Ariel",10),wraplength=300,fg="red")
        warning.place(x=100, y=360)
        self.write_superhints()

    def super_hints_off(self,super_hints_message):
        global superhints
        superhints = "False"
        super_hints_message.destroy()
        warning.destroy()
        super_hints_message = Label(self.frame, text="Currently cheats are: disabled ", font=("Ariel",12),wraplength=300)
        super_hints_message.place(x=100, y=335)
        self.write_superhints()

    def help_hints(self):
        help_hint = Tk()
        w = 200
        h = 100
        ws = help_hint.winfo_screenwidth()
        hs = help_hint.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        help_hint.geometry('%dx%d+%d+%d' % (w, h, x, y))
        help_hint.resizable(width=False, height=False)
        help_hint.geometry("200x100")
        label = Label(help_hint, text="Allows you to press a button that shows all the answers that are wrong on the board in red",font=("Ariel",10),wraplength=200)
        label.pack()

    def help_length(self):
        help_hint = Tk()
        w = 200
        h = 100
        ws = help_hint.winfo_screenwidth()
        hs = help_hint.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        help_hint.geometry('%dx%d+%d+%d' % (w, h, x, y))
        help_hint.resizable(width=False, height=False)
        help_hint.geometry("200x100")
        label = Label(help_hint, text="Changes the number of times that you can undo and redo in the sudoku board",font=("Ariel",10),wraplength=200)
        label.pack()

    def help_cheat(self):
        help_hint = Tk()
        w = 200
        h = 100
        ws = help_hint.winfo_screenwidth()
        hs = help_hint.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        help_hint.geometry('%dx%d+%d+%d' % (w, h, x, y))
        help_hint.resizable(width=False, height=False)
        help_hint.geometry("200x100")
        label = Label(help_hint, text="Allows you to see whenever you make a mistake by highlighting it in red if it is wrong",font=("Ariel",10),wraplength=200)
        label.pack()


     
    def write_stacklength(self):
        f = open("stacklength.txt", "w")
        f.write(str(stacklength))
        f.close()
        
    def write_settings(self):
        f = open("hints.txt", "w")
        if hints_active == "True":
            f.write("True")
        else:
            f.write("False")
        f.close()
            
    def write_superhints(self):
        f = open("superhints.txt", "w")
        if superhints == "True":
            f.write("True")
        else:
            f.write("False")
        f.close()


class leaderboard():
    def __init__(self):
        self.leaderboard = Tk()
        w = 700
        h = 700
        ws = self.leaderboard.winfo_screenwidth()
        hs = self.leaderboard.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.leaderboard.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.leaderboard.resizable(width=False, height=False)
        self.frame = Frame(self.leaderboard, height=700, width=500)
        self.frame.pack(side=LEFT, fill=BOTH)


    def get_leaderboard(self):
        f = open("leaderboard.txt", "r")
        raw_leaderboard = f.read()
        num_lines = 0
        temp1 = raw_leaderboard.split()
        num_lines = len(temp1)
        board1 = []
        for x in range(num_lines):
            temp = temp1[x].strip("\n")
            board1.append(temp)

        board2 = []
        for x in range(num_lines):
            board3 = board1[x].split(",")
            board2.append(board3)
        f.close()
        return board2

    def sort_difficulty(self,sortdifficulty):
        eligiblerecords = []
        sorted_difficulty = []
        for x in range(len(time_sort_list)):
            if int(time_sort_list[x][2]) == int(sortdifficulty):
                sorted_difficulty.append(time_sort_list[x])
        return sorted_difficulty


    def sort_time(self,unsorted):
        numbers = []
        index = []
        for y in range(len(unsorted)):
            numbers.append(unsorted[y][1])
            index.append(y)

        for i in range(len(unsorted)-1,0,-1):
            for x in range(i):
                if int(numbers[x]) > int(numbers[x+1]):
                    temp = numbers[x]
                    numbers[x] = numbers[x+1]
                    numbers[x+1] = temp

                    temp = index[x]
                    index[x] = index[x+1]
                    index[x+1] = temp

        sorted_list = []
        for n in range(len(unsorted)):
            sorted_list.append(unsorted[index[n]])
                    
        return sorted_list

    def sort_timedesc(self,unsorted):
        numbers = []
        index = []
        for y in range(len(unsorted)):
            numbers.append(unsorted[y][1])
            index.append(y)

        for i in range(len(unsorted)-1,0,-1):
            for x in range(i):
                if int(numbers[x]) < int(numbers[x+1]):
                    temp = numbers[x]
                    numbers[x] = numbers[x+1]
                    numbers[x+1] = temp

                    temp = index[x]
                    index[x] = index[x+1]
                    index[x+1] = temp

        sorted_list = []
        for n in range(len(unsorted)):
            sorted_list.append(unsorted[index[n]])
                    
        return sorted_list



    def create_leaderboard(self):
        global time_sort_list
        sorted_list = self.sort_time(basic_leaderboard)
        self.frame.destroy()
        self.frame = Frame(self.leaderboard, height=700, width=500)
        self.frame.pack(side=LEFT, fill=BOTH)
        self.input_leaderboard(sorted_list)
        time_sort_list = sorted_list

    def input_leaderboard(self,sorted_list):
        multiplier = 30
        settings_title = Label(self.leaderboard, text="Leaderboard", font=("Ariel", 20))
        settings_title.place(x=250,y=50)
        position = Label(self.leaderboard, text = "Position", font=("Ariel", 14), bg="Cyan",width=6,pady=5)
        position.place(x=75, y=120)
        name = Label(self.leaderboard, text = "Name", font=("Ariel", 14))
        name.place(x=175, y=120)
        time_title = Label(self.leaderboard, text = "Time", font=("Ariel", 14))
        time_title.place(x=270, y=120)
        diff_title = Label(self.leaderboard, text = "Difficulty", font=("Ariel", 14))
        diff_title.place(x=350, y=120)
        if len(basic_leaderboard) > 15:
            leaderboard_length = 15
        else:
            leaderboard_length = len(sorted_list)
        for x in range(leaderboard_length):
            name = str(sorted_list[x][0])
            time = secondstominutes(sorted_list[x][1])
            if sorted_list[x][2] == "1":
                difficulty1 = "Easy"
            elif sorted_list[x][2] == "2":
                difficulty1 = "Medium"
            else:
                difficulty1 = "Hard"
            text1 = Label(self.frame, text= str(x+1), font=("Ariel", 14), bg="Cyan",width=6, pady=5 )
            text1.place(x=75, y=150+(multiplier*x))
            text2 = Label(self.frame, text= name, font=("Ariel", 14))
            text2.place(x=175, y=150+(multiplier*x))
            text3 = Label(self.frame, text= str(time), font=("Ariel", 14))
            text3.place(x=270, y=150+(multiplier*x))
            text4 = Label(self.frame, text= str(difficulty1), font=("Ariel", 14))
            text4.place(x=350, y=150+(multiplier*x))
        self.buttons()

    def buttons(self):
        var = 473
        back = Button(self.leaderboard, text="Back to Main Menu", width=15, relief=GROOVE,command= lambda: menu_main_leaderboard())
        back.place(x=50,y=650)
        diff_settings = Label(self.leaderboard, text="Sort By",font=("Ariel", 14))
        diff_settings.place(x=475,y=150)
        l1 = Label(self.leaderboard, text="Difficulty:",font=("Ariel", 14))
        l1.place(x=475,y=200)
        easy = Button(self.leaderboard, text="Easy", width=6, relief=GROOVE, command=lambda: self.sort_easy())
        easy.place(x=var,y=250)
        medium = Button(self.leaderboard, text="Medium", width=6, relief=GROOVE, command=lambda: self.sort_medium())
        medium.place(x=var+50,y=250)
        hard = Button(self.leaderboard, text="Hard", width=6, relief=GROOVE, command=lambda: self.sort_hard())
        hard.place(x=var+100,y=250)
        l2 = Label(self.leaderboard, text="Time:",font=("Ariel", 14))
        l2.place(x=475,y=300)
        sortbytimedown = Button(self.leaderboard, text="Low to High", relief=GROOVE, command=lambda: self.create_leaderboard())
        sortbytimedown.place(x=475, y=350)
        sortbytimeup = Button(self.leaderboard, text="High to Low", relief=GROOVE, command=lambda: self.sort_desc())
        sortbytimeup.place(x=548, y=350)
        l3 = Label(self.leaderboard, text="Name: ", font=("Ariel", 14))
        l3.place(x=475,y=400)
        sort_name = Button(self.leaderboard, text="Alphabetical", relief=GROOVE, command=lambda: self.sort_name())
        sort_name.place(x=480,y=450)
        l4 = Label(self.leaderboard, text="Search: ",font=("Ariel", 12))
        l4.place(x=440,y=497)
        searched_name = Entry(self.leaderboard)
        searched_name.place(x=500,y=500)
        submit = Button(self.leaderboard, text="Submit", relief=GROOVE, command=lambda: self.search_name(searched_name))
        submit.place(x=575,y=540)

    def search_name(self,button):
        names = []
        name = button.get()
        for x in range(len(basic_leaderboard)):
            if str(name) == str(basic_leaderboard[x][0]):
                names.append(basic_leaderboard[x])
        self.frame.destroy()
        self.frame = Frame(self.leaderboard, height=700, width=500)
        self.frame.pack(side=LEFT, fill=BOTH)
        self.input_leaderboard(names) 

        
    def sort_easy(self):
        sorted_list = self.sort_difficulty(1)
        if len(sorted_list) == 0:
            error = Label(self.frame, text="There is nothing in that leaderboard please select a \ndifferent option", font=("Ariel", 12))
            error.place(x=100,y=550)
        else:
            fully_sorted = self.sort_time(sorted_list)
            self.frame.destroy()
            self.frame = Frame(self.leaderboard, height=700, width=500)
            self.frame.pack(side=LEFT, fill=BOTH)
            self.input_leaderboard(fully_sorted)

    def sort_medium(self):
        sorted_list = self.sort_difficulty(2)
        if len(sorted_list) == 0:
            error = Label(self.frame, text="There is nothing in that leaderboard please select a \ndifferent option", font=("Ariel", 12))
            error.place(x=100,y=550)
        else:
            fully_sorted = self.sort_time(sorted_list)
            self.frame.destroy()
            self.frame = Frame(self.leaderboard, height=700, width=500)
            self.frame.pack(side=LEFT, fill=BOTH)
            self.input_leaderboard(fully_sorted)           

    def sort_hard(self):
        sorted_list = self.sort_difficulty(3)
        if len(sorted_list) == 0:
            error = Label(self.frame, text="There is nothing in that leaderboard please select a \ndifferent option", font=("Ariel", 12))
            error.place(x=100,y=550)
        else:
            fully_sorted = self.sort_time(sorted_list)
            self.frame.destroy()
            self.frame = Frame(self.leaderboard, height=700, width=500)
            self.frame.pack(side=LEFT, fill=BOTH)
            self.input_leaderboard(fully_sorted)

    def sort_desc(self):
        self.frame.destroy()
        self.frame = Frame(self.leaderboard, height=700, width=500)
        self.frame.pack(side=LEFT, fill=BOTH)
        sorted_list = self.sort_timedesc(basic_leaderboard)
        self.input_leaderboard(sorted_list)

    def sort_name(self):
        sorted_list = basic_leaderboard
        sorted_list.sort()
        self.frame.destroy()
        self.frame = Frame(self.leaderboard, height=700, width=500)
        self.frame.pack(side=LEFT, fill=BOTH)
        self.input_leaderboard(sorted_list)
        
'''
END OF INTERFACE!
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
        file = (str(file_num) + ".txt")
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

def initialise_hints():
    global hints_active
    f = open("hints.txt", "r")
    hints_active = (f.read())
    f.close()

def initialise_stacklength():
    global stacklength
    f = open("stacklength.txt", "r")
    stacklength = int(f.read())
    f.close()

def initialise_superhints():
    global superhints
    f = open("superhints.txt", "r")
    superhints = (f.read())
    f.close()


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

    def hint(self):
        global hint_pressed
        hint_pressed = True
        hint_board = [["0" for x in range(9)]for x in range(9)]
        for x in range(9):
            for i in range(9):
                if updated_board[x][i] != "0" and updated_board[x][i] != solution_board[x][i]:
                    hint_board[x][i] = "1"
        b.canvas.delete("all")
        b.draw_board()
        b.input_numbers(updated_board,original_board)

    def super_hints(self,x,y):
        if updated_board[int(x)][int(y)] != solution_board[int(x)][int(y)]:
            return True

    
    def create_stacks(self):
        global stack_num
        global stack_row
        global stack_column
        global previous_num
        global redo_num
        global redo_row
        global redo_column
        global redo_previous_num
        global stacklength
        stack_num = Stack(stacklength)
        stack_row = Stack(stacklength)
        stack_column = Stack(stacklength)
        previous_num = Stack(stacklength)
        redo_num = Stack(stacklength)
        redo_row = Stack(stacklength)
        redo_column = Stack(stacklength)
        redo_previous_num = Stack(stacklength)
        
                             
    def record_changes(self,num,row,col):
        stack_num.push(num)
        stack_row.push(row)
        stack_column.push(col)


    #almost completely useless
    def concat_str(self, column, number, row):
        user_input = (number + column + row)
        return user_input
    
    
    def undo(self):

        previous_number = previous_num.pop()
        number = stack_num.pop()
        row = stack_row.pop()
        col = stack_column.pop()
        if stack_num.empty == True:
            return
        self.redo_changes(number, col, row)

        updated_board[int(row)][int(col)] = previous_number
    
        b.canvas.delete("all")
        b.draw_board()
        b.input_numbers(updated_board,original_board)
        

    def redo_changes(self, number, column, row):
        redo_num.push(number)
        redo_row.push(row)
        redo_column.push(column)

    def redo(self):
        number = redo_num.pop()
        column = redo_column.pop()
        row = redo_row.pop()
        if redo_num.empty == True:
            return
        
        updated_board[int(row)][int(column)] = number
    
        b.canvas.delete("all")
        b.draw_board()
        b.input_numbers(updated_board,original_board)

        self.record_changes(number,row,column)


        
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
            
        self.s[self.sp] = num
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
                    return False
                    #There is a box wrong
            else:
                return False
                    #There is a column wrong
        else:
            return False
                #There is a row wrong
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
def main_settings():
    m.menu.destroy()
    global setting
    setting = settings()
    setting.buttons()

def main_leaderboard():
    m.menu.destroy()
    global l
    global basic_leaderboard
    l = leaderboard()
    basic_leaderboard = l.get_leaderboard()
    l.create_leaderboard()
    leader = l.sort_time(basic_leaderboard)

    
def main_help():
    m.menu.destroy()
    global h
    h = help2()
    h.make_page()
    
def menu_main():
    global m
    initialise_hints()
    initialise_stacklength()
    initialise_superhints()
    m = menu() 
    m.title()
    m.buttons()

def menu_main_board():        
    b.root.destroy()
    global m
    m = menu()
    m.title()
    m.buttons()

def menu_main_leaderboard():
    l.leaderboard.destroy()
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

def menu_main_settings():
    setting.settings.destroy()
    global m
    m = menu()
    m.title()
    m.buttons()

def end():
    m.menu.destroy()


def main():
    m.menu.destroy()
    global solution_board
    global updated_board
    global original_board
    global s
    global b
    global completed
    completed = False
    b = boardUI()
    b.draw_board()
    updated_board = read_board()
    original_board = get_board(file)
    solution = (str(file_num) + "solution.txt")
    solution_board = get_board(solution)
    s = Sudoku_board(updated_board,file_num)
    s.create_stacks()
    b.input_numbers(updated_board,original_board)
    b.input_buttons()
    clock()
    check = checks(updated_board)
    b.root.bind("<Button-1>", b.cell_clicked)
    b.root.mainloop()
        
menu_main()

#previous_num is used for the number that is in the previous spot to the one being changed (usually 0) in order to be able to undo the number back to what it was originally


#To DO:
#Leaderboard - either sql integration in python or a dictionary or a file
#Board - extra hint: checking if a move is correct after it is taken.
#Backgrounds to the sudoku board
#Base case for the clock function
#Timer doesnt stop after ending a game

                        
