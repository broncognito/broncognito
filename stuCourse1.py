import tkinter as tk
from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Broncs23", database="broncognito")
mycursor = mydb.cursor()

global mainWindow2, answerScreen, my_label, askScreen, answerProfQues, askOwnQues, studentHomeInterface


def helpPage():
    helpScreen = Toplevel(mainWindow2)
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
    Button(mainWindow2, text="Course Home Feed", height=4, width=16, fg="black", font=("Calibre", 20),
           borderwidth=4, relief="solid", command=studentHomeInterface).place(x=5, y=230)
    Button(helpScreen, text="Answer Your \nProfessor's Questions", height=4, width=16, fg="black",
           font=("Calibre", 20), command=answerProfQues).place(x=5, y=331)
    Button(helpScreen, text="Create/Ask Your \nOwn Question", height=4, width=16, fg="black",
           font=("Calibre", 20), borderwidth=4, relief="solid", command=askOwnQues).place(x=5, y=430)
    Button(helpScreen, text="Help", bg="lightgray", height=4, width=16, fg="black", font=("Calibre", 20),
           borderwidth=4, relief="solid", command=helpPage).place(x=5, y=530)

    helpScreen.mainloop()


def answerProfQues():
    global answerScreen, my_label, helpPage
    answerScreen = Toplevel(mainWindow2)
    answerScreen.title("Student Response Forum")
    answerScreen.geometry("1500x800")
    Label(answerScreen, text="Answer Your Professor's Questions", fg='black', bg='lightgray', width='300', height='2',
          font=("Calibre", 50)).pack()
    redStripe = Label(answerScreen, text=" ", fg='red', bg='indianred', width='300', height='1', font=("Calibre", 50))
    redStripe.pack()
    # code below is adding in the different texts written on the screen in various areas
    Label(answerScreen, text="BronCognito Student", bg="lightgray", fg="black", font=("Calibre", 20)).place(x=5, y=8)
    backButton = Button(answerScreen, text='< Previous Page', font=('Times_New_Roman', 15), height=2, width=15,
                        command=answerScreen.destroy)
    backButton.place(x=10, y=50)
    # creating the menu below (these need to be buttons)
    Label(answerScreen, text="Menu", bg="white", fg="black", font=("Calibre", 25)).place(x=10, y=195)
    Button(mainWindow2, text="Course Home Feed", height=4, width=16, fg="black", font=("Calibre", 20),
           borderwidth=4, relief="solid", command=studentHomeInterface).place(x=5, y=230)
    Button(answerScreen, text="Answer Your \nProfessor's Questions", height=4, width=16, fg="black",
           font=("Calibre", 20), command=answerProfQues).place(x=5, y=331)
    Button(answerScreen, text="Create/Ask Your \nOwn Question", height=4, width=16, fg="black",
           font=("Calibre", 20), borderwidth=4, relief="solid", command=askOwnQues).place(x=5, y=430)
    Button(answerScreen, text="Help", bg="lightgray", height=4, width=16, fg="black", font=("Calibre", 20),
           borderwidth=4, relief="solid", command=helpPage).place(x=5, y=530)

    Label(answerScreen, text="Below is a list of questions that your professor has made available for you to answer. "
                             "\n Please Select a Question and Type a Response in the box Below:",
          font=('Calibre', 25)).pack(pady=10)

    # creating the dropdown menu for the question choice (this shows both default and custom made prof questions)
    mycursor.execute("SELECT DISTINCT DefaultQues FROM DefaultProfQuesCourse1")
    defProfQues = mycursor.fetchall()
    mycursor.execute("SELECT DISTINCT CustomQues FROM CustomProfQuesCourse1")
    customProfQues = mycursor.fetchall()

    def callback(selection):
        global question
        question = selection

    my_list = [r for r, in defProfQues]
    mylist2 = [r for r, in customProfQues]  # create a  list
    options = tk.StringVar(answerScreen)
    options.set(my_list[0])
    options.set(mylist2[0])  # default value
    drpdwn = tk.OptionMenu(answerScreen, options, *my_list, *mylist2, command=callback)
    drpdwn.place(x=400, y=280)

    stuEntry = Entry(answerScreen, font='Calibre 24')
    stuEntry.config(highlightthickness=5)
    stuEntry.place(x=400, y=320, width=600, height=300)

    # def clear():  # clear button not working correctly right now
      #  userResponse.delete(1.0, END)

    #def get_text():
        #my_label.config(text="Your response has been posted to Dr. Mourya's Course.", font=("Calibre", 20))

    def saveResponse():  # saves custom ques to the DB and goes to the list of ques to be grabbed for the student page
        response = stuEntry.get()
        mycursor.execute("INSERT INTO StuResponseCourse1(ProfQ, StuResponse) VALUES ('"+question+"', '"+response+"')")
        mydb.commit()
        my_label.config(text="Your response has been sent to your professor.", font=("Calibre", 20))
        my_label.place(x=530, y=660)
        print("Response Submitted")  # only for personal use, not required for GUI

    postBtn = Button(answerScreen, text="Send Response", command=saveResponse)
    postBtn.place(x=690, y=630)
    clear_button = Button(answerScreen, text="Clear Text",)  # command=clear)
    clear_button.place(x=610, y=630)

    my_label = Label(answerScreen)
    my_label.pack(pady=20)
    answerScreen.mainloop()


def askOwnQues():
    global askScreen, my_label, helpPage
    askScreen = Toplevel(mainWindow2)
    askScreen.title("Student Question Forum")
    askScreen.geometry("1500x800")
    Label(askScreen, text="Create Your Own Question to Ask", fg='black', bg='lightgray', width='300', height='2',
          font=("Calibre", 50)).pack()
    redStripe = Label(askScreen, text=" ", fg='red', bg='indianred', width='300', height='1', font=("Calibre", 50))
    redStripe.pack()
    # code below is adding in the different texts written on the screen in various areas
    Label(askScreen, text="BronCognito Student", bg="lightgray", fg="black", font=("Calibre", 20)).place(x=5, y=8)
    backButton = Button(askScreen, text='< Previous Page', font=('Times_New_Roman', 15), height=2, width=15,
                        command=askScreen.destroy)
    backButton.place(x=10, y=50)
    # creating the menu below (these need to be buttons)
    Label(askScreen, text="Menu", bg="white", fg="black", font=("Calibre", 25)).place(x=10, y=195)
    Button(mainWindow2, text="Course Home Feed", height=4, width=16, fg="black", font=("Calibre", 20),
           borderwidth=4, relief="solid", command=studentHomeInterface).place(x=5, y=230)
    Button(askScreen, text="Answer Your \nProfessor's Questions", height=4, width=16, fg="black",
           font=("Calibre", 20), command=answerProfQues).place(x=5, y=331)
    Button(askScreen, text="Create/Ask Your \nOwn Question", height=4, width=16, fg="black",
           font=("Calibre", 20), borderwidth=4, relief="solid", command=askOwnQues).place(x=5, y=430)
    Button(askScreen, text="Help", bg="lightgray", height=4, width=16, fg="black", font=("Calibre", 20),
           borderwidth=4, relief="solid", command=helpPage).place(x=5, y=530)

    Label(askScreen, text="In the box below, type to create your own question to ask your professor. \nYou may also "
                          "enter any comment or suggestion that you would like your professor to see.",
          font=('Calibre', 25)).pack(pady=40)

    entry = Entry(askScreen, font='Calibre 24')
    entry.config(highlightthickness=5)
    entry.place(x=400, y=300, width=600, height=300)

    def clear():  # NEED TO FIX THE CLEAR TEXT FUNCTION IT IS NOT WORKING-- OR JUST DELETE IT
        stuQues = entry.get()
        stuQues.delete(1.0, END)

    def postStuQ():  # saves custom ques to the DB and goes to the list of ques to be grabbed for the student page
        stuQues = entry.get()
        mycursor.execute("INSERT INTO StuQuesCourse1(StuQues) VALUES ('"+stuQues+"')")
        mydb.commit()
        my_label.config(text="Your custom question has been sent to your professor.", font=("Calibre", 20))
        my_label.place(x=530, y=660)
        print("Response Submitted")  # only for personal use, not required for GUI

    postBtn = Button(askScreen, text="Post Question", command=postStuQ)
    postBtn.place(x=690, y=610)
    clear_button = Button(askScreen, text="Clear Text", command=clear)
    clear_button.place(x=610, y=610)

    my_label = Label(askScreen, text="")
    my_label.pack(pady=20)
    askScreen.mainloop()


def studentHomeInterface():
    global mainWindow2, answerProfQues, askOwnQues, helpPage
    mainWindow2 = Tk()
    mainWindow2.title("Course Home")
    mainWindow2Title = Label(mainWindow2, text="Welcome to Dr.Mourya's Course", fg='black', bg='lightgray',
                             width='300', height='2', font=("Calibre", 50))
    mainWindow2Title.pack()
    redStripe = Label(mainWindow2, text=" ", fg='red', bg='indianred', width='300', height='1', font=("Calibre", 50))
    redStripe.pack()
    mainWindow2.geometry("1500x800")
    Label(mainWindow2, text="BronCognito Student", bg="lightgray", fg="black", font=("Calibre", 20)).place(x=5, y=8)
    backButton = Button(mainWindow2, text='< Previous Page', font=('Times_New_Roman', 15), height=2, width=15,
                        command=mainWindow2.destroy)
    backButton.place(x=10, y=50)

    #  outlining
    Label(mainWindow2, text=" ", bg="white", fg="black", font=("Calibre", 20), height=20, width=80,
          borderwidth=1, relief="solid").place(x=300, y=260)

    # creating the menu below (these might need to be buttons)
    Label(mainWindow2, text="Menu", bg="white", fg="black", font=("Calibre", 25)).place(x=10, y=195)
    Button(mainWindow2, text="Course Home Feed", height=4, width=16, fg="black", font=("Calibre", 20),
           borderwidth=4, relief="solid", command=studentHomeInterface).place(x=5, y=230)
    Button(mainWindow2, text="Answer Your \nProfessor's Questions", height=4, width=16, fg="black",
           font=("Calibre", 20), command=answerProfQues).place(x=5, y=331)
    Button(mainWindow2, text="Create/Ask Your \nOwn Question", height=4, width=16, fg="black",
           font=("Calibre", 20), borderwidth=4, relief="solid", command=askOwnQues).place(x=5, y=430)
    Button(mainWindow2, text="Help", bg="lightgray", height=4, width=16, fg="black", font=("Calibre", 20),
          borderwidth=4, relief="solid", command=helpPage).place(x=5, y=530)
    Label(mainWindow2, text="Course Home", bg="white", fg="black", font=("Calibre", 30)).place(x=350, y=210)

    Label(mainWindow2, text="Here, you can view your professor's replies to student submissions: ",
          font=('Calibre', 25)).place(x=375, y=300)


    # here, we need to grab the student questions and professor responses from the database and display them
    mycursor.execute("SELECT StuQ FROM ProfResponseCourse1")
    stuSubmissions = mycursor.fetchall()
    i = 0
    for x in stuSubmissions:
        i += 1
        submissionsStu = Label(mainWindow2, text="Student Submission: %s" % x).place(x=350, y=350+(30*i))

    mycursor.execute("SELECT ProfResponse FROM ProfResponseCourse1")
    profR = mycursor.fetchall()
    i = 0
    for x in profR:
        i += 1
        responsesProf = Label(mainWindow2, text="Professor's Answer: %s" % x).place(x=850, y=350+(30*i))

    mainWindow2.mainloop()


studentHomeInterface()


