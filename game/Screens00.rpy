screen Your_Office:
    frame at fading:
        xalign 0.5 yalign 0.5
        xsize 0.4 ysize 0.4
        # Morning #
        vbox:
            xalign 0.05 yalign 0.05
            text "Morning":
                style "your_text_style2"
                xalign 0.5
            text ""
            text ""
            textbutton "Office":
                yanchor 0.35
                xalign 0.5
                action SetField(persistent, mc.morning, "office")
                hovered Show("placeholder_text0", displayText = "Talk to your staff member\nto increase staff support\n\n+ staff support")
                unhovered Hide("placeholder_text0")
            if s.gym >= 0:
                textbutton "Gym":
                    xalign 0.5
                    action SetField(persistent, mc.morning, "gym")
                    hovered Show("placeholder_text0", displayText = "Check out gymnastic\n\n+ Athlethic\n-Inhibition")
                    unhovered Hide("placeholder_text0")
            if s.library >= 0:
                textbutton "Library":
                    xalign 0.5
                    action SetField(persistent, mc.morning, "library")
                    hovered Show("placeholder_text0", displayText = "Learn something new\n\n+ Academic")
                    unhovered Hide("placeholder_text0")
            if s.sex_education >= 0:
                textbutton "Sex\nEducation":
                    text_textalign 0.5
                    xalign 0.5
                    action SetField(persistent, mc.morning, "sex education")
                    hovered Show("placeholder_text0", displayText = "Give your student a teaching\nabout sex education\n- Inhibition\n+ Deviance")
                    unhovered Hide("placeholder_text0")
        # Afternoon #
        vbox:
            xalign 0.5 yalign 0.05
            text "Afternoon":
                style "your_text_style2"
                xalign 0.5
            text ""
            text ""
            textbutton "Classroom":
                yanchor 0.35
                xalign 0.5
                action SetField(persistent, mc.afternoon, "classroom")
                hovered Show("placeholder_text0", displayText = "Attend to your students\nchecking how their studies\n\n+ Academic\n+ Behavior")
                unhovered Hide("placeholder_text0")
            if s.sport_field >= 0:
                textbutton "Sport Field":
                    action SetField(persistent, mc.afternoon, "sport field")
                    hovered Show("placeholder_text0", displayText = "Jog around the Sport Field\n\n+ Athlethic\n+ Morale")
                    unhovered Hide("placeholder_text0")
            if s.pool >= 0:
                textbutton "Pool":
                    xalign 0.5
                    action SetField(persistent, mc.afternoon, "pool")
                    hovered Show("placeholder_text0", displayText = "Visit the swiming pool\n\n+ Athlethic\n- Inhibition")
                    unhovered Hide("placeholder_text0")
            text ""
            if s.cafeteria >= 0:
                textbutton "Cafeteria":
                    yanchor 0.35
                    xalign 0.5
                    action SetField(persistent, mc.afternoon, "cafeteria")
                    hovered Show("placeholder_text0", displayText = "Chill and eat at the Cafeteria\n\n+ Behavior\n+ Morale\n- Athlethic")
                    unhovered Hide("placeholder_text0")
        # Evening # 
        vbox:
            xalign 0.95 yalign 0.05
            text "Evening":
                style "your_text_style2"
                xalign 0.5
            text ""
            textbutton "School\nGrounds":
                xalign 0.5
                text_textalign 0.5
                action SetField(persistent, mc.evening, "school grounds")
                hovered Show("placeholder_text0", displayText = "Take a walk outside\n\n+ Behavior\n+ Morale")
                unhovered Hide("placeholder_text0")
            if s.dorm >= 0:
                textbutton "Dormitory":
                    xalign 0.5
                    action SetField(persistent, mc.evening, "dormitory")
                    hovered Show("placeholder_text0", displayText = "Check out the dormitory\n\n+ Behavior\n+ Academic")
                    unhovered Hide("placeholder_text0")
            if s.bath >= 0:
                textbutton "Bath":
                    xalign 0.5
                    action SetField(persistent, mc.evening, "bath")  
                    hovered Show("placeholder_text0", displayText = "Relax in the public bath\n\n+ Morale\n- Inhibition")
                    unhovered Hide("placeholder_text0")
            text ""   
            if s.club == False:
                textbutton "Club":
                    yanchor 0.35
                    xalign 0.5
                    action SetField(persistent, mc.evening, "club") 
                    hovered Show("placeholder_text0", displayText = "Club")
                    unhovered Hide("placeholder_text0")
    frame:
        xalign 0.5
        yalign 0.75
        #background Solid("#001c7966")    
        vbox:
            textbutton "Next":
                text_style "your_text_style"
                action Jump("Next")

screen Student_stat:
    frame at move_from_right:
        xalign 0.975
        yalign 0.05
        xsize 0.25
        ysize 0.5
        background Solid("#000000be")
        vbox:
            xalign 0.5
            yalign 0.05
            text "Student Stats"
        vbox:
            xalign 0.15
            yalign 0.05
            text ""
            text ""
            textbutton "Behavior:                  ":
                action Jump("Your_Office")
                hovered Show("placeholder_text0", displayText = "This is how obedient\nthe students can be")
                unhovered Hide("placeholder_text0")
                text_color "#50b0ff"
            textbutton "Morale:                    ":
                yanchor 0.25
                action Jump("Your_Office")
                hovered Show("placeholder_text0", displayText = "This is the general happiness\nof the students")
                unhovered Hide("placeholder_text0")
                text_color "#50b0ff"
            textbutton "Academic:                  ":
                yanchor 0.5
                action Jump("Your_Office")
                hovered Show("placeholder_text0", displayText = "This show how smart your student")
                unhovered Hide("placeholder_text0")
                text_color "#50b0ff"
            textbutton "Athletics:                 ":
                yanchor 0.75
                action Jump("Your_Office")
                hovered Show("placeholder_text0", displayText = "This show your student physical health")
                unhovered Hide("placeholder_text0")
                text_color "#50b0ff"
            textbutton "Deviance:                  ":
                yanchor 1.0
                action Jump("Your_Office")
                hovered Show("placeholder_text0", displayText = "This show how's your student\nis used to deprived sexual behavior")
                unhovered Hide("placeholder_text0")
                text_color "#50b0ff"
            textbutton "Inhibition:                ":
                yanchor 1.25
                action Jump("Your_Office")
                hovered Show("placeholder_text0", displayText = "A measure\nto show the student modesty")
                unhovered Hide("placeholder_text0")
                text_color "#50b0ff"
            textbutton "Lust:                    ":
                yanchor 1.5
                action Jump("Your_Office")
                hovered Show("placeholder_text0", displayText = "How horny are the students")
                unhovered Hide("placeholder_text0")
                text_color "#50b0ff"
            textbutton "Stress:                ":
                yanchor 1.75
                action Jump("Your_Office")
                hovered Show("placeholder_text0", displayText = "This show your stress or under pressure")
                unhovered Hide("placeholder_text0")
                text_color "#50b0ff"
            text ""
            textbutton "Population:                ":
                yanchor 1.9
                action Jump("Your_Office")
                hovered Show("placeholder_text0", displayText = "This show how many students\nbe studying in your school")
                unhovered Hide("placeholder_text0")
                text_color "#50b0ff"
            textbutton "Staff:                     ":
                yanchor 2.15
                action Jump("Your_Office")
                hovered Show("placeholder_text0", displayText = "How many employees\nor staff you have hired")
                unhovered Hide("placeholder_text0")
                text_color "#50b0ff"
        vbox:
            xalign 0.9
            yalign 0.05
            text ""
            text ""
            text "[st.behavior]/100"
            text "[st.morale]/100"
            text "[st.academics]/100"
            text "[st.athletics]/100"
            text "[st.deviance]/100"
            text "[st.inhibition]"
            text "[st.lust]"
            text "[st.stress]/100"
            text ""
            text "[st.amount_students]" 
            text "[mc.staff]"

screen Datetime:
    frame at move_from_top0:
        xalign 0.5
        yalign 0.025
        xsize 0.25
        ysize 0.2
        background Solid("#000000be")
        vbox:
            xalign 0.5
            yalign 0.1
            text "[s.name] Academy"
        vbox:
            yalign 0.9
            xalign 0.1
            textbutton "Money:":
                yanchor -0.5
                text_color "#50b0ff"
                action Jump("Your_Office")
                hovered Show("placeholder_text0", displayText = "This show how much $$$ you have\nYou can use this to buy more buildings")
                unhovered Hide("placeholder_text0")
            textbutton "Reputation:":
                yanchor -0.3
                text_color "#50b0ff"
                action Jump("Your_Office")
                hovered Show("placeholder_text0", displayText = "This show how popular your school are\nThis can help you attract more student\nto your school to generate revenue")
                unhovered Hide("placeholder_text0")
            textbutton "Staff Support:":
                yanchor -0.075
                text_color "#50b0ff"
                action Jump("Your_Office")
                hovered Show("placeholder_text0", displayText = "This show how much support\nyou have from your staff\nYou can use the power to enforce rules\nor policies to your school")
                unhovered Hide("placeholder_text0")
        vbox:
            yalign 0.9
            xalign 0.9
            text "[s.money]"
            text "[s.reputation]/150"
            text "[mc.staff_support]/100"
    frame at move_from_top1:
        xalign 0.5
        yalign 0.25
        background Solid("#001c7966")
        text "[s.weekday_name], [s.month_name][s.day_name] [s.year_name]"

screen Functions:
    frame at move_from_left:
        yalign 0.5
        xsize 0.2
        background Solid("#001c7966")
        vbox:
            spacing 10
            xalign 0.5
            textbutton "Policies" action Jump("Test0") style "custom_textbutton":
                xalign 0.5
                xsize 1.0
                text_style "custom_textbutton_text"
            textbutton "Rules" action Jump("Test0") style "custom_textbutton":
                xalign 0.5
                xsize 1.0
                text_style "custom_textbutton_text"
            textbutton "Buildings" action Jump("Buildings") style "custom_textbutton":
                xalign 0.5
                xsize 1.0
                text_style "custom_textbutton_text"
            textbutton "Clubs" action Jump("Test0") style "custom_textbutton":
                xalign 0.5
                xsize 1.0
                text_style "custom_textbutton_text"
            textbutton "Unlocks" action Jump("Test0") style "custom_textbutton":
                xalign 0.5
                xsize 1.0
                text_style "custom_textbutton_text" 
            textbutton "Status Report" action Jump("Test0") style "custom_textbutton":
                xalign 0.5
                xsize 1.0
                text_style "custom_textbutton_text" 
            textbutton "Financial Report" action Jump("Test0") style "custom_textbutton":
                xalign 0.5
                xsize 1.0
                text_style "custom_textbutton_text" 

screen Buildings:
    vbox at move_from_left:
        spacing 10
        frame:
            xsize 0.15
            ysize 0.1
            textbutton "Buildings":
                text_color "#FFFFFF"
                xalign 0.5
                yalign 0.5
        frame:
            textbutton "Bath Area":
                action [SetField(persistent, s.upgrade_building_image, "bath_area"),
                Hide("classroom"), Hide("dormitory"), Hide("gym"), Hide("library"), Hide("cafeteria"),
                Hide("pool"), Hide("school_grounds"), Hide("security"), Hide("surveillance"),
                Hide("sports_field"), Show("bath_area")]
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            textbutton "Cafeteria":
                action [SetField(persistent, s.upgrade_building_image, "cafeteria"), Hide("classroom"),
                Hide("building_classrooms"), Hide("bath_area"), Hide("gym"), Hide("library"),
                Hide("pool"), Hide("school_grounds"), Hide("security"), Hide("surveillance"),
                Hide("dormitory"), Hide("sports_field"), Show("cafeteria")]
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            textbutton "Classroom":
                action [SetField(persistent, s.upgrade_building_image, "classroom"), 
                Hide("building_classrooms"), Hide("bath_area"), Hide("gym"), Hide("library"),
                Hide("pool"), Hide("school_grounds"), Hide("security"), Hide("surveillance"),
                Hide("dormitory"), Hide("cafeteria"), Hide("sports_field"), Show("classroom")]
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            textbutton "Dormitory":
                action [SetField(persistent, s.upgrade_building_image, "dormitory"), 
                Hide("classroom"), Hide("bath_area"), Hide("gym"), Hide("library"),
                Hide("pool"), Hide("school_grounds"), Hide("security"), Hide("surveillance"),
                Hide("cafeteria"), Hide("sports_field"), Show("dormitory")]
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            textbutton "Gym":
                action [SetField(persistent, s.upgrade_building_image, "gym"),
                Hide("classroom"), Hide("bath_area"), Hide("dormitory"), Hide("library"),
                Hide("pool"), Hide("school_grounds"), Hide("security"), Hide("surveillance"),
                Hide("cafeteria"), Hide("sports_field"), Show("gym")]
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            textbutton "Library":
                action [SetField(persistent, s.upgrade_building_image, "library"),
                Hide("classroom"), Hide("bath_area"), Hide("dormitory"), Hide("gym"),
                Hide("pool"), Hide("school_grounds"), Hide("security"),
                Hide("cafeteria"), Hide("sports_field"), Show("library")]
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            textbutton "Pool":
                action [SetField(persistent, s.upgrade_building_image, "pool"),
                Hide("classroom"), Hide("bath_area"), Hide("dormitory"), Hide("gym"),
                Hide("library"), Hide("school_grounds"), Hide("security"), Hide("surveillance"),
                Hide("cafeteria"), Hide("sports_field"), Show("pool")]
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            textbutton "School Grounds":
                action [SetField(persistent, s.upgrade_building_image, "school_grounds"),
                Hide("classroom"), Hide("bath_area"), Hide("dormitory"), Hide("gym"),
                Hide("pool"), Hide("library"), Hide("security"), Hide("surveillance"),
                Hide("cafeteria"), Hide("sports_field"), Show("school_grounds")]
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            textbutton "Security":
                action [SetField(persistent, s.upgrade_building_image, "security"),
                Hide("classroom"), Hide("bath_area"), Hide("dormitory"), Hide("gym"),
                Hide("pool"), Hide("school_grounds"), Hide("library"), Hide("surveillance"),
                Hide("cafeteria"), Hide("sports_field"), Show("security")]
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            textbutton "Sports Fields":
                action [SetField(persistent, s.upgrade_building_image, "sports_field"),
                Hide("classroom"), Hide("bath_area"), Hide("dormitory"), Hide("gym"),
                Hide("pool"), Hide("school_grounds"), Hide("security"), Hide("surveillance"),
                Hide("cafeteria"), Hide("library"), Show("sports_field")]
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        if s.surveillance_option == True:
            frame:
                textbutton "surveillance":
                    action [SetField(persistent, s.upgrade_building_image, "surveillance"),
                    Hide("classroom"), Hide("bath_area"), Hide("dormitory"), Hide("gym"),
                    Hide("pool"), Hide("school_grounds"), Hide("security"),
                    Hide("cafeteria"), Hide("library"), Show("surveillance")]
                    text_style "custom_textbutton_text0"
                    style "custom_textbutton0"
        frame:
            textbutton "Back":
                action [SetField(persistent, s.upgrade_building_image, "None"),
                Hide("classroom"), Hide("bath_area"), Hide("dormitory"), Hide("gym"),
                Hide("pool"), Hide("school_grounds"), Hide("security"), Hide("surveillance"),
                Hide("cafeteria"), Hide("library"), Hide("sports_field"), Jump("Your_Office")]
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
screen classroom:
    frame: 
        xalign 0.9
        yalign 0.25
        add "building_classrooms.jpg"
screen dormitory:
    frame:
        xalign 0.9
        yalign 0.25
        add "building_dormitory.jpg"
screen bath_area:
    frame:
        xalign 0.9
        yalign 0.25
        add "building_bath.jpg"
screen cafeteria:
    frame:
        xalign 0.9
        yalign 0.25
        add "building_cafeteria.jpg"
screen gym:
    frame:
        xalign 0.9
        yalign 0.25
        add "building_gym.jpg"
screen school_grounds:
    frame:
        xalign 0.9
        yalign 0.25
        add "building_grounds.jpg"
screen library:
    frame:
        xalign 0.9
        yalign 0.25
        add "building_library.jpg"
screen pool:
    frame:
        xalign 0.9
        yalign 0.25
        add "building_pool.jpg"
screen sports_field:
    frame:
        xalign 0.9
        yalign 0.25
        add "building_sports_field.jpg"
screen surveillance:
    frame:
        xalign 0.9
        yalign 0.25
        add "building_surveillance.jpg"
screen security:
    frame:
        xalign 0.9
        yalign 0.25
        add "building_security.jpg"

screen placeholder_text0:
    default displayText0 = ""
    vbox:
        xalign 0.025
        yalign 0.025
        frame:
            text displayText

transform move_from_top0:
    on show:
        yalign -0.5
        linear 0.5 yalign 0.025
    on hide:
        yalign 0.025
        linear 0.5 yalign -0.5

transform move_from_top1:
    on show:
        yalign -0.5
        linear 0.5 yalign 0.25
    on hide:
        yalign 0.25
        linear 0.5 yalign -0.5

transform move_from_right:
    on show:
        xalign 1.5
        linear 0.5 xalign 0.975
    on hide:
        xalign 0.975
        linear 0.5 xalign 1.5

transform fading:
    on show:
        alpha 0.0
        linear 0.25 alpha 1.0
    on hide:
        linear 0.25 alpha 0.0

transform move_from_left:
    on show:
        xalign -0.5
        linear 0.5 xalign 0.025
    on hide:
        xalign 0.025
        linear 0.5 xalign -0.5



init python:
    # Functions custom_textbutton #
    style.custom_textbutton = Style(style.button)
    style.custom_textbutton.background = Frame("choice_idle_background.png", 150, 8, 150, 8, tile=False)
    style.custom_textbutton.hover_background = Frame("choice_hover_background.png", 150, 8, 150, 8, tile=False)

    # Functions custom_textbutton_text #
    style.custom_textbutton_text = Style(style.button_text)
    style.custom_textbutton_text.color = "#888888"
    style.custom_textbutton_text.hover_color = "#ffffff"
    style.custom_textbutton_text.xalign = 0.5

    # Buildings custom_textbutton0 #
    style.custom_textbutton0 = Style(style.button)
    style.custom_textbutton0.background = "#646da377"
    style.custom_textbutton0.hover_background = "#a1a1a1"
    style.custom_textbutton0.selected_background = "#5a5a5a"

    # Buildings custom_textbutton_text0 #
    style.custom_textbutton_text0 = Style(style.button_text)
    style.custom_textbutton_text0.color = "#888888"
    style.custom_textbutton_text0.hover_color = "#ffffff"
    style.custom_textbutton_text0.selected_idle_color = "#ffffff"

    # Your_Office your_text_style #
    style.create("your_text_style", style.text)
    style.your_text_style.color = "#929292"
    style.your_text_style.hover_color = "#ffffff"

    # custom_text2 #
    style.create("your_text_style2", style.text)
    style.your_text_style2.color = "#00eeff"