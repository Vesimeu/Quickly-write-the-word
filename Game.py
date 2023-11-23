import tkinter as tk
from tkinter import ttk
import time

user_word = ""
start_time = 0
running = False
times = []

def set_word():
    global user_word
    user_word = word_entry.get().lower()
    word_label.config(text=f"Зафиксировано слово: {user_word}")

def start_training():
    global running
    running = True
    train_word()

def stop_training():
    global running
    running = False

def train_word():
    global start_time, user_word, running, times

    if running:
        if start_time == 0:
            start_time = time.time()
            result_label.config(text="")

        input_text = input_entry.get().lower()

        if input_text == user_word:
            end_time = time.time()
            time_taken = end_time - start_time
            times.append(time_taken)
            update_times_table()
            update_min_time()
            result_label.config(text=f"Поздравляю! Вы ввели слово '{user_word}' за {time_taken:.2f} секунд.")
            input_entry.delete(0, 'end')
            start_time = 0

        elif len(input_text) == len(user_word):
            result_label.config(text="Неправильно. Попробуйте ещё раз.")
            input_entry.delete(0, 'end')

        if running:
            root.after(100, train_word)

def update_times_table():
    for i in times_tree.get_children():
        times_tree.delete(i)
    for time_entry in times:
        times_tree.insert('', 'end', values=(f"{time_entry:.2f} секунд",))

def update_min_time():
    if times:
        min_time = min(times)
        min_time_label.config(text=f"Самое маленькое время: {min_time:.2f} секунд")
    else:
        min_time_label.config(text="Самое маленькое время: ")

def clear_times():
    global times
    times = []
    update_times_table()
    update_min_time()

root = tk.Tk()
root.title("Тренировка ввода слова")

word_label = tk.Label(root, text="Введите определённое слово для тренировки:")
word_label.pack()

word_entry = tk.Entry(root)
word_entry.pack()

set_word_button = tk.Button(root, text="Зафиксировать слово", command=set_word)
set_word_button.pack()

instruction_label = tk.Label(root, text="Тренируйтесь, вводя зафиксированное слово:")
instruction_label.pack()

input_entry = tk.Entry(root)
input_entry.pack()

train_button = tk.Button(root, text="Начать тренировку", command=start_training)
train_button.pack()

stop_button = tk.Button(root, text="Остановить тренировку", command=stop_training)
stop_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

times_tree = ttk.Treeview(root, columns=('Time'), show='headings')
times_tree.heading('Time', text='Время ввода слова')
times_tree.pack()

min_time_label = tk.Label(root, text="")
min_time_label.pack()

clear_button = tk.Button(root, text="Очистить таблицу", command=clear_times)
clear_button.pack()

root.mainloop()
