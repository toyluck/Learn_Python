"""
   (@link www.baidu.com)
"""
from Head_First_Python.charpter6.Athlete import Althlete
from Head_First_Python.charpter6.AthleteList import AthleteList


def sanitize(str):
    if not str.find(".") == -1:
        return str
    if str.find("-") > -1 or str.find(":") > -1:
        str = str.replace("-", '.')
        str = str.replace(":", '.')
        return str


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline().strip().split(",")
            althlete = AthleteList(data.pop(0), data.pop(0), [sanitize(each_score) for each_score in data])
            return althlete
    except IOError as ioerr:
        print('File error', ioerr)
    return None


try:
    """
       (In-Place sorting) 原地排序 会替换原有的
       (Copied sorting) 返回一个排序后的副本
    """
    james_scores = get_coach_data("james2.txt")
    james_scores.add_time("1.2")
    print(james_scores.top3())


except IOError as err:
    print("the cause are ", err, end="")
