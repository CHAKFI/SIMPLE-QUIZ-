# Python program to create a simple GUI
# Simple Quiz using Tkinter

# import everything from tkinter
from tkinter import *

# and import messagebox as mb from tkinter
from tkinter import messagebox as mb

# import json to use json file for data
import json

# Image
from PIL import ImageTk, Image

import os


def delete2():
    screen3.destroy()


def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()


def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100+580+300")
    screen3.resizable(False, False)

    Label(screen3, text="Login en Suces").pack()
    Button(screen3, text="OK", command=screen.destroy).pack()


def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Password")
    screen4.geometry("150x100+580+300")
    screen4.resizable(False, False)
    Label(screen4, text="Incorrecte").pack()
    Button(screen4, text="OK", command=delete3).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100+580+300")
    screen5.resizable(False, False)
    Label(screen5, text="utilisateur introuvable").pack()
    Button(screen5, text="OK", command=delete4).pack()


def register_user():
    print("S'enregistrer")

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    global screen0
    screen0 = Toplevel(screen)
    screen0.title("Success")
    screen0.geometry("150x100+580+300")
    screen0.resizable(False, False)

    Label(screen0, text="Registration en Succes").pack()
    Button(screen0, text="OK", command=screen0.destroy).pack()
    screen1.destroy()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
            screen2.destroy()
        else:
            password_not_recognised()

    else:
        user_not_found()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Registrer")
    screen1.geometry("300x250+500+200")
    screen1.resizable(False, False)

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Veuillez saisir votre informations").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()

    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Registrer", width=10, height=1, command=register_user).pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Quitter", width=10, height=1, command=screen1.destroy).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250+500+200")
    screen2.resizable(False, False)

    Label(screen2, text="Veuillez saisir votre informations").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Quitter", width=10, height=1, command=screen2.destroy).pack()


def exity():
    exit()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250+500+200")
    screen.title("L O G I N")
    screen.resizable(False, False)

    Label(text="SESSION", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    Label(text="").pack()
    b1 = Button(text="Quitter", height="2", width="30", command=exity).pack()

    screen.mainloop()


main_screen()


# class to define the components of the GUI
class Quiz:

    def show(self):
        r1 = Tk()
        r1.title("Correction !")
        r1.geometry("500x500+500+100")
        r1.configure(bg='#87E990')

        bb = Button(r1, text="<-- Retour vers Quizz", width=18, bg="#370028", fg="white",
                    font=("Bahnschrift", 16, "bold"), command=r1.destroy)
        bb.place(x=130, y=10)

        label_1 = Label(r1, text="Q1. Reponse : AKHENOCH AZIZ", fg="black", font=("Bahnschrift", 12, "bold"),
                        bg='#87E990')
        label_1.place(x=10, y=130)

        label_2 = Label(r1, text="Q2. Reponse : Intelligents et Mobiles", fg="black",
                        font=("Bahnschrift", 12, "bold"),bg='#87E990')
        label_2.place(x=10, y=210)

        label_3 = Label(r1, text="Q3. Reponse : Python est utilisé dans DATA SCIENCE", fg="black",
                        font=("Bahnschrift", 12, "bold"),bg='#87E990')
        label_3.place(x=10, y=290)

        label_4 = Label(r1, text="Q4. Reponse : Mcr = Mc / ect.", fg="black",
                        font=("Bahnschrift", 12, "bold"),bg='#87E990')
        label_4.place(x=10, y=370)

        r1.mainloop()


    # This is the first method which is called when a
    # new object of the class is initialized. This method
    # sets the question count to 0. and initialize all the
    # other methoods to display the content and make all the
    # functionalities available

    def __init__(self):

        # set question number to 0
        self.q_no = 0

        # assigns ques to the display_question function to update later.
        self.display_title()
        self.display_question()

        # opt_selected holds an integer value which is used for
        # selected option in a question.
        self.opt_selected = IntVar()

        # displaying radio button for the current question and used to
        # display options for the current question
        self.opts = self.radio_buttons()

        # display options for the current question
        self.display_options()

        # displays the button for next and exit.
        self.buttons()

        # no of questions
        self.data_size = len(question)

        # keep a counter of correct answers
        self.correct = 0

    # This method is used to display the result
    # It counts the number of correct and wrong answers
    # and then display them at the end as a message Box
    def display_result(self):

        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Reponses Correctes : {self.correct}"
        wrong = f"Reponses Incorrecte : {wrong_count}"

        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Votre Score : {score} pt"

        # Shows a message box to display the result
        # mb.showinfo("Resultat: ", f"\t\t\n\n{result}\t\t\n\n{correct}\t\t\n\n{wrong}")

        r2 = Tk()
        r2.title("Resultat !")
        r2.geometry("400x400+500+100")
        r2.configure(bg='#74D0F1')
        r2.resizable(False,False)

        bb = Button(r2, text="<-- Retour vers Quizz", width=18, bg="#370028", fg="white",
                    font=("Bahnschrift", 16, "bold"), command=r2.destroy)
        bb.place(x=80, y=10)

        l1 = Label(r2,text="{}".format(result), fg="black",
                        font=("Bahnschrift", 18, "bold"), bg='#74D0F1')
        l1.place(x=65, y=130)

        l2 = Label(r2, text="{}".format(correct), fg="black",
                        font=("Bahnschrift", 18, "bold"), bg='#74D0F1')
        l2.place(x=65, y=210)

        l3 = Label(r2, text="{}".format(wrong), fg="black",
                        font=("Bahnschrift", 18, "bold"), bg='#74D0F1')
        l3.place(x=65, y=290)

    # This method checks the Answer after we click on Next.
    def check_ans(self, q_no):

        # checks for if the selected option is correct
        if self.opt_selected.get() == answer[q_no]:
            # if the option is correct it return true
            return True

    # This method is used to check the answer of the
    # current question by calling the check_ans and question no.
    # if the question is correct it increases the count by 1
    # and then increase the question number by 1. If it is last
    # question then it calls display result to show the message box.
    # otherwise shows next question.
    def pv_b(self):
        self.q_no -= 1
        self.display_question()
        self.display_options()

    def next_btn(self):

        # Check if the answer is correct
        if self.check_ans(self.q_no):
            # if the answer is correct it increments the correct by 1
            self.correct += 1

        # Moves to next Question by incrementing the q_no counter
        self.q_no += 1

        # checks if the q_no size is equal to the data size
        if self.q_no == self.data_size:

            # if it is correct then it displays the score
            self.display_result()


        else:
            # shows the next question
            self.display_question()
            self.display_options()

    # This method shows the two buttons on the screen.
    # The first one is the next_button which moves to next question
    # It has properties like what text it shows the functionality,
    # size, color, and property of text displayed on button. Then it
    # mentions where to place the button on the screen. The second
    # button is the exit button which is used to close the GUI without
    # completing the quiz.
    def buttons(self):

        def bye():
            test = mb.askyesno('Quitter', 'Voulez vous vraiment quitter ?')
            if test:
                gui.destroy()

        # previous button
        prev_button = Button(gui, text="Precedent", command=self.pv_b,
                             width=10, bg="#370028", fg="white", font=("Bahnschrift", 16, "bold"))
        prev_button.place(x=300, y=380)
        # next Question
        next_button = Button(gui, text="Suivant", command=self.next_btn,
                             width=10, bg="#370028", fg="white", font=("Bahnschrift", 16, "bold"))

        # palcing the button  on the screen
        next_button.place(x=435, y=380)

        corr_button = Button(gui, text="Correction", command=self.show,
                             width=10, bg="green", fg="white", font=("Bahnschrift", 16, "bold"))

        # palcing the button  on the screen
        corr_button.place(x=20, y=380)

        # This is the second button which is used to Quit the GUI
        quit_button = Button(gui, text="Quitter", command=bye,
                             width=5, bg="red", fg="white", font=("Bahnschrift", 16, "bold"))

        # placing the Quit button on the screen
        quit_button.place(x=710, y=380)


    # This method deselect the radio button on the screen
    # Then it is used to display the options available for the current
    # question which we obtain through the question number and Updates
    # each of the options for the current question of the radio button.
    def display_options(self):
        val = 0

        # deselecting the options
        self.opt_selected.set(0)

        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    # This method shows the current Question on the screen
    def display_question(self):

        # setting the Question properties
        q_no = Label(gui, text=question[self.q_no], width=60,
                     font=('Bahnschrift', 16, 'bold'), anchor='w', bg='#997A8D')

        # placing the option on the screen
        q_no.place(x=20, y=120)

    # This method is used to Display Title
    def display_title(self):

        # The title to be shown
        title = Label(gui, text="Master Systèmes Intelligents et Mobiles",
                      width=60, bg="#048B9A", fg="white", font=("Bahnschrift", 20, "bold"))
        # place of the title
        title.place(x=-30, y=1)

    # This method shows the radio buttons to select the Question
    # on the screen at the specified position. It also returns a
    # lsit of radio button which are later used to add the options to
    # them.
    def radio_buttons(self):

        # initialize the list with an empty list of options
        q_list = []

        # position of the first option
        y_pos = 180

        # adding the options to the list
        while len(q_list) < 4:
            # setting the radio button properties
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("Bahnschrift", 14), bg='#997A8D')

            # adding the button to the list
            q_list.append(radio_btn)

            # placing the button
            radio_btn.place(x=20, y=y_pos)

            # incrementing the y-axis position by 40
            y_pos += 40

        # return the radio buttons
        return q_list


# Create a GUI Window
gui = Tk()
gui.resizable(False, False)
gui.iconbitmap('C:/Users/ahmed/Pictures/Gg.ico')
gui.configure(bg='#997A8D')

# add image
load = Image.open("C:/Users/ahmed/Desktop/DUT-LP-MS/S7/FPT.png")
img = load.resize((700, 60), Image.ANTIALIAS)
render = ImageTk.PhotoImage(img)
pic = Label(gui, image=render, bg='#997A8D')
pic.place(x=50, y=40)

# set the size of the GUI Window
gui.geometry("800x450+300+150")

# set the title of the Window
gui.title("Master Systèmes Intelligents et Mobiles")

# get the data from the json file
with open('data.json') as f:
    data = json.load(f)

# set the question, options, and answer
question = (data['question'])
options = (data['options'])
answer = (data['answer'])

# create an object of the Quiz Class.

quiz = Quiz()

# Start the GUI
gui.mainloop()
