define unknown = Character("???")
define C = Character("Creator")
image ashford = Transform("images/ashford.jpg", size = (1920, 1080))
image building_classrooms = Transform("images/building_classrooms.jpg", size = (1920, 1080))
image building_dormitory = Transform("images/building_dormitory.jpg", size = (1920, 1080))
image building_bath_area = Transform("images/building_bath.jpg", size = (1920, 1080))
image building_cafeteria = Transform("images/building_cafeteria.jpg", size = (1920, 1080))
image building_security = Transform("images/building_security.jpg", size = (1920, 1080))
image building_gym = Transform("images/building_gym.jpg", size = (1920, 1080))
image building_school_grounds = Transform("images/building_grounds.jpg", size = (1920, 1080))
image building_library = Transform("images/building_library.jpg", size = (1920, 1080))
image building_pool = Transform("images/building_pool.jpg", size = (1920, 1080))
image building_sport_field = Transform("images/building_sports_field.jpg", size = (1920, 1080))
image building_surveillance = Transform("images/building_surveillance.jpg", size = (1920, 1080))
image dp_frame = "gui/dp_frame.png"

init python:
    class MC:
        def __init__(self):
            self.morning = "office"
            self.afternoon = "classroom"
            self.evening = "school grounds"
            self.name = "Principle"
            self.charisma = 0
            self.intelligence = 0
            self.dns = 3 #1.Submissive 2.Compliant 3.Passive 4.Authoritative 5.Dominant 6.Superior
            self.staff_support = 20.0
            self.staff = 6
        def staff_support_cal(self):
            self.staff_support += 1

    mc = MC()

    class Students:
        def __init__(self):
            self.amount_students = 100
            self.behavior = 30.0
            self.morale = 10.0
            self.athletics = 5.0
            self.academics = 15.0
            self.stress = 1.5
            self.inhibition = 100.0
            self.deviance = 0.0
            self.inhibition_lvl = 0
            self.lust = 0

        def capped(self):
            if self.behavior >= 100.0:
                self.behavior = 100.0
            if self.morale >= 100.0:
                self.behavior = 100.0
            if self.athletics >= 100.0:
                self.athletics = 100.0
            if self.academics >= 100.0:
                self.academics = 100.0
            if self.stress >= 100.0:
                self.stress = 100.0
            if self.deviance >= 100.0:
                self.deviance = 100.0

            # for inhibition cap #
            if self.inhibition <= 100 and self.inhibition_lvl == 5:
                self.inhibition = 0
            elif self.inhibition <= 20 and self.inhibition_lvl == 4:
                self.inhibition = 20
            elif self.inhibition <= 40 and self.inhibition_lvl == 3:
                self.inhibition = 40
            elif self.inhibition <= 60 and self.inhibition_lvl == 2:
                self.inhibition = 60
            elif self.inhibition <= 80 and self.inhibition_lvl == 1:
                self.inhibition = 80
            elif self.inhibition <= 100 and self.inhibition_lvl == 0:
                self.inhibition = 100

    st = Students()

    class School:
        def __init__(self):
            # SCHOOL SETTINGS #
            self.name = "Ashford"
            self.dresscode = "conservative"
            self.teacher_leeway = "verbal abuse"
            self.entrance_requirement_strength = "standard"
            self.entrance_requirement_focus = "obedient"
            self.learning_materials = "old_n_cheap"
            self.teacher_salery = "average"
            self.class_size = "big"

            # SCHOOL UPGRADES #
            self.surveillance_option = False
            self.surveillance = 1
            self.classroom = 1
            self.cafeteria = 0
            self.dorm = 0
            self.gym = 0
            self.library = 0
            self.pool = 0
            self.school_grounds = 1
            self.security = 1
            self.sport_field = 0
            self.bath = 0
            self.club = False
            self.sex_education = False
            self.upgrade_building_image = "classroom"

            # SCHOOL STATS #
            self.hygiene = "clean"
            self.reputation = 12.5
            self.money = 1000.00

            # DATETIME #
            self.student_enter = False
            self.count_day = 1
            self.day = 1
            self.weekday_name = "Monday"
            self.month = 1
            self.month_name = "January"
            self.year = 1
            self.day_name = "1st"
            self.year_name = "{:04d}".format(self.year)

        def next_day(self):
            self.day += 1
            self.count_day += 1 
            if self.month >= 13:
                self.year += 1
                self.month = 1
            if self.year % 2:
                if self.month == 2:
                    if self.day >= 28:
                        self.month += 1
                        self.day = 1
            else:
                if self.month == 2:
                    if self.day >= 29:
                        self.month += 1
                        self.day = 1
            if self.month in [1, 3, 5, 7, 8, 10, 12]:
                if self.day >= 31:
                    self.month += 1
                    self.day = 1
            elif self.month in [2, 4, 6, 9, 11]:
                if self.day >= 30:
                    self.month += 1
                    self.day = 1
            self.year_name = "{:04d}".format(self.year)

            if self.month == 1:
                self.month_name = "January"
            elif self.month == 2:
                self.month_name = "February"
            elif self.month == 3:
                self.month_name = "March"
            elif self.month == 4:
                self.month_name = "April"
            elif self.month == 5:
                self.month_name = "May"
            elif self.month == 6:
                self.month_name = "June"
            elif self.month == 7:
                self.month_name = "July"
            elif self.month == 8:
                self.month_name = "August"
            elif self.month == 9:
                self.month_name = "September"
            elif self.month == 10:
                self.month_name = "October"
            elif self.month == 11:
                self.month_name = "November"
            elif self.month == 12:
                self.month_name = "December"

            if self.day in [1, 11, 21, 31]:    
                self.day_name = str(self.day) + "st"
            elif self.day in [2, 12, 22]:
                self.day_name = str(self.day) + "nd"
            elif self.day in [3, 13, 23]:
                self.day_name = str(self.day) + "rd"
            else:
                self.day_name = str(self.day) + "th"

            q = self.day
            m = self.month
            k = self.year % 100
            j = self.year // 100
            f = q + ((13*(m+1)) // 5) + k + (k // 4) + (j // 4) - 2*j
            weekday = f % 7
            weekdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            self.weekday_name = weekdays[weekday]

            if self.count_day >= 8:
                self.count_day = 1
                self.student_enter = True
            
        def Student_population(self): # calculate student population
            st.amount_students += renpy.random.randint(25, 50)

            reputation_deductions = [(1000.0, 10), (100.0, 15), (10.0, 20), (0, 25)]
            for rep, deduction in reputation_deductions:
                if self.reputation >= rep:
                    st.amount_students -= renpy.random.randint(0, deduction)
                    break

            entrance_requirements = {
                "none": 0,
                "age": 10,
                "standard": 20,
                "advanced": 30,
                "perfect record": 40
            }
            st.amount_students -= renpy.random.randint(0, entrance_requirements.get(self.entrance_requirement_strength, 0))
    
    s = School()

    # class School_club:
    #     def __init__(self):
    #         self.club_name = ""
    #         self.club_member = 0
    #         self.

    # sc = School_club()