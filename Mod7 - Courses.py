# CSC500-1
# Program: Courses
# Author: Matt Orrin
# Description:
#       Maintain a dictionary of Course codes as keys, and room, instructor and meet times
#       as values for each Course. User can enter Course number and get class info


def get_course_info():

    course_rooms = {'CSC101': '3004',
                    'CSC102': '4501',
                    'CSC103': '6755',
                    'NET110': '1244',
                    'COM241': '1411'}
                    
    course_instructor = {'CSC101': "Haynes",
                         'CSC102': "Alvarado",
                         'CSC103': "Rich",
                         'NET110': "Burke",
                         'COM241': "Lee"}
    
    course_times = {'CSC101': "8:00 a.m.",
                    'CSC102': '9:00 a.m.',
                    'CSC103': '10:00 a.m.',
                    'NET110': '11:00 a.m.',
                    'COM241': '1:00 p.m.'}
    
#Determines if input is valid
    valid_course = False
    while valid_course == False:
        
        #handles any case by making it uppercase
        course_number = input('State course you are interested in: ').upper()   
        
        #If entry is in dictionary, then it will output each related value then change valid_course to True ending loop
        if course_number in course_rooms:
            room = course_rooms[course_number]
            instructor = course_instructor[course_number]
            times = course_times[course_number]
            print('\n{} is in room {}, with Instructor {}, at {}'.format(course_number, room, instructor, times))
            valid_course = True
        
        else:
            print('Not a valid entry, please try again!\n')

#Function call
get_course_info()



###get_course_info takes input and searches for related info for that course
##def get_course_info():
##
##    course_nums = {'CSC101': {"room": '3004', "Instructor": "Haynes",
##                          "meet time": "8:00 a.m."},
##               'CSC102': {"room": '4501', "Instructor": "Alvarado",
##                          "meet time": '9:00 a.m.'},
##               'CSC103': {"room": '6755', "Instructor": "Rich",
##                          "meet time": '10:00 a.m.'},
##               'NET110': {"room": '1244', "Instructor": "Burke",
##                          "meet time": '11:00 a.m.'},
##               'COM241': {"room": '1411', "Instructor": "Lee",
##                          "meet time": '1:00 p.m.'}}
##
###Determines if input is valid
##    valid_course = False
##    while valid_course == False:
##        
##        #handles any case by making it uppercase
##        course_number = input('State course you are interested in: ').upper()   
##        
##        #If entry is in dictionary, then it will output each related value then change valid_course to True ending loop
##        if course_number in course_nums:
##            info = course_nums[course_number]
##            print('\n{} is in room {}, with Instructor {}, at {}'.format(course_number, info["room"],
##                                                                 info["Instructor"],
##                                                                 info["meet time"]))
##            valid_course = True
##        
##        else:
##            print('Not a valid entry, please try again!\n')
##
###Function call
##get_course_info()
##
##
