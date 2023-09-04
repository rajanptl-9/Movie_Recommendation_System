from tkinter import *
import mlcode
root = Tk()

root.geometry("420x420")
root.title("Movie_Recommendation_System")

def get_input():
    user_input = entry.get()
    sorted_similar_movies, df_movies = mlcode.search_movie(user_input)
    i = 1
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = df_movies[df_movies.index == index]['title'].values[0]

        if i <= 30:
            listbox.insert(i, str(i) + " -> " + title_from_index)
            i = i + 1

def clear_search():
    entry.delete(0, END)
    listbox.delete(0, END)

input_frame = Frame(root)
input_frame.pack(pady=10)

label = Label(input_frame, text="Movie:")
label.pack(side=LEFT)

# Create an Entry widget for input
entry = Entry(input_frame, width=30)
entry.pack(pady=10)

button_frame = Frame(root)
button_frame.pack()

# Create a button that calls the get_input function when clicked
button = Button(button_frame, text="Search Movie", command=get_input)
button.pack(side=LEFT, padx=5)

clear_button = Button(button_frame, text="Clear Search", command=clear_search)
clear_button.pack(side=LEFT, padx=5)

listbox_frame = Frame(root)
listbox_frame.pack()

lbl = Label(listbox_frame, text="Recommeded Movies : ", pady=10)

listbox = Listbox(root, width=40, height=17)

lbl.pack()
listbox.pack()

root.mainloop()  