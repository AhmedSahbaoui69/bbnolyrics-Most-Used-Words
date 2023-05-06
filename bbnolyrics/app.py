import tkinter as tk
from tkinter import ttk
import pandas as pd

# initiate window
window = tk.Tk()
window.title("Bbno$ Word Count")

# configure theme
style = ttk.Style()
style.theme_use('clam')

# display bbnolyrics image
img = tk.PhotoImage(file="Jupyter_Notebook/img.png")
bbnolyrics = ttk.Label(window, image=img).pack(pady=15)

# add "enter word" label
enter_label = ttk.Label(window, text="Enter a word:", font=('Arial', 12)).pack(pady=5)

# add textbox
textbox = ttk.Entry(window, width=20, font=('Arial', 12))
textbox.pack(pady=10)

def get_count():
    # import data
    df = pd.read_csv("Jupyter_Notebook/word_count_data/word_counts.csv")
    
    # check for count
    word = textbox.get().lower()
    count = df.loc[df['Word'] == word, 'Count'].values
    
    # display the count 
    if len(count) > 0:
        count_label.config(text=f"The count for '{word}' is {count[0]}.")
    else:
        count_label.config(text=f"'{word}' was not found.")
        
# add search button
search_butt = ttk.Button(window, text="Search", command=get_count)
search_butt.pack(pady=10)

# add label to display count
count_label = ttk.Label(window, text="")
count_label.pack(pady=5)

# disclaimer
disclaimer_label = ttk.Label(window, text="*Disclaimer : Lyrics of featured artists were also included.", foreground="red").pack()

# set window size 
window.geometry('690x300')
window.resizable(False, False)

# run loop
window.mainloop()
