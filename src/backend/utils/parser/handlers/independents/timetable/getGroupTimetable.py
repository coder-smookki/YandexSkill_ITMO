import requests
from bs4 import BeautifulSoup as bs
from ...utils.textNormalizer.index import textNormalizer


def getGroupTimetable(args, lang):
    result = []

    if not isinstance(args, list):
        raise TypeError(
            "The argument to the findGroups must be an array: [groupname(str), degree(int)]."
        )

    groupName = args[0]
    course = groupName[2]
    # 3 - бакалавриат
    # 4 - магистратура
    # 5 - специалитет
    degreeWord = args[1]

    # Degree must be:
    #     3 - undergraduate (бакалавриат)
    #     4 - magistracy (магистратура)
    #     5 - specialty (специалитет)
    if "бакал" in degreeWord or "unde" in degreeWord or "bac" in degreeWord:
        degree = 3
    elif "магис" in degreeWord or "magis" in degreeWord:
        degree = 4
    elif "спец" in degreeWord or "spec" in degreeWord:
        degree = 4
    else:
        return False

    if lang == "ru-RU":
        url = (
            "https://student.itmo.ru/ru/timetable/"
            + groupName
            + "/"
            + course
            + "/"
            + str(degree)
        )
    else:
        url = (
            "https://student.itmo.ru/en/timetable/"
            + groupName
            + "/"
            + course
            + "/"
            + str(degree)
        )

    # https://student.itmo.ru/ru/timetable/A4130/1/4/
    # group/course/degree

    try:
        r = requests.get(url)
    except:
        return False

    soup = bs(r.text, "html.parser")
    lectures = soup.select(".timetable-article__row:nth-child(n+3)")
    if len(lectures) < 2:
        return False

    for lecture in lectures:
        if lecture.select_one(".timetable-article__day") is None:
            continue
        lectureResult = {}
        lectureResult["dayWeek"] = textNormalizer(
            lecture.select_one(".timetable-article__day").getText()
        )
        lectureResult["date"] = textNormalizer(
            lecture.select_one(".timetable-article__date").getText()
        )
        time = textNormalizer(
            lecture.select_one(".timetable-article__col-time").getText()
        ).split(" ", maxsplit=1)
        lectureResult["hours"] = textNormalizer(time[0])
        lectureResult["whatWeeks"] = textNormalizer(time[1])
        lectureResult["subjectName"] = textNormalizer(
            lecture.select_one(".timetable-article__subject").getText()
        )
        lectureResult["lecturerName"] = textNormalizer(
            lecture.select_one(".timetable-article__instructor").getText()
        )
        lectureResult["classroomNumber"] = textNormalizer(
            lecture.select_one(".timetable-article__room:first-child").getText()
        )
        lectureResult["classroomAddress"] = textNormalizer(
            lecture.select_one(".timetable-article__address address").getText()
        )
        lectureResult["classroomNavigator"] = lecture.select_one(
            ".timetable-article__address a"
        ).get("href")
        lectureResult["classFormat"] = textNormalizer(
            lecture.select_one(".timetable-article__room:last-child").getText()
        )
        result.append(lectureResult)
    return result
