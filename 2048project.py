import tkinter as tk
import random
import keyboard as key

#run when start the game to show the first window
def first_time_open():
    heading_Text.pack(padx=20, pady=20)
    First_Frame.pack(side="top",expand=True, fill="both")
    start_bt.pack(side="bottom", pady="50")
    

#command for the play button
def start_game():
    #making 4x4 matrix use in game 
    global matrix
    matrix = []
    for i in range(4):
         matrix.append([0] * 4)

    First_Frame.pack_forget()
    game_over_frame.pack_forget()
    Second_Frame.pack(expand=True, fill="both")
    heading.grid(row=0, column=1, columnspan = 2)
    show_tiles()


#game over window
def game_over():
     print("end game activate")
     Second_Frame.pack_forget()
     game_over_text.pack(side="top", pady="50")
     replay_button.pack(side="bottom", pady="50")
     game_over_frame.pack(expand=True,fill="both")


#Using loop to make the Lable widget for the game
def show_tiles():
    for row in range(4):
        for collum in range(4):
            Second_Frame.columnconfigure(row, weight=1)
            Second_Frame.rowconfigure(row+1, weight=1)
            label = tk.Label(Second_Frame, text="0", font=("Comic Sans MS", 24), width=4, height=2, borderwidth=2, relief="solid", background="pink")
            if matrix[row][collum] == 0:
                label.config(text="")
            else:label.config(text= matrix[row][collum])
            label.grid(row=row+1, column=collum, padx=5, pady=5, sticky="NS"+"WE")


def add_new_tiles(matrix):
    avaiable_number = [2,4]
    #choose random tile in 4x4 matrix
    row = random.randint(0,3)
    collum = random.randint(0,3)

    #check if the tile is taken or not
    while matrix[row][collum] != 0:
        row = random.randint(0,3)
        collum = random.randint(0,3)
    
    #adding 2 or 4 into the choosen tile
    matrix[row][collum] = random.choice(avaiable_number)


def Check_game_state(matrix):
    for row in range(4):
        for collum in range(4):
            if matrix[row][collum] == 2048:
                 return "You won the game"

    for row in range(20):
        for collum in range(4):
             if matrix[row][collum] == 0:
                  return "game not over"
             
    #check if there are any movable row
    for row in range(3):    
        for collum in range(3):
            if matrix[row][collum] == matrix[row][collum+1] or matrix[row][collum] == matrix[row+1][collum]:
                 return "game not over"
            
    return "Game over"



def merge(direction): #move all the number to each other then merge them together in certain direction
    changed = False
    if direction.upper() == "DOWN":
        for collum in range(4):
            for row in range(4):
                if row > 0 and matrix[row-1][collum] != 0 and matrix[row][collum] == 0:
                    matrix[row][collum] = matrix[row-1][collum]
                    matrix[row-1][collum] = 0
                    changed = True

                if row < 3 and matrix[row][collum] == matrix[row+1][collum]:
                    matrix[row+1][collum] += matrix[row][collum]
                    matrix[row][collum] = 0
                    changed = True

        for collum in range(4):
            for row in range(4):
                    if row < 3 and matrix[row+1][collum] == 0 and matrix[row][collum] != 0:
                        matrix[row+1][collum] = matrix[row][collum]
                        matrix[row][collum] = 0
                        changed = True


    if direction.upper() == "UP":
        matrix.reverse()
        for collum in range(4):
            for row in range(4):
                if row > 0 and matrix[row-1][collum] != 0 and matrix[row][collum] == 0:
                    matrix[row][collum] = matrix[row-1][collum]
                    matrix[row-1][collum] = 0
                    changed = True

                if row < 3 and matrix[row][collum] == matrix[row+1][collum]:
                    matrix[row+1][collum] += matrix[row][collum]
                    matrix[row][collum] = 0
                    changed = True

        for collum in range(4):
            for row in range(4):
                    if row < 3 and matrix[row+1][collum] == 0 and matrix[row][collum] != 0:
                        matrix[row+1][collum] = matrix[row][collum]
                        matrix[row][collum] = 0
                        changed = True
        matrix.reverse()


    if direction.upper() == "RIGHT":
        for row in range(4):
            for collum in range(4):
                    if collum > 0 and matrix[row][collum-1] != 0 and matrix[row][collum] == 0:
                        matrix[row][collum] = matrix[row][collum-1]
                        matrix[row][collum-1] = 0
                        changed = True

                    if collum < 3 and matrix[row][collum+1] == matrix[row][collum]:
                        matrix[row][collum+1] += matrix[row][collum]
                        matrix[row][collum] = 0
                        changed = True

        for row in range(4):
            for collum in range(4):
                    if collum < 3 and matrix[row][collum+1] == 0 and matrix[row][collum] != 0:
                        matrix[row][collum+1] = matrix[row][collum]
                        matrix[row][collum] = 0
                        changed = True

    if direction.upper() == "LEFT":
        for row in range(4):
             matrix[row].reverse()
        for row in range(4):
            for collum in range(4):
                    if collum > 0 and matrix[row][collum-1] != 0 and matrix[row][collum] == 0:
                        matrix[row][collum] = matrix[row][collum-1]
                        matrix[row][collum-1] = 0
                        changed = True

                    if collum < 3 and matrix[row][collum+1] == matrix[row][collum]:
                        matrix[row][collum+1] += matrix[row][collum]
                        matrix[row][collum] = 0
                        changed = True

        for row in range(4):
            for collum in range(4):
                    if collum < 3 and matrix[row][collum+1] == 0 and matrix[row][collum] != 0:
                        matrix[row][collum+1] = matrix[row][collum]
                        matrix[row][collum] = 0
                        changed = True

        for row in range(4):
             matrix[row].reverse()

    if changed == True: #if anything changed add 2 or 4 block
        add_new_tiles(matrix)
        show_tiles()

    if Check_game_state(matrix) != "game not over" : 
        game_over()


#move function two move number all over the place
def move_up():
    merge("UP")
    print("move up", matrix)
    print(Check_game_state(matrix))

def move_down():
    merge("DOWN")
    print("move down", matrix)
    print(Check_game_state(matrix))

def move_right():
    merge("RIGHT")
    print("move right", matrix)
    print(Check_game_state(matrix))

def move_left():
    merge("LEFT")
    print("move left", matrix)
    print(Check_game_state(matrix))

#hotkeys for WASD
key.add_hotkey('w', move_up)
key.add_hotkey('s', move_down)
key.add_hotkey('d', move_right)
key.add_hotkey('a', move_left)
#hotkeys for arrows
key.add_hotkey('up', move_up)
key.add_hotkey('down', move_down)
key.add_hotkey('right', move_right)
key.add_hotkey('left', move_left)

#the root of all the widget
root = tk.Tk()
root.title("")
root.geometry('400x400')

#frames 
First_Frame = tk.Frame(root, background="Orange")
Second_Frame = tk.Frame(root, background="Yellow")
game_over_frame = tk.Frame(root, background="Orange", width=100)

#labels
heading_Text = tk.Label(First_Frame, text= "Welcome to the game",       
                bg="lightblue",                   
                bd=3,                  
                font=("Comic Sans MS", 25, "bold"),   
                fg="red",
                padx=15,pady=15,)
heading = tk.Label(Second_Frame, text="2048", font=("Comic Sans MS", 30, "bold"), background="Yellow")
game_over_text = tk.Label(game_over_frame, text="GAME OVER", font=("Comic Sans MS",40, "bold"), background="Orange")

#buttons
start_bt = tk.Button(First_Frame, text="Play",
                command=start_game,
                activebackground="Pink",
                activeforeground="White",
                bg="lightgray",
                cursor="hand2",
                disabledforeground="gray",
                font=("Comic Sans MS", 12),
                padx=10,
                pady=5,
                width=15)

replay_button = tk.Button(game_over_frame, text="Replay",
                command=start_game,
                activebackground="Pink",
                activeforeground="White",
                bg="lightgray",
                cursor="hand2",
                disabledforeground="gray",
                font=("Comic Sans MS", 12, "bold"),
                padx=10,
                pady=5,
                width=15)

# Execute Tkinter
first_time_open()
root.mainloop()