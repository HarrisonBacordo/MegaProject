from tkinter import *
import tkinter.filedialog


def new_file():
    print("dummy")


def open_file():
    file = tkinter.filedialog.askopenfile(parent=root, mode='rb',
                                          title='Select a file!')  # opens window to request user to choose a file
    if file is not None:  # check that file variable isn't empty
        contents = file.read()  # puts contents of the file into contents variable
        text.insert('1.0', contents)  # inserts text into the text area
        file.close()  # close the file


def save_file():
    file = tkinter.filedialog.asksaveasfile(mode='w')   # opens window to ask user to to save file; in write mode
    if file is not None:
        data = text.get('1.0', END + '-1c')
        file.write(data)    # write data to the file
        file.close()


root = Tk()  # This initiates the the root as the tk window. like JFrame

text = Text(root)  # set text top parent root
scrollbar = Scrollbar(root)  # set scrollbar to root
menu = Menu(root)  # set menu to root

root.config(menu=menu)  # set this window's main menu to be menu
file_menu = Menu(menu)  # set file_menu to be the popup menu for the main menu
menu.add_cascade(label="File", menu=file_menu)  # adds a cascade menu under the label "file" to the menu.
file_menu.add_command(label="New Document",
                      command=new_file)  # adds a new button to the cascade menu, calls new_file on click
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_separator()  # adds a separator between cascade menu elements
file_menu.add_command(label="Exit", command=root.quit)

text.pack(side=LEFT, fill=Y)  # fit text to left side of the window, have it fill vertically
scrollbar.pack(side=RIGHT, fill=Y)  # fit scrollbar to right side of the window, have it fil l vertically
scrollbar.config(command=text.yview())  # configure the scroll bar to change the text's yview on use
text.config(yscrollcommand=scrollbar.set)  # configure the text area to change the scrollbar position on scroll

root.mainloop()  # initiate the loop to make it run
