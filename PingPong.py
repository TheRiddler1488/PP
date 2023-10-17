import tkinter as tk
import random

# Определение начальных параметров игры
WIDTH, HEIGHT = 600, 400
BALL_SPEED = 5
PADDLE_SPEED = 10
ball_dx, ball_dy = 0, 0

# Переменные для хранения координат мыши
mouse_x = 0

# Переменная для счета
right_score = 0

# Функция для начала новой игры
def new_game():
    global ball_dx, ball_dy, right_score
    right_score = 0  # Сброс счета
    canvas.delete("all")
    ball_dx = random.choice((1, -1)) * BALL_SPEED
    ball_dy = random.choice((1, -1)) * BALL_SPEED
    canvas.create_rectangle(WIDTH / 2 - 40, HEIGHT - 20, WIDTH / 2 + 40, HEIGHT - 10, fill="white", tags="paddle")
    canvas.create_oval(WIDTH / 2 - 15, HEIGHT / 2 - 15, WIDTH / 2 + 15, HEIGHT / 2 + 15, fill="white", tags="ball")
    canvas.create_text(WIDTH / 2 + 50, 30, text=str(right_score), fill="white", font=("Arial", 24), tags="right_score")
    canvas.bind("<Motion>", move_paddle)
    canvas.after(1000, move_ball)

# Функции для движения мяча
def move_ball():
    global ball_dx, ball_dy, right_score
    ball_x, ball_y, ball_x2, ball_y2 = canvas.coords("ball")

    # Проверка столкновения с верхней границей
    if ball_y <= 0:
        ball_dy = -ball_dy

    # Проверка столкновения с нижней границей
    if ball_y2 >= HEIGHT:
        new_game()
        return

    # Проверка столкновения с боковыми границами
    if ball_x <= 0 or ball_x2 >= WIDTH:
        ball_dx = -ball_dx

    # Проверка столкновения с ракеткой
    paddle = canvas.coords("paddle")
    if ball_y2 >= HEIGHT - 10 and paddle[0] < ball_x < paddle[2]:
        ball_dy = -ball_dy
        right_score += 1
        canvas.itemconfig("right_score", text=str(right_score))

    canvas.move("ball", ball_dx, ball_dy)
    canvas.after(10, move_ball)

# Функция для движения ракетки с помощью мыши
def move_paddle(event):
    global mouse_x
    mouse_x = event.x
    canvas.coords("paddle", mouse_x - 40, HEIGHT - 20, mouse_x + 40, HEIGHT - 10)

# Создаем главное окно
window = tk.Tk()
window.title("Pong Game")

# Создаем холст для отображения игры
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Начинаем новую игру
new_game()

# Запускаем главный цикл tkinter
window.mainloop()
