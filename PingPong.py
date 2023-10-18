import tkinter as tk
import random

# Defining the initial parameters of the game
WIDTH, HEIGHT = 600, 400
BALL_SPEED = 5
PADDLE_SPEED = 10
ball_dx, ball_dy = 0, 0

# Variables for storing mouse coordinates

mouse_x = 0

# Variable for the account
right_score = 0

# Feature to start a new game
def new_game():
    global ball_dx, ball_dy, right_score
    right_score = 0
    canvas.delete("all")
    ball_dx = random.choice((1, -1)) * BALL_SPEED
    ball_dy = random.choice((1, -1)) * BALL_SPEED
    canvas.create_rectangle(WIDTH / 2 - 40, HEIGHT - 20, WIDTH / 2 + 40, HEIGHT - 10, fill="white", tags="paddle")
    canvas.create_oval(WIDTH / 2 - 15, HEIGHT / 2 - 15, WIDTH / 2 + 15, HEIGHT / 2 + 15, fill="white", tags="ball")
    canvas.create_text(WIDTH / 2 + 50, 30, text=str(right_score), fill="white", font=("Arial", 24), tags="right_score")
    canvas.bind("<Motion>", move_paddle)
    canvas.after(1000, move_ball)

# Functions for Ball Movement
def move_ball():
    global ball_dx, ball_dy, right_score
    ball_x, ball_y, ball_x2, ball_y2 = canvas.coords("ball")


    if ball_y <= 0:
        ball_dy = -ball_dy


    if ball_y2 >= HEIGHT:
        new_game()
        return


    if ball_x <= 0 or ball_x2 >= WIDTH:
        ball_dx = -ball_dx


    paddle = canvas.coords("paddle")
    if ball_y2 >= HEIGHT - 10 and paddle[0] < ball_x < paddle[2]:
        ball_dy = -ball_dy
        right_score += 1
        canvas.itemconfig("right_score", text=str(right_score))

    canvas.move("ball", ball_dx, ball_dy)
    canvas.after(10, move_ball)

# Function to move the paddle with the mouse
def move_paddle(event):
    global mouse_x
    mouse_x = event.x
    canvas.coords("paddle", mouse_x - 40, HEIGHT - 20, mouse_x + 40, HEIGHT - 10)

# Creating the Main Window
window = tk.Tk()
window.title("Pong Game")

# How to Create a Canvas to Display the Game
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Starting a new game
new_game()

# Run the main tkinter loop
window.mainloop()
