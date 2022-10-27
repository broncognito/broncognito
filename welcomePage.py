# here i am going to develop the welcome page where it will say "welcome to BronCognito", and it will have a little
# bit of background on what the app is, maybe we can put our email on there if someone wants to send us an email to
# contact us. I will also put "please begin by choosing your course below" and then it will bring you to the page for
# that course that will ask you for the access code. it can say please ask your professor for the access code. and it
# can have some details about the course including prof name, time, course name and title, etc. then, once, they log in,
# it can prompt to another .py file for that course, where we can run everything out of

# lets add an option on this page that says something like "if you are a professor, click here to log in" and then we
# have one common welcome page screen for ALL USERS, and then for the students, its easy and right there.


from tkinter import *
import time

global main_screen, course1access_screen, course2access_screen, course3access_screen, course4access_screen


def course1access():
    global course1access_screen
    course1access_screen = Toplevel(main_screen)
    course1access_screen.title("Access Your Course")
    course1access_screen.geometry("1500x800")
    Label(course1access_screen, text="Get Access to Dr. Mourya's Course", bg="lightgray", width="300",
          height="2", font=("Calibre", 70)).pack()
    redStripe = Label(course1access_screen, text=" ", fg='red', bg='indianred', width='300', height='1', font=("Calibre", 50))
    redStripe.pack()
    Label(course1access_screen, text="Please enter your access code below: ", font=("calibre", 35), pady=50).pack()
    Label(course1access_screen, text="Access Code * ", font=("calibre", 25)).pack()

    def accessCode_verify():
        codeInput = course1code.get() # gets the password from user entry
        if codeInput == "12345": # here is where we can set up the access code per course
            Label(course1access_screen, text="Now entering the course...", font=("calibre", 35)).pack()
            time.sleep(1)
            exec(open("stuCourse1.py").read())
        else:
            Label(course1access_screen, text="Incorrect access code. Please try again.", font=("calibre", 35)).pack()

    course1code = StringVar()
    accessCode_entry = Entry(course1access_screen, textvariable=course1code)
    accessCode_entry.pack()
    accessCode_entry.config(highlightbackground="black")
    Button(course1access_screen, text="Enter", width=20, height=2, command=accessCode_verify).pack()


def course2access():
    global course2access_screen
    course2access_screen = Toplevel(main_screen)
    course2access_screen.title("Access Your Course")
    course2access_screen.geometry("1500x800")
    Label(course2access_screen, text="Get Access to Dr. Ali's Course", bg="lightgray", width="300",
          height="2", font=("Calibre", 70)).pack()
    redStripe = Label(course2access_screen, text=" ", fg='red', bg='indianred', width='300', height='1', font=("Calibre", 50))
    redStripe.pack()
    Label(course2access_screen, text="Please enter your access code below: ", font=("calibre", 35), pady=50).pack()
    Label(course2access_screen, text="Access Code * ", font=("calibre", 25)).pack()

    def accessCode_verify():
        codeInput = course2code.get() # gets the password from user entry
        if codeInput == "54321": # here is where we can set up the access code per course
            Label(course2access_screen, text="Now entering the course...", font=("calibre", 35)).pack()
            time.sleep(1)
            exec(open(".py").read()) #NEED TO SWITCH THIS TO COURSE 2 PAGE
        else:
            Label(course2access_screen, text="Incorrect access code. Please try again.", font=("calibre", 35)).pack()

    course2code = StringVar()
    accessCode_entry = Entry(course2access_screen, textvariable=course2code)
    accessCode_entry.pack()
    accessCode_entry.config(highlightbackground="black")
    Button(course2access_screen, text="Enter", width=20, height=2, command=accessCode_verify).pack()


def course3access():
    global course3access_screen
    course3access_screen = Toplevel(main_screen)
    course3access_screen.title("Access Your Course")
    course3access_screen.geometry("1500x800")
    Label(course3access_screen, text="Get Access to Dr. Jay's Course", bg="lightgray", width="300",
          height="2", font=("Calibre", 70)).pack()
    redStripe = Label(course3access_screen, text=" ", fg='red', bg='indianred', width='300', height='1', font=("Calibre", 50))
    redStripe.pack()
    Label(course3access_screen, text="Please enter your access code below: ", font=("calibre", 35), pady=50).pack()
    Label(course3access_screen, text="Access Code * ", font=("calibre", 25)).pack()

    def accessCode_verify():
        codeInput = course3code.get() # gets the password from user entry
        if codeInput == "67890": # here is where we can set up the access code per course
            Label(course3access_screen, text="Now entering the course...", font=("calibre", 35)).pack()
            time.sleep(1)
            exec(open(".py").read()) #NEED TO SWITCH THIS TO COURSE 3 PAGE
        else:
            Label(course3access_screen, text="Incorrect access code. Please try again.", font=("calibre", 35)).pack()

    course3code = StringVar()
    accessCode_entry = Entry(course3access_screen, textvariable=course3code)
    accessCode_entry.pack()
    accessCode_entry.config(highlightbackground="black")
    Button(course3access_screen, text="Enter", width=20, height=2, command=accessCode_verify).pack()


def course4access():
    global course4access_screen
    course4access_screen = Toplevel(main_screen)
    course4access_screen.title("Access Your Course")
    course4access_screen.geometry("1500x800")
    Label(course4access_screen, text="Get Access to Dr. Duo's Course", bg="lightgray", width="300",
          height="2", font=("Calibre", 70)).pack()
    redStripe = Label(course4access_screen, text=" ", fg='red', bg='indianred', width='300', height='1', font=("Calibre", 50))
    redStripe.pack()
    Label(course4access_screen, text="Please enter your access code below: ", font=("calibre", 35), pady=50).pack()
    Label(course4access_screen, text="Access Code * ", font=("calibre", 25)).pack()

    def accessCode_verify():
        codeInput = course4code.get() # gets the password from user entry
        if codeInput == "09876": # here is where we can set up the access code per course
            Label(course4access_screen, text="Now entering the course...", font=("calibre", 35)).pack()
            time.sleep(1)
            exec(open(".py").read()) #NEED TO SWITCH THIS TO COURSE 4 PAGE
        else:
            Label(course4access_screen, text="Incorrect access code. Please try again.", font=("calibre", 35)).pack()

    course4code = StringVar()
    accessCode_entry = Entry(course4access_screen, textvariable=course4code)
    accessCode_entry.pack()
    accessCode_entry.config(highlightbackground="black")
    Button(course4access_screen, text="Enter", width=20, height=2, command=accessCode_verify).pack()
# ^^^ for the above 4 defs, i can shorten the code by using a nested if/elif statement with the 4 different access
# codes. this will bring ALL students to the same access page instead of having 4 different pages and using the nest i
# can draw them to one of the 4 different class pages depending on the access code that they gave me ?? would have to
# do some extra editing here with the pages and titles, so for now i'll leave it but can go back later


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("1500x800")
    main_screen.title("BronCognito Welcome Page")
    Label(text="Welcome to BronCognito", bg="lightgray", width="300", height="2", font=("Calibre", 70)).pack()
    redStripe = Label(main_screen, text=" ", fg='red', bg='indianred', width='300', height='1', font=("Calibre", 50))
    redStripe.pack()

    lbl = Label(main_screen, text="STUDENTS - To get started, please choose your course from the list below: ",
                fg='black', font=("Calibre", 25))
    lbl.place(x=340, y=265)
    course1 = Button(main_screen, text="Dr. Mourya's Class", height=10, width=30, command=course1access)
    course1.place(x=130, y=320)
    course2 = Button(main_screen, text="Dr. Ali's Class", height=10, width=30, command=course2access)
    course2.place(x=430, y=320)
    course3 = Button(main_screen, text="Dr. Jay's Class", height=10, width=30, command=course3access)
    course3.place(x=730, y=320)
    course4 = Button(main_screen, text="Dr. Duo's Class", height=10, width=30, command=course4access)
    course4.place(x=1030, y=320)

    label = Label(main_screen, text="PROFESSORS - enter your user information below to login: ", fg='black',
                  font=("Calibre", 25))
    label.place(x=400, y=520)
    # work here to add the username and password spots to help the professors login to their accounts (make 4 preset
    # account user and pass. combos. and then draw them to their course home page from the welcome screen depending
    # on which user they are)

    def profLogin_verify():
        username = userInput.get()  # gets the user from entry
        password = passInput.get()  # gets the password from user entry
        if username == "Mourya" and password == "prof1": #manually setting user and pass
            # Label(main_screen, text="Now entering your course...", font=("calibre", 35)).pack()
            time.sleep(1)
            exec(open("profCourse1.py").read())
        #elif username == "Ali" and password == "prof2":
        #elif username == "Jay": ...
        #elif username == "Duo": ...
        else:
            Label(main_screen, text="Invalid username or password. Please try again.", font=("calibre", 25)).place(x=490, y=720)

    userInput = StringVar()
    passInput = StringVar()
    # input_border = Frame(main_screen, background="indianred")
    username_entry = Entry(main_screen, textvariable=userInput)
    username_entry.place(x=610, y=580)
    username_entry.config(highlightbackground="black")
    Label(main_screen, text="Username: ", font=("calibre", 20)).place(x=500, y=575)
    pass_entry = Entry(main_screen, textvariable=passInput)
    pass_entry.place(x=610, y=620)
    pass_entry.config(highlightbackground="black")
    Label(main_screen, text="Password: ", font=("calibre", 20)).place(x=504, y=620)
    Button(main_screen, text="Enter", width=20, height=2, command=profLogin_verify).place(x=614, y=680)

    main_screen.mainloop()

main_account_screen()

