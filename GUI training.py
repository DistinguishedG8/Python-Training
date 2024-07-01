
import customtkinter
import os
import csv

# -> Sets display style
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

# <*> TEST 1 - Grid <*>

# # -> Creates root, main display format
# root = customtkinter.CTk()
# root.geometry("800x550")
# root.grid_columnconfigure((0), weight=1)

# # -> test function
# def accept_action():

#     def show_FileFolders():
#         # -> Checks current directory and objects within
#         director = os.listdir()
#         dataFromFile = csv.reader(director, delimiter = ",")
        
#     # -> Displays folders and files
#         for steps in dataFromFile:
#             comeTogether = "".join(steps)
#             tab_view.add(comeTogether)

#     show_FileFolders()
#     print(" \n ")

# def show_tab():
#     steps = tab_view.get()
#     print(steps)


# # -> Master frame, ties in other elements
# frame = customtkinter.CTkFrame(master = root)
# frame.grid(row=0, column=0, pady = 20, padx = 60)

# # -> Main label header
# title_label = customtkinter.CTkLabel(master = frame, text = "File System", font = ("Calibri", 24))
# title_label.grid(row=1, column=1, pady = 12, padx = 10)

# # -> Main label header
# tab_view = customtkinter.CTkTabview(master = frame, width = 1, height = 1, command = show_tab)
# tab_view.grid(row=2, column=1, pady = 12, padx = 10, sticky = "ew")

# # -> Designed for user input
# entry_userEmail = customtkinter.CTkEntry(master = frame, placeholder_text = "email")
# entry_userEmail.grid(row=3, column=1, pady =(0,2), padx = (50,0), columnspan = 1, sticky = "w")

# # -> User states access mode
# entry_accessMode = customtkinter.CTkEntry(master = frame, placeholder_text = "Access Mode")
# entry_accessMode.grid(row=3, column=2, pady = (0,2), padx = (0,50), columnspan = 1, sticky = "w")

# entry_textBox = customtkinter.CTkTextbox(master = frame, width = 400, height = 100, font = ("Calibri", 12))
# entry_textBox.grid(row=5, column=1, pady = 12, padx = 10)

# # -> Checkbox for cloud selection
# checkbox = customtkinter.CTkCheckBox(master = frame, text = "Use Cloud Files")
# checkbox.grid(row=6, column=1, pady = 12, padx = 10)

# # -> Button for user login interaction
# accept_button = customtkinter.CTkButton(master = frame, text = "Accept", command = accept_action)
# accept_button.grid(row=7, column=1, pady = 12, padx = 10)

# # -> Error/Reader label, displays file and error details
# display_label = customtkinter.CTkLabel(master = frame, text = "", font = ("Calibri", 24))
# display_label.grid(row=8, column=1, pady = 12, padx = 10)

# root.mainloop()


# # <*> TEST 2 - pack & place <*>

# # -> Creates root, main display format
# place_root = customtkinter.CTk()
# place_root.geometry("800x550")

# # -> test function
# def accept_action():

#     def show_FileFolders():
#         # -> Checks current directory and objects within
#         director = os.listdir()
#         dataFromFile = csv.reader(director, delimiter = ",")
        
#     # -> Displays folders and files
#         for steps in dataFromFile:
#             comeTogether = "".join(steps)
#             tab_view.add(comeTogether)

#     show_FileFolders()
#     print(" \n ")

# def show_tab():
#     steps = tab_view.get()
#     print(steps)


# # -> Master frame, ties in other elements
# frame = customtkinter.CTkFrame(master = place_root, width = 800, height = 550)
# frame.pack(pady = 20, padx = 20)

# # -> Main label header
# title_label = customtkinter.CTkLabel(master = frame, text = "File System", font = ("Calibri", 24))
# title_label.place(relx=0.5, rely=0.1, anchor = "center")

# # -> Main label header
# tab_view = customtkinter.CTkTabview(master = frame, width = 1, height = 1, command = show_tab)
# tab_view.place(relx=0.5, rely=0.3, anchor = "center")

# # -> Designed for user input
# entry_userEmail = customtkinter.CTkEntry(master = frame, placeholder_text = "email")
# entry_userEmail.place(relx=0.5, rely=0.3, anchor = "center")

# # -> User states access mode
# entry_accessMode = customtkinter.CTkEntry(master = frame, placeholder_text = "Access Mode")
# entry_accessMode.place(relx=0.5, rely=0.4, anchor = "center")

# entry_textBox = customtkinter.CTkTextbox(master = frame, width = 400, height = 100, font = ("Calibri", 12))
# entry_textBox.place(relx=0.5, rely=0.6, anchor = "center")

# # -> Checkbox for cloud selection
# checkbox = customtkinter.CTkCheckBox(master = frame, text = "Use Cloud Files")
# checkbox.place(relx=0.5, rely=0.8, anchor = "center")

# # -> Button for user login interaction
# accept_button = customtkinter.CTkButton(master = frame, text = "Accept", command = accept_action)
# accept_button.place(relx=0.5, rely=0.9, anchor = "center")

# # -> Error/Reader label, displays file and error details
# display_label = customtkinter.CTkLabel(master = frame, text = "", font = ("Calibri", 24))
# display_label.place(relx=0.5, rely=1.1, anchor = "center")

# place_root.mainloop()

# <*> TEST 2 - pack & place <*>

# -> Creates root, main display format
pack_root = customtkinter.CTk()
pack_root.geometry("800x550")

# -> test function
def accept_action():

    def show_FileFolders():
        # -> Checks current directory and objects within
        director = os.listdir()
        dataFromFile = csv.reader(director, delimiter = ",")
        
    # -> Displays folders and files
        for steps in dataFromFile:
            comeTogether = "".join(steps)
            tab_view.add(comeTogether)

    show_FileFolders()
    print(" \n ")

def show_tab():
    steps = tab_view.get()
    print(steps)


# -> Master frame, ties in other elements
frame = customtkinter.CTkFrame(master = pack_root)
frame.pack(pady = 20, padx = 60)

# -> Main label header
title_label = customtkinter.CTkLabel(master = frame, text = "File System", font = ("Calibri", 24))
title_label.pack(pady = 10, padx = 10, anchor = "center")

# -> Main label header
tab_view = customtkinter.CTkTabview(master = frame, width = 1, height = 1, command = show_tab)
tab_view.pack(pady = 10, padx = 10, anchor = "center")

# -> Designed for user input
entry_userEmail = customtkinter.CTkEntry(master = frame, placeholder_text = "email")
entry_userEmail.pack(pady = 10, padx = 10, anchor = "center")

# -> User states access mode
entry_accessMode = customtkinter.CTkEntry(master = frame, placeholder_text = "Access Mode")
entry_accessMode.pack(pady = 10, padx = 10, anchor = "center")

entry_textBox = customtkinter.CTkTextbox(master = frame, width = 400, height = 100, font = ("Calibri", 12))
entry_textBox.pack(pady = 10, padx = 10, anchor = "center")

# -> Checkbox for cloud selection
checkbox = customtkinter.CTkCheckBox(master = frame, text = "Use Cloud Files")
checkbox.pack(pady = 10, padx = 10, anchor = "center")

# -> Button for user login interaction
accept_button = customtkinter.CTkButton(master = frame, text = "Accept", command = accept_action)
accept_button.pack(pady = 10, padx = 10, anchor = "center")

# -> Error/Reader label, displays file and error details
display_label = customtkinter.CTkLabel(master = frame, text = "", font = ("Calibri", 24))
display_label.pack(pady = 10, padx = 10, anchor = "center")

pack_root.mainloop()