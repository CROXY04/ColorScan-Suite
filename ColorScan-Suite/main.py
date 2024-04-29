import time
import tkinter as tk
import os
from PIL import ImageTk, Image


def openfile_picture(e):
    os.system(r"venv\Scripts\python.exe picture.py")

def webcam_function(e):
    os.system(r"venv\Scripts\python.exe webcam.py")

weekday_names_german = {
    "Monday": "Montag",
    "Tuesday": "Dienstag",
    "Wednesday": "Mittwoch",
    "Thursday": "Donnerstag",
    "Friday": "Freitag",
    "Saturday": "Samstag",
    "Sunday": "Sonntag"
}

month_names_german = {
    1: "Januar",
    2: "Februar",
    3: "März",
    4: "April",
    5: "Mai",
    6: "Juni",
    7: "Juli",
    8: "August",
    9: "Spetember",
    10: "Oktober",
    11: "November",
    12: "Dezember",
}

month_names_english = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "Spetember",
    10: "October",
    11: "November",
    12: "December",
}

date_names_english = {
    1: "1st",
    2: "2nd",
    3: "3rd",
    4: "4th",
    5: "5th",
    6: "6th",
    7: "7th",
    8: "8th",
    9: "9th",
    10: "10th",
    11: "11th",
    12: "12th",
    13: "13th",
    14: "14th",
    15: "15th",
    16: "16th",
    17: "17th",
    18: "18th",
    19: "19th",
    20: "20th",
    21: "21st",
    22: "22nd",
    23: "23rd",
    24: "24th",
    25: "25th",
    26: "26th",
    27: "27th",
    28: "28th",
    29: "29th",
    30: "30th",
    31: "31st",
}


#-----------------------------German package start---------------------#
def german_package(e):


    def webcam_function_german(e):
        webcam_window = tk.Toplevel(root)
        webcam_window.iconbitmap('icons/icon.ico')
        webcam_window.title("ColorScan - Webcam")
        webcam_window.minsize(530, 275)
        webcam_window.configure(bg=schrift_standard)
        # nav
        top_frame = tk.Frame(webcam_window, bg=standard_farbe)
        top_frame.pack(side="top", fill=tk.X)
        nav_name = tk.Label(top_frame, text="Farberkennung mit Webcam", bg=standard_farbe, font="Bahnschrift 30", fg="white", height=2)
        nav_name.pack(side="top")

        web_desc = tk.Label(webcam_window, text="Um das Programm zu öffnen, klicken Sie\n"
                                                 "auf Start. Klicken Sie auf die ESC-Taste,"
                                                 "\n um das Programm zu schließen",
                            bg=schrift_standard, font="Bahnschrift 17", fg="black",
                                height=4)
        web_desc.pack()
        start_button = tk.Label(webcam_window, text="Start", bg=standard_farbe, font="Bahschrift 20", fg=schrift_standard)
        start_button.pack(side='top')
        start_button.bind("<Button-1>", webcam_function)


    def picture_function_german(e):
        picture_window = tk.Toplevel(root)
        picture_window.iconbitmap('icons/icon.ico')
        picture_window.title("ColorScan - Bild")
        picture_window.minsize(490, 275)
        picture_window.configure(bg=schrift_standard)
        # nav
        top_frame = tk.Frame(picture_window, bg=standard_farbe)
        top_frame.pack(side="top", fill=tk.X)
        nav_name = tk.Label(top_frame, text="Farberkennung mit Bild", bg=standard_farbe, font="Bahnschrift 30", fg="white", height=2)
        nav_name.pack(side="top")

        pic_desc = tk.Label(picture_window, text="Um das Programm zu öffnen, klicken Sie\n"
                                                 "auf Start. Klicken Sie auf die ESC-Taste,"
                                                 "\n um das Programm zu schließen",
                            bg=schrift_standard, font="Bahnschrift 17", fg="black",
                                height=4)
        pic_desc.pack()
        start_button = tk.Label(picture_window, text="Start", bg=standard_farbe, font="Bahschrift 20", fg=schrift_standard)
        start_button.pack(side='top')
        start_button.bind("<Button-1>", openfile_picture)


    def impressum_german(e):
        impressum_window = tk.Toplevel(root)
        impressum_window.title("ColorScan - Impressum")
        impressum_window.iconbitmap('icons/icon.ico')
        impressum_window.minsize(400, 400)
        impressum_window.configure(bg=schrift_standard)
        # nav
        top_frame = tk.Frame(impressum_window, bg=standard_farbe)
        top_frame.pack(side="top", fill=tk.X)
        nav_name = tk.Label(top_frame, text="Impressum", bg=standard_farbe, font="Bahnschrift 30", fg="white", height=2)
        nav_name.pack(side="top")
        impressum_Angabe = tk.Label(impressum_window, text="ColorScan® 2022", bg=hintergrund, font="Bahnschrift 20",
                                    fg=standard_farbe, height=2)
        impressum_Angabe.pack()
        impressum_us = tk.Label(impressum_window, text="Entwickler", bg=hintergrund, font="Bahnschrift 17 bold", fg="black", height=2)
        impressum_us.pack()
        impressum_text = tk.Label(impressum_window, text="Chakresh Pechetti\nNishant Rostewitz\nSebastian Morawietz", bg=hintergrund,
                                  font="Bahnschrift 15", fg="black", height=3)
        impressum_text.pack()


    #colors
    standard_farbe= "#2f2f2f"
    schrift_standard = "#ff6620"
    hintergrund = schrift_standard

    root = tk.Tk()
    root.iconbitmap('icons/icon.ico')
    root.title("ColorScan")
    root.minsize(700, 575)

    top_frame = tk.Frame(root, bg=standard_farbe)
    top_frame.pack(side="top", fill=tk.X)
    title = tk.Label(top_frame, text='ColorScan - Ein Farberkenner', font="Bahnschrift 35" ,bg=standard_farbe,
                     fg=schrift_standard, height=2)
    title.pack(side="top")

    home_label1 = tk.Label(root, height=1)
    home_label1.pack()

    home_label2 = tk.Frame(root, height=3,  bg=schrift_standard)
    home_label2.pack(side="top", fill=tk.X)

    webcam_link = tk.Label(home_label2, text="Farberkennung mit\nWebcam", font="Bahnschrift 17",
                           bg= schrift_standard, fg=standard_farbe, height=3)
    webcam_link.pack(side='left', padx= 100)
    webcam_link.bind("<Button-1>", webcam_function_german)

    photo_link = tk.Label(home_label2, text="Farberkennung mit\nFoto", font="Bahnschrift 17",
                          bg =schrift_standard, fg=standard_farbe, height=3)
    photo_link.pack(side='left')
    photo_link.bind("<Button-1>", picture_function_german)

    home_label3 = tk.Label(root, height=1)
    home_label3.pack()

    home_label4 = tk.Label(root, height=3, bg=standard_farbe, font="Bahnschrift 17", fg=schrift_standard,
                           text="Diese Anwendung hilft dir, Farben aus Bildern oder von der\n"
                                " Webcam zu erkennen. Wir wollen die Farberkennung mit"
                                "\n einem Klick ermöglichen!")
    home_label4.pack(side="top", fill=tk.X)

    home_label5 = tk.Label(root, height=1)
    home_label5.pack()

    home_label6 = tk.Label(root, height=2, bg=schrift_standard, font="Bahnschrift 17", fg=standard_farbe, text="")
    home_label6.pack(side="top", fill=tk.X)


    def clock_german():
        day = time.strftime("%d")
        weekday = time.strftime("%A")
        month = time.strftime("%m")
        year = time.strftime("%Y")
        hour = time.strftime("%H")
        minute = time.strftime("%M")
        clock_label.config(text=weekday_names_german[weekday] + ", " + day + ". " + month_names_german[int(month)] + " " + year + " - " + hour + ":" + minute)
        clock_label.after(1, clock_german)
    clock_label = tk.Label(home_label6, text="", bg=schrift_standard, fg=standard_farbe, font="Bahnschrift 30", width=30)
    clock_label.pack(pady=30)
    clock_german()

    home_label7 = tk.Label(root, height=1 )
    home_label7.pack()

    bottom_frame = tk.Frame(root, bg=standard_farbe, height = 2)
    bottom_frame.pack(side='bottom', fill=tk.X)
    impressum_link = tk.Label(bottom_frame, text='Impressum', font="Bahnschrift 20" ,bg=standard_farbe,
                              fg=schrift_standard,height=2)
    impressum_link.pack(side="top")
    impressum_link.bind("<Button-1>", impressum_german)

    root.mainloop()
#----------------------------German package end--------------------------#



#----------------------------English package start-----------------------#

def english_package(e):


    def webcam_function_english(e):

        webcam_window = tk.Toplevel(root)
        webcam_window.iconbitmap('icons/icon.ico')
        webcam_window.title("ColorScan - Webcam")
        webcam_window.minsize(580, 265)
        webcam_window.configure(bg=schrift_standard)
        # nav
        top_frame = tk.Frame(webcam_window, bg=standard_farbe)
        top_frame.pack(side="top", fill=tk.X)
        nav_name = tk.Label(top_frame, text="Color recognition with webcam", bg=standard_farbe, font="Bahnschrift 30", fg="white", height=2)
        nav_name.pack(side="top")

        web_desc = tk.Label(webcam_window, text="To open the program click the start\n"
                                                 "button. To close the program click ESC.",
                            bg=schrift_standard, font="Bahnschrift 17", fg="black",
                                height=4)
        web_desc.pack()
        start_button = tk.Label(webcam_window, text="Start", bg=standard_farbe, font="Bahschrift 20", fg=schrift_standard)
        start_button.pack(side='top')
        start_button.bind("<Button-1>", webcam_function)


    def picture_function_english(e):

        picture_window = tk.Toplevel(root)
        picture_window.iconbitmap('icons/icon.ico')
        picture_window.title("ColorScan - Picture")
        picture_window.minsize(550, 265)
        picture_window.configure(bg=schrift_standard)
        # nav
        top_frame = tk.Frame(picture_window, bg=standard_farbe)
        top_frame.pack(side="top", fill=tk.X)
        nav_name = tk.Label(top_frame, text="Color detection with picture", bg=standard_farbe, font="Bahnschrift 30", fg="white", height=2)
        nav_name.pack(side="top")

        pic_desc = tk.Label(picture_window, text="To open the program click the start\n"
                                                 "button. To close the program click ESC.",

                            bg=schrift_standard, font="Bahnschrift 17", fg="black",
                                height=4)
        pic_desc.pack()
        start_button = tk.Label(picture_window, text="Start", bg=standard_farbe, font="Bahschrift 20", fg=schrift_standard)
        start_button.pack(side='top')
        start_button.bind("<Button-1>", openfile_picture)


    def impressum_english(e):
        impressum_window = tk.Toplevel(root)
        impressum_window.title("ColorScan - Impressum")
        impressum_window.iconbitmap('icons/icon.ico')
        impressum_window.minsize(400, 400)
        impressum_window.configure(bg=schrift_standard)
        # nav
        top_frame = tk.Frame(impressum_window, bg=standard_farbe)
        top_frame.pack(side="top", fill=tk.X)
        nav_name = tk.Label(top_frame, text="Impressum", bg=standard_farbe, font="Bahnschrift 30", fg="white", height=2)
        nav_name.pack(side="top")
        impressum_Angabe = tk.Label(impressum_window, text="ColorScan® 2022", bg=hintergrund, font="Bahnschrift 20",
                                    fg=standard_farbe, height=2)
        impressum_Angabe.pack()
        impressum_us = tk.Label(impressum_window, text="Developers", bg=hintergrund, font="Bahnschrift 17 bold", fg="black", height=2)
        impressum_us.pack()
        impressum_text = tk.Label(impressum_window, text="Chakresh Pechetti\nNishant Rostewitz\nSebastian Morawietz", bg=hintergrund,
                                  font="Bahnschrift 15", fg="black", height=3)
        impressum_text.pack()


    #colors
    standard_farbe= "#2f2f2f"
    schrift_standard = "#ff6620"
    hintergrund = schrift_standard

    root = tk.Tk()
    root.iconbitmap('icons/icon.ico')
    root.title("ColorScan")
    root.minsize(700, 575)

    top_frame = tk.Frame(root, bg=standard_farbe)
    top_frame.pack(side="top", fill=tk.X)
    title = tk.Label(top_frame, text='ColorScan - A colour detecter', font="Bahnschrift 35" ,bg=standard_farbe,
                     fg=schrift_standard, height=2)
    title.pack(side="top")

    home_label1 = tk.Label(root, height=1)
    home_label1.pack()

    home_label2 = tk.Frame(root, height=3,  bg=schrift_standard)
    home_label2.pack(side="top", fill=tk.X)

    webcam_link = tk.Label(home_label2, text="Color recognition\nwith webcam", font="Bahnschrift 17",
                           bg= schrift_standard, fg=standard_farbe, height=3)
    webcam_link.pack(side='left', padx= 100)
    webcam_link.bind("<Button-1>", webcam_function_english)

    photo_link = tk.Label(home_label2, text="Color recognition\nwith image", font="Bahnschrift 17",
                          bg =schrift_standard, fg=standard_farbe, height=3)
    photo_link.pack(side='left', padx=40)
    photo_link.bind("<Button-1>", picture_function_english)

    home_label3 = tk.Label(root, height=1)
    home_label3.pack()

    home_label4 = tk.Label(root, height=3, bg=standard_farbe, font="Bahnschrift 17", fg=schrift_standard,
                           text="This application helps you recognize colors from pictures\n"
                                "or from the webcam. With this tool you can detect colours\n"
                                " with one click!")
    home_label4.pack(side="top", fill=tk.X)

    home_label5 = tk.Label(root, height=1)
    home_label5.pack()

    home_label6 = tk.Label(root, height=2, bg=schrift_standard, font="Bahnschrift 17", fg=standard_farbe, text="")
    home_label6.pack(side="top", fill=tk.X)


    def clock():
        day = time.strftime("%d")
        weekday = time.strftime("%A")
        month = time.strftime("%m")
        year = time.strftime("%Y")
        hour = time.strftime("%H")
        minute = time.strftime("%M")
        clock_label.config(text=weekday + ", " + date_names_english[int(day)] + " " + month_names_english[int(month)]
                                + " " + year + " - " + hour + ":" + minute)
        clock_label.after(1, clock)
    clock_label = tk.Label(home_label6, text="", bg=schrift_standard, fg=standard_farbe, font="Bahnschrift 30", width=30)
    clock_label.pack(pady=30)
    clock()

    home_label7 = tk.Label(root, height=1 )
    home_label7.pack()

    bottom_frame = tk.Frame(root, bg=standard_farbe, height = 2)
    bottom_frame.pack(side='bottom', fill=tk.X)
    impressum_link = tk.Label(bottom_frame, text='Impressum', font="Bahnschrift 20" ,bg=standard_farbe,
                              fg=schrift_standard,height=2)
    impressum_link.pack(side="top")
    impressum_link.bind("<Button-1>", impressum_english)

    root.mainloop()

#----------------------------English package end-------------------------#

language = tk.Tk()
language.title("ColorScan - Language")
language.iconbitmap('icons/icon.ico')

standard_farbe = "#2f2f2f"
schrift_standard = "#ff6620"
hintergrund = schrift_standard

top_frame = tk.Frame(language, bg=standard_farbe)
top_frame.pack(side="top", fill=tk.X)
title = tk.Label(top_frame, text='Choose your language\nWählen Sie die Sprache', font="Bahnschrift 30" ,bg=standard_farbe,
                 fg=schrift_standard, height=2)
title.pack(side="top")

bottom_frame = tk.Frame(language, bg=standard_farbe, height=3)
bottom_frame.pack(side='bottom', fill=tk.X)

germanyflag = ImageTk.PhotoImage(file='icons/germany.png')
deutsch = tk.Label(bottom_frame, image=germanyflag, bg=standard_farbe)
deutsch.pack(side='left', padx=40)
deutsch.bind('<Button-1>', german_package)

ukflag= ImageTk.PhotoImage(file='icons/uk.png')
english = tk.Label(bottom_frame, image=ukflag, bg=standard_farbe)
english.pack(side='left', padx=40)
english.bind('<Button-1>', english_package)

language.mainloop()