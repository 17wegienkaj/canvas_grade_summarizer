from canvasapi import Canvas
import config

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

def main():
    canvas = Canvas(config.API_URL, config.API_KEY)
    courses = canvas.get_courses()

    setTerms(courses);
    classesInSem = getCoursesForTerm(courses, config.CurrentTerm)


if __name__ == '__main__':
    main()