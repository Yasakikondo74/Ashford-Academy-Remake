label Your_Office:
    hide screen Policies
    hide screen Buildings
    scene ashford
    show screen Your_Office
    show screen Student_stat
    show screen Datetime
    show screen Functions
    pause
    jump Your_Office

label Next:
    hide ashford
    hide screen Your_Office
    hide screen Student_stat
    hide screen Datetime
    hide screen Functions
    $ s.next_day()
    if s.student_enter == True:
        $ s.student_enter = False
        $ s.Student_population()
    pause
    jump Events

label Test0:
    hide screen Your_Office
    hide screen Student_stat
    hide screen Datetime
    hide screen Functions
    pause
    jump Your_Office

label Buildings:
    hide screen Your_Office
    hide screen Student_stat
    hide screen Datetime
    hide screen Functions
    show screen Buildings
    pause
    jump Buildings

label Events:
    "Events"
    jump Your_Office

label Policies:
    hide screen Your_Office
    hide screen Student_stat
    hide screen Datetime
    hide screen Functions
    show screen Policies
    pause
    jump Policies