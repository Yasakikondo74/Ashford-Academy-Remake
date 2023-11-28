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
                hovered Show("placeholder_text", displayText = "Talk to your staff member\nto increase staff support\n\n+ staff support")
                unhovered Hide("placeholder_text")
            if s.gym >= 1:
                textbutton "Gym":
                    xalign 0.5
                    action SetField(persistent, mc.morning, "gym")
                    hovered Show("placeholder_text", displayText = "Check out gymnastic\n\n+ Athlethic\n-Inhibition")
                    unhovered Hide("placeholder_text")
            if s.library >= 1:
                textbutton "Library":
                    xalign 0.5
                    action SetField(persistent, mc.morning, "library")
                    hovered Show("placeholder_text", displayText = "Learn something new\n\n+ Academic")
                    unhovered Hide("placeholder_text")
            if s.sex_education >= 1:
                textbutton "Sex\nEducation":
                    text_textalign 0.5
                    xalign 0.5
                    action SetField(persistent, mc.morning, "sex education")
                    hovered Show("placeholder_text", displayText = "Give your student a teaching\nabout sex education\n- Inhibition\n+ Deviance")
                    unhovered Hide("placeholder_text")
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
                hovered Show("placeholder_text", displayText = "Attend to your students\nchecking how their studies\n\n+ Academic\n+ Behavior")
                unhovered Hide("placeholder_text")
            if s.sport_field >= 1:
                textbutton "Sport Field":
                    action SetField(persistent, mc.afternoon, "sport field")
                    hovered Show("placeholder_text", displayText = "Jog around the Sport Field\n\n+ Athlethic\n+ Morale")
                    unhovered Hide("placeholder_text")
            if s.pool >= 1:
                textbutton "Pool":
                    xalign 0.5
                    action SetField(persistent, mc.afternoon, "pool")
                    hovered Show("placeholder_text", displayText = "Visit the swiming pool\n\n+ Athlethic\n- Inhibition")
                    unhovered Hide("placeholder_text")
            text ""
            if s.cafeteria >= 1:
                textbutton "Cafeteria":
                    yanchor 0.35
                    xalign 0.5
                    action SetField(persistent, mc.afternoon, "cafeteria")
                    hovered Show("placeholder_text", displayText = "Chill and eat at the Cafeteria\n\n+ Behavior\n+ Morale\n- Athlethic")
                    unhovered Hide("placeholder_text")
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
                hovered Show("placeholder_text", displayText = "Take a walk outside\n\n+ Behavior\n+ Morale")
                unhovered Hide("placeholder_text")
            if s.dorm >= 1:
                textbutton "Dormitory":
                    xalign 0.5
                    action SetField(persistent, mc.evening, "dormitory")
                    hovered Show("placeholder_text", displayText = "Check out the dormitory\n\n+ Behavior\n+ Academic")
                    unhovered Hide("placeholder_text")
            if s.bath >= 1:
                textbutton "Bath":
                    xalign 0.5
                    action SetField(persistent, mc.evening, "bath")  
                    hovered Show("placeholder_text", displayText = "Relax in the public bath\n\n+ Morale\n- Inhibition")
                    unhovered Hide("placeholder_text")
            text ""   
            if s.club == True:
                textbutton "Club":
                    yanchor 0.35
                    xalign 0.5
                    action SetField(persistent, mc.evening, "club") 
                    hovered Show("placeholder_text", displayText = "Club")
                    unhovered Hide("placeholder_text")
    frame:
        xalign 0.5
        yalign 0.75
        #background Solid("#001c7966")    
        vbox:
            textbutton "Done Planning":
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
                hovered Show("placeholder_text", displayText = "This is how obedient\nthe students can be")
                unhovered Hide("placeholder_text")
                text_color "#50b0ff"
            textbutton "Morale:                    ":
                yanchor 0.25
                action Jump("Your_Office")
                hovered Show("placeholder_text", displayText = "This is the general happiness\nof the students")
                unhovered Hide("placeholder_text")
                text_color "#50b0ff"
            textbutton "Academic:                  ":
                yanchor 0.5
                action Jump("Your_Office")
                hovered Show("placeholder_text", displayText = "This show how smart your student")
                unhovered Hide("placeholder_text")
                text_color "#50b0ff"
            textbutton "Athletics:                 ":
                yanchor 0.75
                action Jump("Your_Office")
                hovered Show("placeholder_text", displayText = "This show your student physical health")
                unhovered Hide("placeholder_text")
                text_color "#50b0ff"
            textbutton "Deviance:                  ":
                yanchor 1.0
                action Jump("Your_Office")
                hovered Show("placeholder_text", displayText = "This show how's your student\nis used to deprived sexual behavior")
                unhovered Hide("placeholder_text")
                text_color "#50b0ff"
            textbutton "Inhibition:                ":
                yanchor 1.25
                action Jump("Your_Office")
                hovered Show("placeholder_text", displayText = "A measure\nto show the student modesty")
                unhovered Hide("placeholder_text")
                text_color "#50b0ff"
            textbutton "Lust:                    ":
                yanchor 1.5
                action Jump("Your_Office")
                hovered Show("placeholder_text", displayText = "How horny are the students")
                unhovered Hide("placeholder_text")
                text_color "#50b0ff"
            textbutton "Stress:                ":
                yanchor 1.75
                action Jump("Your_Office")
                hovered Show("placeholder_text", displayText = "This show your stress or under pressure")
                unhovered Hide("placeholder_text")
                text_color "#50b0ff"
            text ""
            textbutton "Population:                ":
                yanchor 1.9
                action Jump("Your_Office")
                hovered Show("placeholder_text", displayText = "This show how many students\nbe studying in your school")
                unhovered Hide("placeholder_text")
                text_color "#50b0ff"
            textbutton "Staff:                     ":
                yanchor 2.15
                action Jump("Your_Office")
                hovered Show("placeholder_text", displayText = "How many employees\nor staff you have hired")
                unhovered Hide("placeholder_text")
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
                hovered Show("placeholder_text", displayText = "This show how much $$$ you have\nYou can use this to buy more buildings")
                unhovered Hide("placeholder_text")
            textbutton "Reputation:":
                yanchor -0.3
                text_color "#50b0ff"
                action Jump("Your_Office")
                hovered Show("placeholder_text", displayText = "This show how popular your school are\nThis can help you attract more student\nto your school to generate revenue")
                unhovered Hide("placeholder_text")
            textbutton "Staff Support:":
                yanchor -0.075
                text_color "#50b0ff"
                action Jump("Your_Office")
                hovered Show("placeholder_text", displayText = "This show how much support\nyou have from your staff\nYou can use the power to enforce rules\nor policies to your school")
                unhovered Hide("placeholder_text")
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
            textbutton "Policies" action Jump("Policies") style "custom_textbutton":
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
    frame at fading:
        xsize 0.135
        ysize 0.06
        xalign 0.935
        yalign 0.05
        textbutton "Buy/Upgrades":
            action NullAction()
            text_style "custom_textbutton_text0"
            style "custom_textbutton0"
    vbox at move_from_left:
        spacing 10
        frame:
            xsize 0.15
            ysize 0.1
            textbutton "Buildings":
                action NullAction()
                text_color "#FFFFFF"
                xalign 0.5
                yalign 0.5
        frame:
            xalign 1.0
            textbutton "Bath Area":
                action [SetLocalVariable(upgrade_building_image, "bath_area"),
                Hide("classroom"), Hide("dormitory"), Hide("gym"), Hide("library"), Hide("cafeteria"),
                Hide("pool"), Hide("school_grounds"), Hide("security"), Hide("surveillance"),
                Hide("sports_field"), Show("bath_area")]
                hovered Show("placeholder_text0", displayText0 = "Level [s.bath]")
                unhovered Hide("placeholder_text0")
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            xalign 1.0
            textbutton "Cafeteria":
                action [SetLocalVariable(upgrade_building_image, "cafeteria"), Hide("classroom"),
                Hide("building_classrooms"), Hide("bath_area"), Hide("gym"), Hide("library"),
                Hide("pool"), Hide("school_grounds"), Hide("security"), Hide("surveillance"),
                Hide("dormitory"), Hide("sports_field"), Show("cafeteria")]
                hovered Show("placeholder_text1", displayText1 = "Level [s.cafeteria]")
                unhovered Hide("placeholder_text1")
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            xalign 1.0
            textbutton "Classroom":
                action [SetLocalVariable(upgrade_building_image, "classroom"), 
                Hide("building_classrooms"), Hide("bath_area"), Hide("gym"), Hide("library"),
                Hide("pool"), Hide("school_grounds"), Hide("security"), Hide("surveillance"),
                Hide("dormitory"), Hide("cafeteria"), Hide("sports_field"), Show("classroom")]
                hovered Show("placeholder_text2", displayText2 = "Level [s.classroom]")
                unhovered Hide("placeholder_text2")
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            xalign 1.0
            textbutton "Dormitory":
                action [SetLocalVariable(upgrade_building_image, "dormitory"), 
                Hide("classroom"), Hide("bath_area"), Hide("gym"), Hide("library"),
                Hide("pool"), Hide("school_grounds"), Hide("security"), Hide("surveillance"),
                Hide("cafeteria"), Hide("sports_field"), Show("dormitory")]
                hovered Show("placeholder_text3", displayText3 = "Level [s.dorm]")
                unhovered Hide("placeholder_text3")
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            xalign 1.0
            textbutton "Gym":
                action [SetLocalVariable(upgrade_building_image, "gym"),
                Hide("classroom"), Hide("bath_area"), Hide("dormitory"), Hide("library"),
                Hide("pool"), Hide("school_grounds"), Hide("security"), Hide("surveillance"),
                Hide("cafeteria"), Hide("sports_field"), Show("gym")]
                hovered Show("placeholder_text4", displayText4 = "Level [s.gym]")
                unhovered Hide("placeholder_text4")
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            xalign 1.0
            textbutton "Library":
                action [SetLocalVariable(upgrade_building_image, "library"),
                Hide("classroom"), Hide("bath_area"), Hide("dormitory"), Hide("gym"),
                Hide("pool"), Hide("school_grounds"), Hide("security"),
                Hide("cafeteria"), Hide("sports_field"), Show("library")]
                hovered Show("placeholder_text5", displayText5 = "Level [s.library]")
                unhovered Hide("placeholder_text5")
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            xalign 1.0
            textbutton "Pool":
                action [SetLocalVariable(upgrade_building_image, "pool"),
                Hide("classroom"), Hide("bath_area"), Hide("dormitory"), Hide("gym"),
                Hide("library"), Hide("school_grounds"), Hide("security"), Hide("surveillance"),
                Hide("cafeteria"), Hide("sports_field"), Show("pool")]
                hovered Show("placeholder_text6", displayText6 = "Level [s.pool]")
                unhovered Hide("placeholder_text6")
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            xalign 1.0
            textbutton "School Grounds":
                action [SetLocalVariable(upgrade_building_image, "school_grounds"),
                Hide("classroom"), Hide("bath_area"), Hide("dormitory"), Hide("gym"),
                Hide("pool"), Hide("library"), Hide("security"), Hide("surveillance"),
                Hide("cafeteria"), Hide("sports_field"), Show("school_grounds")]
                hovered Show("placeholder_text7", displayText7 = "Level [s.school_grounds]")
                unhovered Hide("placeholder_text7")
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            xalign 1.0
            textbutton "Security":
                action [SetLocalVariable(upgrade_building_image, "security"),
                Hide("classroom"), Hide("bath_area"), Hide("dormitory"), Hide("gym"),
                Hide("pool"), Hide("school_grounds"), Hide("library"), Hide("surveillance"),
                Hide("cafeteria"), Hide("sports_field"), Show("security")]
                hovered Show("placeholder_text8", displayText8 = "Level [s.security]")
                unhovered Hide("placeholder_text8")
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            xalign 1.0
            textbutton "Sports Fields":
                action [SetLocalVariable(upgrade_building_image, "sports_field"),
                Hide("classroom"), Hide("bath_area"), Hide("dormitory"), Hide("gym"),
                Hide("pool"), Hide("school_grounds"), Hide("security"), Hide("surveillance"),
                Hide("cafeteria"), Hide("library"), Show("sports_field")]
                hovered Show("placeholder_text9", displayText9 = "Level [s.sport_field]")
                unhovered Hide("placeholder_text9")
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        if s.surveillance_option == True:
            frame:
                xalign 1.0
                textbutton "Surveillance":
                    action [SetLocalVariable(upgrade_building_image, "surveillance"),
                    Hide("classroom"), Hide("bath_area"), Hide("dormitory"), Hide("gym"),
                    Hide("pool"), Hide("school_grounds"), Hide("security"),
                    Hide("cafeteria"), Hide("library"), Show("surveillance")]
                    hovered Show("placeholder_text10", displayText10 = "Level [s.surveillance]")
                    unhovered Hide("placeholder_text10")
                    text_style "custom_textbutton_text0"
                    style "custom_textbutton0"
        frame:
            xalign 1.0
            textbutton "Back":
                action [SetLocalVariable(upgrade_building_image, "None"),
                Hide("classroom"), Hide("bath_area"), Hide("dormitory"), Hide("gym"),
                Hide("pool"), Hide("school_grounds"), Hide("security"), Hide("surveillance"),
                Hide("cafeteria"), Hide("library"), Hide("sports_field"), Jump("Your_Office")]
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"         

screen Policies:
    vbox at move_from_top2:
        spacing 5
        frame:
            xsize 0.2
            ysize 0.1
            xalign 0.5
            textbutton "School Policies":
                action NullAction()
                text_color "#FFFFFF"
                xalign 0.5
                yalign 0.5
        frame:
            xalign 1.0
            textbutton "Dresscode":
                action Jump("Policies_Options_dresscode_check")
                hovered Show("school_dresscode")
                unhovered Hide("school_dresscode")
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            xalign 1.0
            textbutton "Teacher Leeway":
                action Jump("Policies_Options_teacher_leeway_check")
                hovered Show("teacher_leeway")
                unhovered Hide("teacher_leeway")
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            xalign 1.0
            textbutton "Depiction of the human body":
                action Show("depiction_of_the_human_body_check")
                hovered Show("depiction_of_the_human_body")
                unhovered Hide("depiction_of_the_human_body")
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            xalign 1.0
            textbutton "Entrance requirement strenght":
                action Show("entrance_requirement_strenght_check")
                hovered Show("entrance_requirement_strenght")
                unhovered Hide("entrance_requirement_strenght")
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            xalign 1.0
            textbutton "Entrance requirement focus":
                action Show("entrance_requirement_focus")
                hovered Show("entrance_requirement_focus")
                unhovered Hide("entrance_requirement_focus")
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            xalign 1.0
            textbutton "Learning materials":
                action Show("learning_materials_check")
                hovered Show("learning_materials")
                unhovered Hide("learning_materials")
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            xalign 1.0
            textbutton "Staff salary":
                action Show("staff_salary_check")
                hovered Show("staff_salary")
                unhovered Hide("staff_salary")
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            xalign 1.0
            textbutton "Class size":
                action Show("class_size_checl")
                hovered Show("class_size")
                unhovered Hide("class_size")
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"
        frame:
            xalign 1.0
            textbutton "Back":
                action [Hide("school_dresscode"), Hide("teacher_leeway"), Hide("depiction_of_the_human_body"), 
                Hide("entrance_requirement_strenght"), Hide("entrance_requirement_focus"),
                Hide("learning_materials"), Hide("staff_salary"), Hide("class_size"),Jump("Your_Office")]
                text_style "custom_textbutton_text0"
                style "custom_textbutton0"         