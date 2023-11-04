label Your_Office:
    scene office
    show screen Your_Office
    show screen Student_stat
    show screen Datetime
    show screen Functions
    pause
    jump Your_Office

label Test:
    $ s.next_day()
    if s.student_enter ==     True:
        $ s.student_enter = False
        $ s.Student_population()
    "Hello World!"
    jump Your_Office

label Hide_everything:
    hide screen Your_Office
    hide screen Student_stat
    hide screen Datetime
    hide screen Functions
    pause
    jump Your_Office