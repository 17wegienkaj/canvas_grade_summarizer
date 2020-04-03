from canvasapi import Canvas
import grade_summarizer
import unittest
import config
import warnings

def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            test_func(self, *args, **kwargs)
    return do_test

class TestFunctions(unittest.TestCase):
    @ignore_warnings
    def test_hasNumbers(self):
        self.assertEqual(True, grade_summarizer.hasNumbers("F17"))
        self.assertEqual(False, grade_summarizer.hasNumbers("FA"))
        self.assertEqual(True, grade_summarizer.hasNumbers("WN20"))
        self.assertEqual(False, grade_summarizer.hasNumbers("W"))

    @ignore_warnings
    def test_setTerm(self):
        courseListSmall = []
        canvas = Canvas(config.API_URL, config.API_KEY)
        courseListSmall.append(canvas.get_course(301754)) # ALA 421 Students WN 2019
        courseListSmall.append(canvas.get_course(314843)) # EECS 201 F19
        grade_summarizer.setTerms(courseListSmall)
        self.assertEqual("W19", courseListSmall[0].term)
        self.assertEqual("F19", courseListSmall[1].term)

    @ignore_warnings
    def test_getCoursesForTerm(self):
        courseListSmall = []
        canvas = Canvas(config.API_URL, config.API_KEY)
        courseListSmall.append(canvas.get_course(301754)) # ALA 421 Students WN 2019
        courseListSmall.append(canvas.get_course(314843)) # EECS 201 F19
        courseListSmall.append(canvas.get_course(275474)) # ASIAN 325 001 WN 2019
        grade_summarizer.setTerms(courseListSmall)
        courseListSemSmall = grade_summarizer.getCoursesForTerm(courseListSmall, "W19")
        self.assertEqual(2, len(courseListSemSmall))
        self.assertEqual("ALA 421 Students WN 2019", courseListSemSmall[0].name)
        self.assertEqual("ASIAN 325 001 WN 2019", courseListSemSmall[1].name)

if __name__ == '__main__':
    unittest.main()