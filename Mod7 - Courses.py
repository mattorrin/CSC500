#get_course_info takes input and searches for related info for that course
def get_course_info():

    course_nums = {'CSC101': {"room": '3004', "Instructor": "Haynes",
                          "meet time": "8:00 a.m."},
               'CSC102': {"room": '4501', "Instructor": "Alvarado",
                          "meet time": '9:00 a.m.'},
               'CSC103': {"room": '6755', "Instructor": "Rich",
                          "meet time": '10:00 a.m.'},
               'NET110': {"room": '1244', "Instructor": "Burke",
                          "meet time": '11:00 a.m.'},
               'COM241': {"room": '1411', "Instructor": "Lee",
                          "meet time": '1:00 p.m.'}}

#Determines if input is valid
    valid_course = False
    while valid_course == False:               
        course_number = input('State course you are interested in: ').upper()   #handles and case by making it uppercase
        
#If entry is in dictionary, then it will output each related value then change valid_course to True to end the loop
        if course_number in course_nums:
            info = course_nums[course_number]
            print('\n{} is in room {}, with Instructor {}, at {}'.format(course_number, info["room"],
                                                                 info["Instructor"],
                                                                 info["meet time"]))
            valid_course = True
        
        else:
            print('Not a valid entry, please try again!\n')

#Function call
get_course_info()
