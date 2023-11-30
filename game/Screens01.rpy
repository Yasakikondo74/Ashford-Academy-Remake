screen classroom:
    frame at fading: 
        xalign 0.5
        yalign 0.05
        add Frame("building/building_classrooms.jpg", 8, 8, 8, 8, tile=False):
            xsize 0.5
            ysize 0.75
    frame at fading:
        xalign 0.5
        yalign 0.9
        background Solid("#00000073")
        textbutton "Quality, equipment and state of your classrooms.\nGood classrooms will help your students academically.\nThey are also more enjoyable to teach in {b}Afternoon{b}":
            text_color "#FFFFFF"
    frame at move_from_right_cost:
        xalign 0.905
        yalign 0.15
        textbutton "Cost: $$$":
            text_color "#FFFFFF"  

screen dormitory:
    frame at fading:
        xalign 0.5
        yalign 0.05
        add Frame("building/building_dormitory.jpg", 8, 8, 8, 8, tile=False):
            xsize 0.5
            ysize 0.75
    frame at fading:
        xalign 0.5
        yalign 0.9
        background Solid("#00000073")
        textbutton "A dormitory is a building primarily providing sleeping\nand residential quarters for large numbers of students\nto board school more conviently {b}Evening{b}":
            text_color "#FFFFFF"
    frame at move_from_right_cost:
        xalign 0.905
        yalign 0.15
        textbutton "Cost: $$$":
            text_color "#FFFFFF"  

screen bath_area:
    frame at fading:
        xalign 0.5
        yalign 0.05
        add Frame("building/building_bath.jpg", 8, 8, 8, 8, tile=False):
            xsize 0.5
            ysize 0.75
    frame at fading:
        xalign 0.5
        yalign 0.9
        background Solid("#00000073")
        textbutton "Open hot water baths for students to relax also known as Onsen\nBuying this will give your students a boost of\nmorale every {b}Evening{b}":
            text_color "#FFFFFF"
    frame at move_from_right_cost:
        xalign 0.905
        yalign 0.15
        textbutton "Cost: $$$":
            text_color "#FFFFFF"  

screen cafeteria:
    frame at fading:
        xalign 0.5
        yalign 0.05
        add Frame("building/building_cafeteria.jpg", 8, 8, 8, 8, tile=False):
            xsize 0.5
            ysize 0.75
    frame at fading:
        xalign 0.5
        yalign 0.9
        background Solid("#00000073")
        textbutton "This is where you students be buying snacks and socialize\nThis building could help you generate some income {b}Afternoon{b}":
            text_color "#FFFFFF"
    frame at move_from_right_cost:
        xalign 0.905
        yalign 0.15
        textbutton "Cost: $$$":
            text_color "#FFFFFF" 

screen gym:
    frame at fading:
        xalign 0.5
        yalign 0.05
        add Frame("building/building_gym.jpg", 8, 8, 8, 8, tile=False):
            xsize 0.5
            ysize 0.75
    frame at fading:
        xalign 0.5
        yalign 0.9
        background Solid("#00000073")
        textbutton "A building where students can practice indoor athletic trainning\nThis gym could boost athletic stats {b}Morning{b}":
            text_color "#FFFFFF"
    frame at move_from_right_cost:
        xalign 0.905
        yalign 0.15
        textbutton "Cost: $$$":
            text_color "#FFFFFF"  

screen school_grounds:
    frame at fading:
        xalign 0.5
        yalign 0.05
        add Frame("building/building_grounds.jpg", 8, 8, 8, 8, tile=False):
            xsize 0.5
            ysize 0.75
    frame at fading:
        xalign 0.5
        yalign 0.9
        background Solid("#00000073")
        textbutton "This building represent the quality and upkeep\nof the school. Upgrading thiswill makes the whole school more\nbeautiful with students and staff happier {b}Evening{b}":
            text_color "#FFFFFF"
    frame at move_from_right_cost:
        xalign 0.905
        yalign 0.15
        textbutton "Cost: $$$":
            text_color "#FFFFFF"

screen library:
    frame at fading:
        xalign 0.5
        yalign 0.05
        add Frame("building/building_library.jpg", 8, 8, 8, 8, tile=False):
            xsize 0.5
            ysize 0.75
    frame at fading:
        xalign 0.5
        yalign 0.9
        background Solid("#00000073")
        textbutton "A library to store school's collection of books\nand internet access. Giving students access to knowledge help\n boost their academic skills {b}Morning{b}":
            text_color "#FFFFFF"
    frame at move_from_right_cost:
        xalign 0.905
        yalign 0.15
        textbutton "Cost: $$$":
            text_color "#FFFFFF"  

screen pool:
    frame at fading:
        xalign 0.5
        yalign 0.05
        add Frame("building/building_pool.jpg", 8, 8, 8, 8, tile=False):
            xsize 0.5
            ysize 0.75
    frame at fading:
        xalign 0.5
        yalign 0.9
        background Solid("#00000073")
        textbutton "This is a swimming pool which boost athletic skills\nstudents can spend their time enjoy swimming in the pool {b}Afternoon{b}":
            text_color "#FFFFFF"
    frame at move_from_right_cost:
        xalign 0.905
        yalign 0.15
        textbutton "Cost: $$$":
            text_color "#FFFFFF"  

screen sports_field:
    frame at fading:
        xalign 0.5
        yalign 0.05
        add Frame("building/building_sports_field.jpg", 8, 8, 8, 8, tile=False):
            xsize 0.5
            ysize 0.75
    frame at fading:
        xalign 0.5
        yalign 0.9
        background Solid("#00000073")
        textbutton "A large and open field play ground for students to\npractice and exercise to their heart contents {b}Afternoon{b}":
            text_color "#FFFFFF"
    frame at move_from_right_cost:
        xalign 0.905
        yalign 0.15
        textbutton "Cost: $$$":
            text_color "#FFFFFF"  

screen surveillance:
    frame at fading:
        xalign 0.5
        yalign 0.05
        add Frame("building/building_surveillance.jpg", 8, 8, 8, 8, tile=False):
            xsize 0.5
            ysize 0.75
    frame at fading:
        xalign 0.5
        yalign 0.9
        background Solid("#00000073")
        textbutton "Upgrading surveillance will record anysuspicious\nactivity around the school":
            text_color "#FFFFFF"
    frame at move_from_right_cost:
        xalign 0.905
        yalign 0.15
        textbutton "Cost: $$$":
            text_color "#FFFFFF"  

screen security:
    frame at fading:
        xalign 0.5
        yalign 0.05
        add Frame("building/building_security.jpg", 8, 8, 8, 8, tile=False):
            xsize 0.5
            ysize 0.75
    frame at fading:
        xalign 0.5
        yalign 0.9
        background Solid("#00000073")
        textbutton "This upgrades is keep everything under control\nImprove student behavior and prevent any circumstances\nthat ruin the school reputation":
            text_color "#FFFFFF"
    frame at move_from_right_cost:
        xalign 0.905
        yalign 0.15
        textbutton "Cost: $$$":
            text_color "#FFFFFF"  

screen school_dresscode:
    frame at move_from_middle_to_right:
        xsize 0.25
        yalign 0.025
        background "#00000050"
        vbox:
            frame:
                text "Current: [s.dresscode]"
            if s.dresscode == "Conservative":
                textbutton "The skirt must be longer than mid thigh. Bras and panties must be worn conervatively. All clothing must be opaque":
                    action NullAction()
                    text_color "#FFFFFF"
            elif s.dresscode == "Normal":
                textbutton "The skirt only covers the panties completely, while not being longer than mid-thigh.Normal bras and panties. All clothing must be opaque":
                    action NullAction()
                    text_color "#FFFFFF"
            elif s.dresscode == "None":
                textbutton "Students may wear any clothing whatsoever. Giving student more freedom to express themselves.":
                    action NullAction()
                    text_color "#FFFFFF"
            elif s.dresscode == "Sexy":
                textbutton "Top and bottom must shows a bit of panties and bras or just plain underwears. Swimsuits must cover very little skins":
                    action NullAction()
                    text_color "#FFFFFF"
            elif s.dresscode == "Nude":
                textbutton "No clothing allowed in school. No covering the breasts or pelvic area. Covering it up is prohibited":
                    action NullAction()
                    text_color "#FFFFFF"
    frame at fading:
        xalign 0.45
        yalign 0.05
        xsize 0.5
        ysize 0.75
        if s.dresscode == "Conservative":
            add Frame("policies/dresscode_cons.jpg", 8, 8, 8, 8, tile=False)
        elif s.dresscode == "Normal":
            add Frame("policies/dresscode_normal.jpg", 8, 8, 8, 8, tile=False)
        elif s.dresscode == "None":
            add Frame("policies/dresscode_none.jpg", 8, 8, 8, 8, tile=False)
        elif s.dresscode == "Sexy":
            add Frame("policies/dresscode_sexy.jpg", 8, 8, 8, 8, tile=False)
        elif s.dresscode == "Nude":
            add Frame("policies/dresscode_nude.jpg", 8, 8, 8, 8, tile=False)
    frame at move_from_middle_to_right:
        xsize 0.25
        yalign 0.725
        background "#00000050"
        text "This change how your student should dress while in school or during events"

screen teacher_leeway:
    frame at move_from_middle_to_right:
        xsize 0.25
        yalign 0.025
        background "#00000050"
        vbox:
            frame:
                text "Current: [s.teacher_leeway]"
            if s.teacher_leeway == "None":
                textbutton "No kind of aggression towards students is allowed. A bad if the students aren't obedient"
            elif s.teacher_leeway == "Verbal Abuse":
                textbutton "Verbal physical is allowed but no more than physical pushnishment"
            elif s.teacher_leeway == "Physical Abuse":
                textbutton "Teachers are allowed to use moderate violence. Students are warned that they might get expelled if they flaunt the rules"
            elif s.teacher_leeway == "Spanking":
                textbutton "Teachers are allowed to give spankings to misbehaving students. On average, parents are in favor of this."
            elif s.teacher_leeway == "BDSM":
                textbutton "Teachers are allowed to punish with any means be it by sexually harrasing them or doing some bdsm punishment"
    frame at move_from_middle_to_right:
        xsize 0.25
        yalign 0.725
        background "#00000050"
        text "This show you amount of punishment are allowed to punish the students"
    frame at fading:
        xalign 0.45
        yalign 0.05
        xsize 0.5
        ysize 0.75
        if s.teacher_leeway == "None":
            add Frame("policies/no.png", 8, 8, 8, 8, tile=False)
        elif s.teacher_leeway == "Verbal Abuse":
            add Frame("policies/teacher_leeway_verbal.jpg", 8, 8, 8, 8, tile=False)
        elif s.teacher_leeway == "Physical Abuse":
            add Frame("policies/teacher_leeway_physical.jpg", 8, 8, 8, 8, tile=False)
        elif s.teacher_leeway == "Spanking":
            add Frame("policies/teacher_leeway_spanking.jpg", 8, 8, 8, 8, tile=False)
        elif s.teacher_leeway == "BDSM":
            add Frame("policies/teacher_leeway_bdsm.jpg", 8, 8, 8, 8, tile=False)

screen depiction_of_the_human_body:
    frame at move_from_middle_to_right:
        xsize 0.25
        yalign 0.025
        background "#00000050"
        vbox:
            frame:
                text "Current: [s.depiction_of_the_human_body]"
            if s.depiction_of_the_human_body == "None":
                text "Non sexualized version of the human body"
            elif s.depiction_of_the_human_body == "Correct":
                text "Usage of anatomically correct human models"
            elif s.depiction_of_the_human_body == "Hyper Sexualized":
                text "Using models based on porn stars, showing them in an aroused state"
            elif s.depiction_of_the_human_body == "Live Models":
                text "Pictures in books are obviously not enough. So there are 'voluteers' from the class to shwo their fellow students what the human body look like"
    frame at fading:
        xalign 0.45
        yalign 0.05
        xsize 0.5
        ysize 0.75
        if s.depiction_of_the_human_body == "None":
            add Frame("policies/human_anatomy_depiction_nonsexual.jpg", 8, 8, 8, 8, tile=False)
        elif s.depiction_of_the_human_body == "Correct":
            add Frame("policies/human_anatomy_depiction_correct.jpg", 8, 8, 8, 8, tile=False)
        elif s.depiction_of_the_human_body == "Hyper Sexualized":
            add Frame("policies/human_anatomy_depiction_hypersexualized.jpg", 8, 8, 8, 8, tile=False)
        elif s.depiction_of_the_human_body == "Live Models":
            add Frame("policies/human_anatomy_depiction_live_student_models.jpg", 8, 8, 8, 8, tile=False)
    frame at move_from_middle_to_right:
        xsize 0.25
        yalign 0.725
        background "#00000050"
        text "How anatomically coorect should nude pictures be\nin teaching materials"

screen entrance_requirement_strenght:
    frame at move_from_middle_to_right:
        xsize 0.25
        yalign 0.025
        background "#00000050"
        vbox:
            frame:
                text "Current: [s.entrance_requirement_strenght]"
            if s.entrance_requirement_strenght == "None":
                text ""
            elif s.entrance_requirement_strenght == "Age":
                text ""
            elif s.entrance_requirement_strenght == "Standard":
                text ""
            elif s.entrance_requirement_strenght == "Advanced":
                text ""
            elif s.entrance_requirement_strenght == "Perfect":
                text ""
    frame at fading:
        xalign 0.45
        yalign 0.05
        xsize 0.5
        ysize 0.75
        if s.entrance_requirement_strenght == "None":
            add Frame("policies/entrance_req_strength_none.jpg", 8, 8, 8, 8, tile=False)
        elif s.entrance_requirement_strenght == "Age":
            add Frame("policies/entrance_req_strength_age.jpg", 8, 8, 8, 8, tile=False)
        elif s.entrance_requirement_strenght == "Standard":
            add Frame("policies/entrance_req_strength_standard.jpg", 8, 8, 8, 8, tile=False)
        elif s.entrance_requirement_strenght == "Advanced":
            add Frame("policies/entrance_req_strength_advanced.jpg", 8, 8, 8, 8, tile=False)
        elif s.entrance_requirement_strenght == "Perfect":
            add Frame("policies/entrance_req_strength_perfect.jpg", 8, 8, 8, 8, tile=False)
    frame at move_from_middle_to_right:
        xsize 0.25
        yalign 0.725
        background "#00000050"
        text "What kind of student should we allowed or accept in school?"

screen entrance_requirement_focus:
    frame at move_from_middle_to_right:
        xsize 0.25
        yalign 0.025
        background "#00000050"
        vbox:
            frame:
                text "Current: [s.entrance_requirement_focus]"
            if s.entrance_requirement_focus == "":
                text ""
            elif s.entrance_requirement_focus == "":
                text ""
            elif s.entrance_requirement_focus == "":
                text ""
            elif s.entrance_requirement_focus == "":
                text ""
            elif s.entrance_requirement_focus == "":
                text ""
    frame at fading:
        xalign 0.45
        yalign 0.05
        xsize 0.5
        ysize 0.75
        if s.entrance_requirement_focus == "Attitude":
            add Frame("policies/entrance_req_focus_attitude.jpg", 8, 8, 8, 8, tile=False)
        elif s.entrance_requirement_focus == "":
            add Frame("policies/entrance_req_focus_attitude.jpg", 8, 8, 8, 8, tile=False)
        elif s.entrance_requirement_focus == "":
            add Frame("policies/entrance_req_focus_attitude.jpg", 8, 8, 8, 8, tile=False)
        elif s.entrance_requirement_focus == "":
            add Frame("policies/entrance_req_focus_attitude.jpg", 8, 8, 8, 8, tile=False)
        elif s.entrance_requirement_focus == "":
            add Frame("policies/entrance_req_focus_attitude.jpg", 8, 8, 8, 8, tile=False)
    frame at move_from_middle_to_right:
        xsize 0.25
        yalign 0.725
        background "#00000050"
        text "Which quality should we test our prospective students for?"

screen learning_materials:
    frame at move_from_middle_to_right:
        xsize 0.25
        yalign 0.025
        background "#00000050"
        vbox:
            frame:
                text "Current: [s.learning_materials]"
            if s.learning_materials == "":
                text ""
            elif s.learning_materials == "":
                text ""
            elif s.learning_materials == "":
                text ""
            elif s.learning_materials == "":
                text ""
            elif s.learning_materials == "":
                text ""
    frame at fading:
        xalign 0.45
        yalign 0.05
        xsize 0.5
        ysize 0.75
        if s.learning_materials == "Old & Cheap":
            add Frame("policies/teaching_materials_old.jpg", 8, 8, 8, 8, tile=False)
        elif s.learning_materials == "":
            add Frame("policies/teaching_materials_old.jpg", 8, 8, 8, 8, tile=False)
        elif s.learning_materials == "":
            add Frame("policies/teaching_materials_old.jpg", 8, 8, 8, 8, tile=False)
        elif s.learning_materials == "":
            add Frame("policies/teaching_materials_old.jpg", 8, 8, 8, 8, tile=False)
        elif s.learning_materials == "":
            add Frame("policies/teaching_materials_old.jpg", 8, 8, 8, 8, tile=False)
    frame at move_from_middle_to_right:
        xsize 0.25
        yalign 0.725
        background "#00000050"
        text "Quality of learning materials available for teaching"

screen staff_salary:
    frame at move_from_middle_to_right:
        xsize 0.25
        yalign 0.025
        background "#00000050"
        vbox:
            frame:
                text "Current: [s.staff_salary]"
            if s.staff_salary == "":
                text ""
            elif s.staff_salary == "":
                text ""
            elif s.staff_salary == "":
                text ""
    frame at fading:
        xalign 0.45
        yalign 0.05
        xsize 0.5
        ysize 0.75
        if s.staff_salary == "Average":
            add Frame("policies/staff_salary_low.jpg", 8, 8, 8, 8, tile=False)
        elif s.staff_salary == "":
            add Frame("policies/staff_salary_low.jpg", 8, 8, 8, 8, tile=False)
        elif s.staff_salary == "":
            add Frame("policies/staff_salary_low.jpg", 8, 8, 8, 8, tile=False)
        elif s.staff_salary == "":
            add Frame("policies/staff_salary_low.jpg", 8, 8, 8, 8, tile=False)
        elif s.staff_salary == "":
            add Frame("policies/staff_salary_low.jpg", 8, 8, 8, 8, tile=False)
    frame at move_from_middle_to_right:
        xsize 0.25
        yalign 0.725
        background "#00000050"
        text "Adjusting the salary of your teachers and co-workers"

screen class_size:
    frame at move_from_middle_to_right:
        xsize 0.25
        yalign 0.025
        background "#00000050"
        vbox:
            frame:
                text "Current: [s.class_size]"
            if s.class_size == "":
                text ""
            elif s.class_size == "":
                text ""
            elif s.class_size == "":
                text ""
            elif s.class_size == "":
                text ""
            elif s.class_size == "":
                text ""
    frame at fading:
        xalign 0.45
        yalign 0.05
        xsize 0.5
        ysize 0.75
        if s.class_size == "Big":
            add Frame("policies/class_size_big.jpg", 8, 8, 8, 8, tile=False)
        elif s.class_size == "":
            add Frame("policies/class_size_big.jpg", 8, 8, 8, 8, tile=False)
        elif s.class_size == "":
            add Frame("policies/class_size_big.jpg", 8, 8, 8, 8, tile=False)
        elif s.class_size == "":
            add Frame("policies/class_size_big.jpg", 8, 8, 8, 8, tile=False)
        elif s.class_size == "":
            add Frame("policies/class_size_big.jpg", 8, 8, 8, 8, tile=False)
    frame at move_from_middle_to_right:
        xsize 0.25
        yalign 0.725
        background "#00000050"
        text "How many students should be in each class at most?"

screen placeholder_text:
    default displayText = ""
    vbox at move_from_left_text:
        yalign 0.025
        frame:
            text displayText

screen placeholder_text0:
    default displayText0 = ""
    hbox at move_from_left_text0:
        yalign 0.12
        textbutton displayText0:
            text_color "#000000"

screen placeholder_text1:
    default displayText1 = ""
    hbox at move_from_left_text0:
        yalign 0.19
        textbutton displayText1:
            text_color "#000000"

screen placeholder_text2:
    default displayText2 = ""
    hbox at move_from_left_text0:
        yalign 0.2625
        textbutton displayText2:
            text_color "#000000"

screen placeholder_text3:
    default displayText3 = ""
    hbox at move_from_left_text0:
        yalign 0.33
        textbutton displayText3:
            text_color "#000000"

screen placeholder_text4:
    default displayText4 = ""
    hbox at move_from_left_text0:
        yalign 0.405
        textbutton displayText4:
            text_color "#000000"

screen placeholder_text5:
    default displayText5 = ""
    hbox at move_from_left_text0:
        yalign 0.475
        textbutton displayText5:
            text_color "#000000"

screen placeholder_text6:
    default displayText6 = ""
    hbox at move_from_left_text0:
        yalign 0.55
        textbutton displayText6:
            text_color "#000000"

screen placeholder_text7:
    default displayText7 = ""
    hbox at move_from_left_text0:
        yalign 0.62
        textbutton displayText7:
            text_color "#000000"

screen placeholder_text8:
    default displayText8 = ""
    hbox at move_from_left_text0:
        yalign 0.69
        textbutton displayText8:
            text_color "#000000"

screen placeholder_text9:
    default displayText9 = ""
    hbox at move_from_left_text0:
        yalign 0.76
        textbutton displayText9:
            text_color "#000000"

screen placeholder_text10:
    default displayText10 = ""
    hbox at move_from_left_text0:
        yalign 0.83
        textbutton displayText10:
            text_color "#000000"

transform move_from_left_text:
    on show:
        alpha 0.0 xalign -0.1
        linear 0.1 xalign 0.025 alpha 1.0
    on hide:
        xalign 0.025 alpha 1.0
        linear 0.1 xalign -0.1 alpha 0.0

transform move_from_left_text0:
    on show:
        alpha 0.0 xalign 0.16
        linear 0.25 xalign 0.185 alpha 1.0
    on hide:
        xalign 0.185 alpha 1.0
        linear 0.25 xalign 0.16 alpha 0.0

transform move_from_top0:
    on show:
        yalign -0.5 alpha 0.0
        linear 0.5 yalign 0.025 alpha 1.0
    on hide:
        yalign 0.025 alpha 1.0
        linear 0.5 yalign -0.5 alpha 0.0

transform move_from_top1:
    on show:
        yalign -0.5 alpha 0.0
        linear 0.5 yalign 0.25 alpha 1.0
    on hide:
        yalign 0.25 alpha 1.0
        linear 0.5 yalign -0.5 alpha 0.0

transform move_from_right:
    on show:
        xalign 1.5 alpha 0.0
        linear 0.5 xalign 0.975 alpha 1.0
    on hide:
        xalign 0.975 alpha 1.0
        linear 0.5 xalign 1.5 alpha 0.0

transform fading:
    on show:
        alpha 0.0
        linear 0.25 alpha 1.0
    on hide:
        linear 0.25 alpha 0.0

transform move_from_left:
    on show:
        xalign -0.5 alpha 0.0
        linear 0.5 xalign 0.025 alpha 1.0
    on hide:
        xalign 0.025 alpha 1.0
        linear 0.5 xalign -0.5 alpha 0.0

transform move_from_right_cost:
    on show:
        xalign 0.875 alpha 0.0
        linear 0.25 xalign 0.895 alpha 1.0
    on hide:
        xalign 0.895 alpha 1.0
        linear 0.25 xalign 0.875 alpha 0.0

transform move_from_middle_to_right:
    on show:
        xalign 0.5 alpha 0.0
        linear 0.5 xalign 0.985 alpha 1.0
    on hide:
        xalign 0.985 alpha 1.0
        linear 0.25 alpha 0.05 #xalign 0.5 

init python:
    # Functions custom_textbutton #
    style.custom_textbutton = Style(style.button)
    style.custom_textbutton.background = Frame("choice_idle_background.png", 8, 8, 8, 8, tile=False)
    style.custom_textbutton.hover_background = Frame("choice_hover_background.png", 8, 8, 8, 8, tile=False)

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