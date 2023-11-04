screen Your_Office:
    frame:
        xalign 0.5 yalign 0.5
        xsize 0.4 ysize 0.4
        # Morning #
        vbox:
            xalign 0.05 yalign 0.05
            text "Morning":
                style "your_text_style2"
                xalign 0.5
            text ""
            textbutton "Test":
                xalign 0.5
                action SetField(persistent, mc.morning, "none")
            text ""
            textbutton "Office":
                yanchor 0.35
                xalign 0.5
                action SetField(persistent, mc.morning, "office")
            if s.cafeteria >= 1:
                textbutton "Cafeteria":
                    xalign 0.5
                    action SetField(persistent, mc.morning, "cafeteria")
            if s.library >= 1:
                textbutton "Library":
                    xalign 0.5
                    action SetField(persistent, mc.morning, "library")
            if s.sex_education >= 1:
                textbutton "Sex\nEducation":
                    text_textalign 0.5
                    xalign 0.5
                    action SetField(persistent, mc.morning, "sex education")
        # Afternoon #
        vbox:
            xalign 0.5 yalign 0.05
            text "Afternoon":
                style "your_text_style2"
                xalign 0.5
            text ""
            textbutton "Test":
                xalign 0.5
                action SetField(persistent, mc.afternoon, "none")
            text ""
            textbutton "Classroom":
                yanchor 0.35
                xalign 0.5
                action SetField(persistent, mc.afternoon, "classroom")
            if s.sport_field >= 1:
                textbutton "Sport Field":
                    action SetField(persistent, mc.afternoon, "sport field")
            if s.gym >= 1:
                textbutton "Gym":
                    xalign 0.5
                    action SetField(persistent, mc.afternoon, "gym")
            text ""
            if s.pool >= 1:
                textbutton "Pool":
                    yanchor 0.35
                    xalign 0.5
                    action SetField(persistent, mc.afternoon, "pool")
        # Evening # 
        vbox:
            xalign 0.95 yalign 0.05
            text "Evening":
                style "your_text_style2"
                xalign 0.5
            text ""
            textbutton "Test":
                xalign 0.5
                action SetField(persistent, mc.evening, "none")
            textbutton "School\nGrounds":
                xalign 0.5
                text_textalign 0.5
                action SetField(persistent, mc.evening, "school grounds")
            if s.dorm >= 1:
                textbutton "Dormitory":
                    xalign 0.5
                    action SetField(persistent, mc.evening, "dormitory")
            if s.bath >= 1:
                textbutton "Bath":
                    xalign 0.5
                    action SetField(persistent, mc.evening, "bath")  
            text ""   
            if s.club == True:
                textbutton "Club":
                    yanchor 0.35
                    xalign 0.5
                    action SetField(persistent, "evening", "club")  
    frame:
        xalign 0.5
        yalign 0.75
        #background Solid("#001c7966")    
        vbox:
            textbutton "Next":
                text_style "your_text_style"
                action Jump("Test")

screen Student_stat:
    frame:
        xalign 0.975
        yalign 0.05
        xsize 0.2
        ysize 0.45
        background Solid("#000000be")
        vbox:
            xalign 0.5
            yalign 0.05
            text "Student Stats"
        vbox:
            xalign 0.975
            yalign 0.05
            text ""
            text ""
            text "Behavior:                  ":
                style "your_text_style1"
            text "Morale:                    ":
                style "your_text_style1"
            text "Academic:                  ":
                style "your_text_style1"
            text "Athletics:                 ":
                style "your_text_style1"
            text "Deviance:                  ":
                style "your_text_style1"
            text "Inhibition:                ":
                style "your_text_style1"
            text "Stress:                    ":
                style "your_text_style1"
            text ""
            text "Population:                ":
                style "your_text_style1"
            text "Staff:                     ":
                style "your_text_style1"
        vbox:
            xalign 0.975
            yalign 0.05
            text ""
            text ""
            text "[st.behavior]/100"
            text "[st.morale]/100"
            text "[st.academics]/100"
            text "[st.athletics]/100"
            text "[st.deviance]/100"
            text "[st.inhibition]"
            text "[st.stress]/100"
            text ""
            text "[st.amount_students]" 
            text "[mc.staff]"

screen Datetime:
    frame:
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
            text "Money:":
                style "your_text_style1"
            text "Reputation:":
                style "your_text_style1"
            text "Staff Support:":
                style "your_text_style1"
        vbox:
            yalign 0.9
            xalign 0.9
            text "[s.money]"
            text "[s.reputation]/150"
            text "[mc.staff_support]/100"
    frame:
        xalign 0.5
        yalign 0.25
        background Solid("#001c7966")
        text "[s.weekday_name], [s.month_name][s.day_name] [s.year_name]"

screen Functions:
    frame:
        xalign 0.025
        yalign 0.5
        xsize 0.2
        background Solid("#001c7966")
        vbox:
            xalign 0.5
            textbutton "Policies" action Jump("Test0") style "custom_textbutton":
                xalign 0.5
                xsize 1.0
                text_style "custom_textbutton_text"
            textbutton "Rules" action Jump("Test0") style "custom_textbutton":
                xalign 0.5
                xsize 1.0
                text_style "custom_textbutton_text"
            textbutton "Buildings" action Jump("Test0") style "custom_textbutton":
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

    # Your_Office your_text_style #
    style.create("your_text_style", style.text)
    style.your_text_style.color = "#929292"
    style.your_text_style.hover_color = "#ffffff"

    # custom_text1 #
    style.create("your_text_style1", style.text)
    style.your_text_style1.color = "#50b0ff"

    # custom_text2 #
    style.create("your_text_style2", style.text)
    style.your_text_style2.color = "#00eeff"