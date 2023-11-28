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

label Policies_Options_teacher_leeway_check:
    $ s.change_teacher_leeway()
    jump Policies

label Policies_Options_dresscode_check:
    $ s.change_dresscode()
    jump Policies

label depiction_of_the_human_body_check:
    $ s.change_depiction_of_the_human_body()
    jump Policies

label entrance_requirement_strenght_check:
    $ s.change_entrance_requirement_strenght()
    jump Policies

label entrance_requirement_focus_check:
    $ s.change_entrance_requirement_focus()
    jump Policies

label learning_materials_check:
    $ s.change_learning_materials()
    jump Policies

label staff_salary_check:
    $ s.change_staff_salary()
    jump Policies

label class_size_check:
    $ s.change_class_size()
    jump Policies