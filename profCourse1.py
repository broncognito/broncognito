import tkinter as tk
from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Broncs23", database="broncognito")
mycursor = mydb.cursor()

global mainWindow, defaultScreen, defaultQ, customQ # , var, label, R1, R2, R3, mainWindow5


def helpPage():
    helpScreen = Toplevel(mainWindow)
    helpScreen.title("Help")
    helpScreen.geometry("1500x800")
    Label(helpScreen, text="Help", fg='black', bg='lightgray', width='300', height='2',
          font=("Calibre", 50)).pack()
    redStripe = Label(helpScreen, text=" ", fg='red', bg='indianred', width='300', height='1', font=("Calibre", 50))
    redStripe.pack()
    # code below is adding in the different texts written on the screen in various areas
    Label(helpScreen, text="BronCognito Student", bg="lightgray", fg="black", font=("Calibre", 20)).place(x=5, y=8)
    backButton = Button(helpScreen, text='< Previous Page', font=('Times_New_Roman', 15), height=2, width=15,
                        command=helpScreen.destroy)
    backButton.place(x=10, y=50)
    # creating the menu below (these need to be buttons)
    Label(helpScreen, text="Menu", bg="white", fg="black", font=("Calibre", 25)).place(x=10, y=195)
    Label(helpScreen, text="Course Home Feed", bg="lightgray", height=4, width=15, fg="black",
          font=("Calibre", 20),borderwidth=4, relief="solid").place(x=5, y=230)
    Button(helpScreen, text="Post a New \n Default Question", height=4, width=16, fg="black",
           font=("Calibre", 20), command=defaultQ).place(x=5, y=331)
    Button(helpScreen, text="Post a New \n Custom Question", height=4, width=16, fg="black",
           font=("Calibre", 20), borderwidth=4, relief="solid", command=customQ).place(x=5, y=430)
    Button(helpScreen, text="Help", bg="lightgray", height=4, width=16, fg="black", font=("Calibre", 20),
          borderwidth=4, relief="solid", command=helpPage).place(x=5, y=530)

    helpScreen.mainloop()

# testing lower
def viewStuResponses():
    global responseScreen
    responseScreen = Toplevel(mainWindow)
    responseScreen.title("View Student Responses to Your Questions")
    responseScreen.geometry("1500x800")
    Label(responseScreen, text="View Student Responses to Your Questions", fg='black', bg='lightgray', width='300',
          height='2', font=("Calibre", 50)).pack()
    redStripe = Label(responseScreen, text=" ", fg='red', bg='indianred', width='300', height='1', font=("Calibre",50))
    redStripe.pack()
    # code below is adding in the different texts written on the screen in various areas
    Label(responseScreen, text="BronCognito Professor", bg="lightgray", fg="black", font=("Calibre", 20)).place(x=5, y=8)
    backButton = Button(responseScreen, text='< Previous Page', font=('Times_New_Roman', 15), height=2, width=15,
                        command=responseScreen.destroy)
    backButton.place(x=10, y=50)
    Label(responseScreen, text="My Account", bg="white", fg="black", font=("Calibre", 20), borderwidth=1,
          relief="solid").place(x=1320, y=8)
    # creating the menu below (these need to be buttons)
    Label(responseScreen, text="Menu", bg="white", fg="black", font=("Calibre", 25)).place(x=10, y=195)
    Label(responseScreen, text="Course Home Feed", bg="lightgray", height=4, width=15, fg="black",
          font=("Calibre", 20),borderwidth=4, relief="solid").place(x=5, y=230)
    Button(responseScreen, text="Post a New \n Default Question", height=4, width=16, fg="black",
           font=("Calibre", 20), command=defaultQ).place(x=5, y=331)
    Button(responseScreen, text="Post a New \n Custom Question", height=4, width=16, fg="black",
           font=("Calibre", 20), borderwidth=4, relief="solid", command=customQ).place(x=5, y=430)
    Button(responseScreen, text="Help", bg="lightgray", height=4, width=16, fg="black", font=("Calibre", 20),
           borderwidth=4, relief="solid", command=helpPage).place(x=5, y=530)

    Label(responseScreen, text="View the student responses below:", font=('Calibre', '30')).pack(pady=30)



    mycursor.execute("SELECT DISTINCT ProfQ FROM StuResponseCourse1")
    profQuestions = mycursor.fetchall()
    i = 0
    for x in profQuestions:
        i += 1
        q1Answers = Label(responseScreen, text=" %s" % x).place(x=300, y=300+(30*i))

    mycursor.execute("SELECT StuResponse FROM StuResponseCourse1")
    stuR = mycursor.fetchall()
    i = 0
    for x in stuR:
        i += 1
        responsesStu = Label(responseScreen, text=" %s" % x).place(x=550, y=300+(30*i))

    responseScreen.mainloop()
'''
    mycursor.execute("SELECT StuResponse FROM StuResponseCourse1 WHERE ProfQ = 'Do you like to work in groups?'")
    answers = mycursor.fetchall()
    i = 0
    for x in answers:
        i += 1
        ans = Label(responseScreen, text=" %s" % x).place(x=500, y=300+(30*i))
'''
    # responseScreen.mainloop()


def viewStuSubmissions():
    global submissionsScreen
    submissionsScreen = Toplevel(mainWindow)
    submissionsScreen.title("Default Question Forum")
    submissionsScreen.geometry("1500x800")
    Label(submissionsScreen, text="View Student Submissions and Feedback", fg='black', bg='lightgray', width='300',
          height='2', font=("Calibre", 50)).pack()
    redStripe = Label(submissionsScreen, text=" ", fg='red', bg='indianred', width='300', height='1', font=("Calibre",50))
    redStripe.pack()
    # code below is adding in the different texts written on the screen in various areas
    Label(submissionsScreen, text="BronCognito Professor", bg="lightgray", fg="black", font=("Calibre", 20)).place(x=5, y=8)
    backButton = Button(submissionsScreen, text='< Previous Page', font=('Times_New_Roman', 15), height=2, width=15,
                    command=submissionsScreen.destroy)
    backButton.place(x=10, y=50)
    Label(submissionsScreen, text="My Account", bg="white", fg="black", font=("Calibre", 20), borderwidth=1,
        relief="solid").place(x=1320, y=8)
    # creating the menu below
    Label(submissionsScreen, text="Menu", bg="white", fg="black", font=("Calibre", 25)).place(x=10, y=195)
    Button(submissionsScreen, text="Course Home Feed", bg="lightgray", height=4, width=16, fg="black",
        font=("Calibre", 20),borderwidth=4, relief="solid", command=profHomeInterface).place(x=5, y=230)
    Button(submissionsScreen, text="Post a New \n Default Question", height=4, width=16, fg="black",
       font=("Calibre", 20), command=defaultQ).place(x=5, y=331)
    Button(submissionsScreen, text="Post a New \n Custom Question", height=4, width=16, fg="black",
       font=("Calibre", 20), borderwidth=4, relief="solid", command=customQ).place(x=5, y=430)
    Button(submissionsScreen, text="Help", bg="lightgray", height=4, width=16, fg="black", font=("Calibre", 20),
       borderwidth=4, relief="solid", command=helpPage).place(x=5, y=530)

    Label(submissionsScreen, text="View the student submissions below:", font=('Calibre', '30')).pack(pady=30)


    # grabbing student submissions
    mycursor.execute("SELECT StuQues FROM StuQuesCourse1")
    stuSubmiss = mycursor.fetchall()

    def callback(selection):
        global stuQues
        stuQues = selection

    listofstuQ = [r for r, in stuSubmiss]
    options = tk.StringVar(submissionsScreen)
    options.set(listofstuQ[0]) # default value
    drpdwn = tk.OptionMenu(submissionsScreen, options, *listofstuQ, command=callback)
    drpdwn.place(x=400, y=280)

    profEntry = Entry(submissionsScreen, font='Calibre 24')
    profEntry.config(highlightthickness=5)
    profEntry.place(x=400, y=320, width=600, height=300)

    # def clear():  # clear button not working correctly right now
    #  userResponse.delete(1.0, END)

    def postResponse():  # saves custom ques to the DB and goes to the list of ques to be grabbed for the student page
        profResponse = profEntry.get()
        mycursor.execute("INSERT INTO ProfResponseCourse1(StuQ, ProfResponse) VALUES ('"+stuQues+"', '"+profResponse+"')")
        mydb.commit()
        my_label = Label(submissionsScreen, text="Your response has been posted to the student feed.", font=("Calibre", 20))
        my_label.place(x=530, y=660)
        print("Response Posted")  # only for personal use, not required for GUI

    postBtn = Button(submissionsScreen, text="Post Response", command=postResponse)
    postBtn.place(x=690, y=630)
    clear_button = Button(submissionsScreen, text="Clear Text",)  # command=clear)
    clear_button.place(x=610, y=630)

    submissionsScreen.mainloop()



'''

    def selected_item():
        for i in listbox.curselection():
            profResponse = profAns.get()
            #stuQues = listbox.get(i)
            #print(stuQues)
            mycursor.execute("INSERT INTO ProfResponseCourse1(StuQ, ProfResponse) VALUES ('"+stuQues+"', '"+profResponse+"')")
            mydb.commit()
            my_label.config(text="Your response has been posted to the student feed.", font=("Calibre", 20))
            my_label.place(x=700, y=700)
            print(listbox.get(i))

    btn = Button(submissionsScreen, text='Post Answer', command=selected_item)
    btn.place(x=1000, y=650)
# Placing the button and listbox
    listbox.place(x=300, y=300)

    my_label = Label(submissionsScreen)
    my_label.pack(pady=20)
    submissionsScreen.mainloop()
    
    
    
    # code below to grab and display the student submissions from the database
    mycursor.execute("SELECT StuQues FROM StuQuesCourse1")
    stuSubmiss = mycursor.fetchall()
    i = 0
    for x in stuSubmiss:
        i += 1
        displaySubmiss = Label(submissionsScreen, text=" %s" % x, font="Calibre 20").place(x=400, y=300+(30*i))
    # maybe create this as buttons and then I can be able to click them for a drop down entry box that will open and we
    # can have the prof answer that question right there and then send teh response w the ques to the student home feed
    # and do some sort of boolean variable to decide if it has been answered or is still unanswered
'''

def defaultQ():
    global defaultScreen, customQ, defaultQ, var, label
    defaultScreen = Toplevel(mainWindow)
    defaultScreen.title("Default Question Forum")
    defaultScreen.geometry("1500x800")
    Label(defaultScreen, text="Post a New Default Question", fg='black', bg='lightgray', width='300', height='2',
          font=("Calibre", 50)).pack()
    redStripe = Label(defaultScreen, text=" ", fg='red', bg='indianred', width='300', height='1', font=("Calibre", 50))
    redStripe.pack()
    # code below is adding in the different texts written on the screen in various areas
    Label(defaultScreen, text="BronCognito Professor", bg="lightgray", fg="black", font=("Calibre", 20)).place(x=5, y=8)
    backButton = Button(defaultScreen, text='< Previous Page', font=('Times_New_Roman', 15), height=2, width=15,
                        command=defaultScreen.destroy)
    backButton.place(x=10, y=50)
    Label(defaultScreen, text="My Account", bg="white", fg="black", font=("Calibre", 20), borderwidth=1,
          relief="solid").place(x=1320, y=8)
    # creating the menu below (these need to be buttons)
    Label(defaultScreen, text="Menu", bg="white", fg="black", font=("Calibre", 25)).place(x=10, y=195)
    Label(defaultScreen, text="Course Home Feed", bg="lightgray", height=4, width=15, fg="black",
          font=("Calibre", 20),borderwidth=4, relief="solid").place(x=5, y=230)
    Button(defaultScreen, text="Post a New \n Default Question", height=4, width=16, fg="black",
           font=("Calibre", 20), command=defaultQ).place(x=5, y=331)
    Button(defaultScreen, text="Post a New \n Custom Question", height=4, width=16, fg="black",
           font=("Calibre", 20), borderwidth=4, relief="solid", command=customQ).place(x=5, y=430)
    Button(defaultScreen, text="Help", bg="lightgray", height=4, width=16, fg="black", font=("Calibre", 20),
          borderwidth=4, relief="solid", command=helpPage).place(x=5, y=530)

    Label(defaultScreen, text="Select a default question from the options below:", font=('Calibre', '30')).pack(pady=30)

    def clicked(value):
        print(var.get())

    def postDefQ():
        label2 = Label(defaultScreen, text="Your chosen question has been posted to CSC 320.", height=1,
                                      width=40, fg="black", font=("Calibre", 20)).place(x=400, y=600)
        Question1 = "What alternative learning methods would you suggest to make this course more interactive?"
        Question2 = "How can the structure of this course be improved?"
        Question3 = "Do you feel that the assignments and examinations have provided you with valuable knowledge?"
        if var.get() == "Ques1":
            print("placeholder for sending ques to the database")
            mycursor.execute("INSERT INTO DefaultProfQuesCourse1(DefaultQues) VALUES ('"+Question1+"')")
            mydb.commit()
        elif var.get() == "Ques2":
            print("placeholder for ques 2")
            mycursor.execute("INSERT INTO DefaultProfQuesCourse1(DefaultQues) VALUES ('"+Question2+"')")
            mydb.commit()
        elif var.get() == "Ques3":
            print("placeholder for ques 3")
            mycursor.execute("INSERT INTO DefaultProfQuesCourse1(DefaultQues) VALUES ('"+Question3+"')")
            mydb.commit()


    var = StringVar()
    Radiobutton(defaultScreen, text="1. What alternative learning methods would you suggest to make "
                "this course more interactive?", variable=var, value='Ques1',
                command=lambda: clicked(var.get())).place(x=390, y=300)
    Radiobutton(defaultScreen, text="2. How can the structure of this course be improved?", variable=var, value='Ques2',
                command=lambda: clicked(var.get())).place(x=390, y=400)
    Radiobutton(defaultScreen, text="3. Do you feel that the assignments and examinations have provided you "
                "with valuable knowledge?", variable=var, value='Ques3',
                command=lambda: clicked(var.get())).place(x=390, y=500)

    post = Button(defaultScreen, text="Post Default Question", height=2, width=20, command=postDefQ)
    post.place(x=550, y=550)
    # end

    defaultScreen.mainloop()


def customQ():
    global customScreen, customQ, defaultQ, my_text, my_label, my_frame, button_frame, clear_button, get_text_button
    customScreen = Toplevel(mainWindow)
    customScreen.title("Custom Question Forum")
    customScreen.geometry("1500x800")
    Label(customScreen, text="Post a New Custom Question", fg='black', bg='lightgray', width='300', height='2',
          font=("Calibre", 50)).pack()
    redStripe = Label(customScreen, text=" ", fg='red', bg='indianred', width='300', height='1', font=("Calibre", 50))
    redStripe.pack()
    # code below is adding in the different texts written on the screen in various areas
    Label(customScreen, text="BronCognito Professor", bg="lightgray", fg="black", font=("Calibre", 20)).place(x=5, y=8)
    backButton = Button(customScreen, text='< Previous Page', font=('Times_New_Roman', 15), height=2, width=15,
                        command=customScreen.destroy)
    backButton.place(x=10, y=50)
    # might want to add the "my account" here in the upper RHS
    # creating the menu below
    Label(customScreen, text="Menu", bg="white", fg="black", font=("Calibre", 25)).place(x=10, y=195)
    Label(customScreen, text="Course Home Feed", bg="lightgray", height=4, width=15, fg="black",
          font=("Calibre", 20), borderwidth=4, relief="solid").place(x=5, y=230)
    Button(customScreen, text="Post a New \n Default Question", height=4, width=16, fg="black",
           font=("Calibre", 20), command=defaultQ).place(x=5, y=331)
    Button(customScreen, text="Post a New \nCustom Question", height=4, width=16, fg="black",
           font=("Calibre", 20), borderwidth=4, relief="solid", command=customQ).place(x=5, y=430)
    Button(customScreen, text="Help", bg="lightgray", height=4, width=16, fg="black", font=("Calibre", 20),
          borderwidth=4, relief="solid", command=helpPage).place(x=5, y=530)

    Label(customScreen, text="Type to create your Custom Question in the Box Below:", font=('Calibre', '30')).pack(pady=30)
    ent1 = Entry(customScreen, font='Calibre 24')
    ent1.config(highlightthickness=5)
    ent1.place(x=400, y=300, width=600, height=300)

    def clear():  # NEED TO FIX THE CLEAR TEXT FUNCTION IT IS NOT WORKING-- OR JUST DELETE IT
        newQues = ent1.get()
        newQues.delete(1.0, END)

    def postCustomQ():  # saves custom ques to the DB and goes to the list of ques to be grabbed for the student page
        newQues = ent1.get()
        mycursor.execute("INSERT INTO CustomProfQuesCourse1(CustomQues) VALUES ('"+newQues+"')")
        mydb.commit()
        my_label.config(text="Your custom question has been posted to your course.", font=("Calibre", 20))
        my_label.place(x=530, y=660)
        print("Response Submitted") # only for personal use, not required for GUI

    postBtn = Button(customScreen, text="Post Question", command=postCustomQ)
    postBtn.place(x=690, y=610)
    clear_button = Button(customScreen, text="Clear Text", command=clear)
    clear_button.place(x=610, y=610)

    my_label = Label(customScreen, text="")
    my_label.pack(pady=20)
    customScreen.mainloop()


# testing below for default questions w student answers. create the page where the questions will post to with responses
#def


def profHomeInterface():
    global mainWindow, defaultQ, customQ, helpPage
    mainWindow = Tk()
    mainWindow.title("Course Home - Professor")
    mainWindowTitle = Label(mainWindow, text="Welcome to Your Course (Dr.Mourya)", fg='black', bg='lightgray',
                            width='300', height='2', font=("Calibre", 50))
    mainWindowTitle.pack()
    redStripe = Label(mainWindow, text=" ", fg='red', bg='indianred', width='300', height='1', font=("Calibre", 50))
    redStripe.pack()
    mainWindow.geometry("1500x800")
    Label(mainWindow, text="BronCognito Professor", bg="lightgray", fg="black", font=("Calibre", 20)).place(x=5, y=8)
    backButton = Button(mainWindow, text='< Previous Page', font=('Times_New_Roman', 15), height=2, width=15,
                        command=mainWindow.destroy)
    backButton.place(x=10, y=50)
    Label(mainWindow, text="My Account", bg="white", fg="black", font=("Calibre", 20), borderwidth=1,
          relief="solid").place(x=1310, y=8) # we might choose to remove this feature

    # creating the menu below (these need to be buttons)
    Label(mainWindow, text="Menu", bg="white", fg="black", font=("Calibre", 25)).place(x=10, y=195)
    Label(mainWindow, text="Course Home Feed", bg="lightgray", height=4, width=15, fg="black", font=("Calibre", 20),
          borderwidth=4, relief="solid").place(x=5, y=230)
    Button(mainWindow, text="Post a New \n Default Question", bg="lightgray", height=4, width=16, fg="black",
           font=("Calibre", 20), borderwidth=4, relief="solid", command=defaultQ).place(x=5, y=330)
    Button(mainWindow, text="Post a New \n Custom Question", bg="lightgray", height=4, width=16, fg="black",
           font=("Calibre", 20), borderwidth=4, relief="solid", command=customQ).place(x=5, y=430)
    Button(mainWindow, text="Help", bg="lightgray", height=4, width=16, fg="black", font=("Calibre", 20),
          borderwidth=4, relief="solid", command=helpPage).place(x=5, y=530)

    Label(mainWindow, text="Course Home", bg="white", fg="black", font=("Calibre", 30)).place(x=300, y=200)
    Label(mainWindow, text=" ", bg="white", fg="black", font=("Calibre", 20), height=20, width=62,
          borderwidth=1, relief="solid").place(x=335, y=260)   # outlining for buttons
    Button(mainWindow, text="View Student Responses \nto Your Questions", bg="lightgray", height=8, width=20, fg="black",
           font=("Calibre", 20), borderwidth=4, relief="solid", command=viewStuResponses).place(x=400, y=350)
    Button(mainWindow, text="View Student-submitted \nQuestions or Comments", bg="lightgray", height=8, width=20, fg="black",
           font=("Calibre", 20), borderwidth=4, relief="solid", command=viewStuSubmissions).place(x=800, y=350)
    # NEED TO CHANGE THE COMMANDS FOR THE TWO BUTTONS ABOVE HERE SO THEY OPEN THE CORRECT PAGES

    mainWindow.mainloop()


profHomeInterface()
