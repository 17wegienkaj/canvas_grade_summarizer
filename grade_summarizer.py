from canvasapi import Canvas
import config

def setTerms(courseList):
    course = courseList[0];
    for course in courseList:
        for word in course.name.split():
            if (word == "F") or (word == "FA") or (word == "W") or (word == "WN"):
                course.term = lambda : None
                if (word == "F") or (word == "FA"):
                    termSeason = 'F'
                elif (word == "W") or (word == "WN"):
                    termSeason = 'W'
                termYear = int(course.name.split()[course.name.split().index(word) + 1]) % 100
                setattr(course, 'term', termSeason + str(termYear))

def main():
    canvas = Canvas(config.API_URL, config.API_KEY)
    courses = canvas.get_courses()

    setTerms(courses)


if __name__ == '__main__':
    main()