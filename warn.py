import tkinter as tk
from tkinter import font

def show_warning(game_title):
  main_view = tk.Tk()
  main_view.title("not the time to play.") 
  main_view.geometry("500x50")

  #これじゃ上手くいかない
  # my_font = tk.font.Font(main_view, family="Segoe UI", size=16)
  my_font = font.Font(main_view, family="Segoe UI", size=16)

  label = tk.Label(main_view, text="you must notice it's not the time to play " + game_title, font=my_font)
  label.pack()

  main_view.mainloop()