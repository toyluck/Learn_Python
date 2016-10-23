import pickle


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
            data = f.readline()
            return (data.strip().split(","))
    except IOError as ioerr:
        print('File error', ioerr)


try:
    """
       (In-Place sorting) 原地排序 会替换原有的
       (Copied sorting) 返回一个排序后的副本
    """
    james_scores = get_coach_data("james2.txt")
    (name, brd) = james_scores.pop(0), james_scores.pop(0)
    james_data = {"name": james_scores.pop(0), "bod": james_scores.pop(0)}
    sorted_scores = (sorted(set((sanitize(each_score) for each_score in james_scores)))[0:3])
    james_data["Times"] = sorted_scores
    print(james_data["name"], " birthday : ", james_data["bod"], "-- ", james_data["Times"])


except IOError as err:
    print("the cause are ", err, end="")
