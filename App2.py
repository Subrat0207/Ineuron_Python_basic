# Importing Tkinter
import tkinter as tk

# Window Dimension and Title
window = tk.Tk()  # Window Start: Add below things :

window.title("My App")
window.geometry('800x800')


# ------FUNCTION----
def input_name():
    """
    Taking the Input whats user give in Entry box
    :return:  filename.pdf, filename.docx
    """
    entry = str(Entry1.get())
    print("ENMTRY", entry)
    return entry

def find_drive():
    """
    This function responsible for findings the existing drives names and return the same
    :return:
    list which contains Drive Names. e.g ['C:', 'D:']
    """

    import os.path
    dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    drives = []

    for d in dl:
        if os.path.exists(d + ':'):
            #print(str(d + ':'))
            drives.append(d + ':\\')

    # drives = [d for d in dl if os.path.exists ]
    return drives


def find_file(file_name_input, drive_names_list):
    """
    This function responsible for Searching the User Entered file in all Drives and returns the path
    :param file_name_input:  User Entry of file name to be searched : string
    :param drive_names_list: All logical drives present in the computer. list type
    :return: string : path of file if file is present or Warning message if that file is not present
    :retrun2: file_present_flag:bool : True : File Exists
    """
    file_path_list = []
    file_present_flag = False
    import os
    for drive in drive_names_list:
        for roots, dirs, files in os.walk(drive):
            for file_name in files:
                if file_name == file_name_input:
                    file_path_list.append(os.path.join(roots, file_name))
                    file_present_flag = True

    if len(file_path_list) == 0:
        #print(" Warning : no file found ")
        file_path_list.append("No Such files")

    return file_path_list, file_present_flag


def display_file_path():
    """
    This function just display the file path : Used by Tkinter Button
    :param file_path_list:  path of searched file or warning message
    :return: none
    """
    file_name_input = input_name()
    drive_names_list = find_drive()
    file_path_list, file_present_flag = find_file(file_name_input, drive_names_list)

    file_path_display = tk.Text(master=window, height=20, width=60)
    file_path_display.grid(column=0, row=5)
    if len(file_path_list) > 0:
        for file_path in file_path_list:
            file_path_display.insert(tk.END, file_path)
            file_path_display.insert(tk.END, '\n')

    else:
        file_path_display.insert(tk.END, file_path_list)


def file_merger():
    """
    This function returns the merger of similar files (present in different location) into one file
    :return: string path name
    """
    file_name_input = input_name()
    drive_names_list = find_drive()
    file_path_list,  file_present_flag = find_file(file_name_input, drive_names_list)
    file_path_display = tk.Text(master=window, height=20, width=60)
    file_path_display.grid(column=0, row=6)
    k_temp = 'c:\\temp.txt' # Hard coded Temp file
    if file_present_flag == True:
        if ('.txt' in file_name_input)  or ('.docx' in file_name_input):
            for file_name in file_path_list:
                with open(file_name) as f:
                    with open(k_temp, "a") as f1:
                        for line in f:
                            f1.write(line)

                    f1.close()
                f.close()
        else:
            k_temp = 'not a txt or Docx'
    else:
        k_temp = 'file not present'
    file_path_display.insert(tk.END, k_temp)
    return k_temp



#---------------------------------------------------------------------------------------------

# -----Label Information----
title = tk.Label(text=" **Welcome to my app2**")
title.grid(column=0, row=0)

# ------ Another Label----
title1 = tk.Label(text=' Please write the file name here')
title1.grid(column=0, row=1)

# ------ Entry field---
Entry1 = tk.Entry()
Entry1.grid(column=0, row=2)

# ----- Button 1 -----
button1 = tk.Button(text='SEARCH', command=display_file_path)
button1.grid(column=0, row=3)

# ----- Button 2 -----
button1 = tk.Button(text='MERGE', command=file_merger)
button1.grid(column=1, row=3)
window.mainloop()  # Window Stop :No need add anything
