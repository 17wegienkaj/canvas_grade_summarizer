from canvasapi import Canvas
import config
import os

def setTerms(courseList):
    for course in courseList:
        for word in course.name.split():
            word = word.upper()
            if (word == "F") or (word == "FA") or (word == "W") or (word == "WN") or (hasNumbers(word) and word.isupper()):
                course.term = lambda : None
                if (word == "F") or (word == "FA"):
                    termSeason = 'F'
                    termYear = int(course.name.split()[course.name.split().index(word) + 1]) % 100
                elif (word == "W") or (word == "WN"):
                    termSeason = 'W'
                    termYear = int(course.name.split()[course.name.split().index(word) + 1]) % 100
                elif(hasNumbers(word) and word.isupper()):
                    if word[0] == 'F':
                        termSeason = 'F'
                    elif word[0] == 'W':
                        termSeason = "W"

                setattr(course, 'term', termSeason + str(termYear))

def hasNumbers(str):
    return any(char.isdigit() for char in str)

def getCoursesForTerm(courses, sem):
    sem = sem.upper()
    coursesInSem = []

    for course in courses:
        if course.term == sem:
            coursesInSem.append(course)
    return coursesInSem

def gradesForCourse(course):
    assignments = course.get_assignments()
    submission = assignments[0].get_submission(os.environ['CANVAS_ID'])
    print(submission.grade)
    # for assignment in assignments:
    # print(course.__dict__)

def main():
    canvas = Canvas(os.environ['API_URL'], os.environ['API_KEY'])
    courses = canvas.get_courses()

    setTerms(courses);
    coursesInSem = getCoursesForTerm(courses, "W20")
    gradesForCourse(coursesInSem[0])
    # for course in coursesInSem:



if __name__ == '__main__':
    main()