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
            text ""
            textbutton "Office":
                yanchor 0.35
                xalign 0.5
                action SetField(persistent, mc.morning, "office")
                hovered Show("placeholder_text0", displayText = "Talk to your staff member\nto increase staff support\n\n+ staff support")
                unhovered Hide("placeholder_text0")
            if s.cafeteria >= 0:
                textbutton "Cafeteria":
                    xalign 0.5
                    action SetField(persistent, mc.morning, "cafeteria")
                    hovered Show("placeholder_text0", displayText = "Visit the Cafeteria\n\n+ Behavior")
                    unhovered Hide("placeholder_text0")
            if s.library >= 0:
                textbutton "Library":
                    xalign 0.5
                    action SetField(persistent, mc.morning, "library")
                    hovered Show("placeholder_text0", displayText = "Visit the Library\n\n+ Academic\n+ Behavior")
                    unhovered Hide("placeholder_text0")
            if s.sex_education >= 0:
                textbutton "Sex\nEducation":
                    text_textalign 0.5
                    xalign 0.5
                    action SetField(persistent, mc.morning, "sex education")
                    hovered Show("placeholder_text0", displayText = "Give your student a teaching\nabout sex education\n+ Inhibition")
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
                hovered Show("placeholder_text0", displayText = "Visit the Cafeteria\n\n+ Behavior")
                unhovered Hide("placeholder_text0")
            if s.sport_field >= 0:
                textbutton "Sport Field":
                    action SetField(persistent, mc.afternoon, "sport field")
                    hovered Show("placeholder_text0", displayText = "Visit the Cafeteria\n\n+ Behavior")
                    unhovered Hide("placeholder_text0")
            if s.gym >= 0:
                textbutton "Gym":
                    xalign 0.5
                    action SetField(persistent, mc.afternoon, "gym")
                    hovered Show("placeholder_text0", displayText = "Visit the Cafeteria\n\n+ Behavior")
                    unhovered Hide("placeholder_text0")
            text ""
            if s.pool >= 0:
                textbutton "Pool":
                    yanchor 0.35
                    xalign 0.5
                    action SetField(persistent, mc.afternoon, "pool")
                    hovered Show("placeholder_text0", displayText = "Visit the Cafeteria\n\n+ Behavior")
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
                hovered Show("placeholder_text0", displayText = "Visit the Cafeteria\n\n+ Behavior")
                unhovered Hide("placeholder_text0")
            if s.dorm >= 0:
                textbutton "Dormitory":
                    xalign 0.5
                    action SetField(persistent, mc.evening, "dormitory")
                    hovered Show("placeholder_text0", displayText = "Visit the Cafeteria\n\n+ Behavior")
                    unhovered Hide("placeholder_text0")
            if s.bath >= 0:
                textbutton "Bath":
                    xalign 0.5
                    action SetField(persistent, mc.evening, "bath")  
                    hovered Show("placeholder_text0", displayText = "Visit the Cafeteria\n\n+ Behavior")
                    unhovered Hide("placeholder_text0")
            text ""   
            if s.club == False:
                textbutton "Club":
                    yanchor 0.35
                    xalign 0.5
                    action SetField(persistent, mc.evening, "club")  
                    hovered Show("placeholder_text0", displayText = "Visit the Cafeteria\n\n+ Behavior")
                    unhovered Hide("placeholder_text0")
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
    frame:
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
    if s.upgrade_building_image == "classroom":
        add "building_classrooms.jpg":
            xalign 0.9
    elif s.upgrade_building_image == "dormitory":
        add "building_dormitory.jpg":
            xalign 0.9
    else:
        add "blank.png"
    vbox at move_from_left:
        frame:
            textbutton "Buildings"
        frame:
            textbutton "Bath Area"
                #action Show("")
        frame:
            textbutton "Classroom":
                action SetField(persistent, s.upgrade_building_image, "classroom")
        frame:
            textbutton "Dormitory":
                action SetField(persistent, s.upgrade_building_image, "dormitory")
        frame:
            textbutton "Gym"
        frame:
            textbutton "Library"
        frame:
            textbutton "Pool"
        frame:
            textbutton "School Groudns"
        frame:
            textbutton "Security"
        frame:
            textbutton "Sports Fields"
        textbutton "Back":
            action Jump("Your_Office")

screen placeholder_text0:
    default displayText0 = ""
    vbox:
        xalign 0.025
        yalign 0.025
        frame:
            text displayText

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