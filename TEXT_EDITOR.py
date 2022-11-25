from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import os, sys
import win32print
import win32api
root = Tk()
root.title('Text Editor')
root.geometry("1200x680")

# Set variable for Open filename
global open_status_name
open_status_name = False

global selected
selected = False
# Creating New File Func
def new_file():
    # Delete Prev Text
    my_text.delete("1.0", END)
    # Update Status Bar
    root.title('New File')
    status_bar.config(text="New File.....")

    global open_status_name
    open_status_name = False

# Open File Func
def open_file():
    # Delete Prev Text
    my_text.delete("1.0", END)
    
    # Grab Filename
    text_file = filedialog.askopenfilename(initialdir="D:\5th Sem\SE\project", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    # Check to see if there is a file name
    if text_file:
        # Make file name global so we can access it later
        global open_status_name
        open_status_name = text_file



    # Update Status bars
    name = text_file
    status_bar.config(text=f'{name}        ')
    name = name.replace("D:\5th Sem\SE\project/", "")
    root.title(f'{name}')

    # Open the file
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    # Add file to text box
    my_text.insert(END, stuff)
    # Close the opened file
    text_file.close()

# Save as File
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="D:\5th Sem\SE\project", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        # Update Status bars
        name = text_file
        status_bar.config(text=f'Saved: {name}        ')
        name = name.replace("D:\5th Sem\SE\project/", "")
        root.title(f'{name}')

        # Save the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        # Close the file
        text_file.close()

# Save File
def save_file():
    global open_status_name
    if open_status_name:
        # Save the file
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        # Close the file
        text_file.close()

        status_bar.config(text=f'Saved: {open_status_name}        ')
        name=open_status_name
        name=name.replace( "D:\5th Sem\SE\project/" ,"")
        root.title(f'{name} - TextPad!')
    else:
        save_as_file()

# Cut Text
def cut_text(e) :
        global selected
        # check to see if keyboard shortcut used
        if e:
            selected= root.clipboard_get()
        else:
            if my_text.selection_get():
                # Grab selected text from text box
	            selected=my_text.selection_get()
	            # Delete Selected Text from text box
	            my_text.delete("sel.first", "sel.last")

            root.clipboard_clear()
            root.clipboard_append(selected)

# Copy Text
def copy_text(e):
    global selected
    # check to see if we used keyboard short
    if e:
	    selected=root.clipboard_get()

    if my_text.selection_get():
	    # Grab selected text from text box
	    selected = my_text.selection_get()
    root.clipboard_clear()
    root.clipboard_append(selected)

# Paste Text
def paste_text(e):
    global selected
    #Check to see if keyboard shutcut used
    if e:
	    selected=root.clipboard_get()
    else:
	    if selected :
		    position=my_text.index(INSERT)
		    my_text. insert (position, selected)

# Bold Text
def bold_it():
    # Configure a font
    bold_font= font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    #configure a tag
    my_text.tag_configure("bold",font=bold_font)

    # define current tags
    current_tags= my_text.tag_names("sel.first")

    # if statement to see if tag has been set
    if "bold" in current_tags:
        my_text.tag_remove("bold","sel.first", "sel.last")
    else:
        my_text.tag_add("bold","sel.first", "sel.last")

# Italics Text
def italics_it():
    # Configure a font
    italics_font= font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")

    #configure a tag
    my_text.tag_configure("italic",font=italics_font)

    # define current tags
    current_tags= my_text.tag_names("sel.first")

    # if statement to see if tag has been set
    if "italic" in current_tags:
        my_text.tag_remove("italic","sel.first", "sel.last")
    else:
        my_text.tag_add("italic","sel.first", "sel.last")

#Change Selected Text Color
def text_color():
    #Pick a color
    my_color = colorchooser.askcolor()[1]
    if my_color:
         #Create our font
        color_font= font.Font(my_text, my_text.cget("font"))

        #configure a tag
        my_text.tag_configure("colored",font=color_font, foreground=my_color)

        # define current tags
        current_tags= my_text.tag_names("sel.first")

    # if statement to see if tag has been set
    if "colored" in current_tags:
        my_text.tag_remove("colored","sel.first", "sel.last")
    else:
        my_text.tag_add("italic","sel.first", "sel.last")

#Change bg color
def bg_color():
        my_color = colorchooser.askcolor()[1]
        if my_color:
            my_text.config(bg=my_color)

#Change All Text Color
def all_text_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(fg=my_color)
#Print File Function
def print_file():
    #printer_name = win32print.GetDefaultPrinter()
    #status_bar.config(text=printer_name)
    #file_to_print
    # Grab Filename
    file_to_print = filedialog.askopenfilename(initialdir="D:\5th Sem\SE\project", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))

    if file_to_print:
        win32api.ShellExecute(0,"print", file_to_print, None, ".", 0)

#Select ALL Text
def select_all(e):
    #Add sel tag to select all text
    my_text.tag_add('sel', '1.0', 'end')

#Clear all Text
def clear_all():
    my_text.delete(1.0, END)



# Create a toolbar frame
toolbar_frame=Frame(root)
toolbar_frame.pack(fill=X)

# Creating Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create Scrollbar for the text box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Horizontal Scrollbar
hor_scroll =Scrollbar(my_frame, orient= 'horizontal')
hor_scroll.pack(side=BOTTOM,fill=X)

# Creating a Text Box
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set,wrap="none",xscrollcommand=hor_scroll.set)
my_text.pack()

# Configuring our scrollbar
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

# Creating Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Adding File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Print File", command=print_file)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Adding Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut",command=lambda: cut_text(False),accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copy",command=lambda: copy_text(False),accelerator="(Ctrl+c)")
edit_menu.add_command(label="Paste      ",command=lambda: paste_text(False),accelerator="(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo",command=my_text.edit_undo,accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo",command=my_text.edit_redo,accelerator="(Ctrl+y)")
edit_menu.add_separator()
edit_menu.add_command(label="Select All",command=lambda: select_all(True),accelerator="(Ctrl+a)")
edit_menu.add_command(label="Clear",command=clear_all,accelerator="(Ctrl+y)")

#Add Color Menu
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
color_menu.add_command(label="Change Selected Text",command=text_color)
color_menu.add_command(label="All text",command=all_text_color)
color_menu.add_command(label="Background",command=bg_color)

# Adding Status bar at the bottom of the app
status_bar = Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=15)

# Edit Bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
#Select Binding
root.bind('Control-A', select_all)
root.bind('Control-a', select_all)

# Create Button

# Bold Button

bold_button= Button(toolbar_frame,text="Bold",command=bold_it)
bold_button.grid(row=0,column=0, sticky=W,padx=5)

# Italics Button

italics_button= Button(toolbar_frame,text="Italics",command=italics_it)
italics_button.grid(row=0, column=1,padx=5)

# Undo/ Redo Buttons

undo_button= Button(toolbar_frame,text="Undo",command=my_text.edit_undo)
undo_button.grid(row=0, column=2,padx=5)
redo_button= Button(toolbar_frame,text="Redo",command=my_text.edit_redo)
redo_button.grid(row=0, column=3,padx=5)

#Text Color
color_text_button = Button(toolbar_frame, text="Text Color", command=text_color)
color_text_button.grid(row=0, column=4, padx=5)

root.mainloop()
