import pickle


def sanitize(str):
    if str.find("-") > -1 or str.find(":") > -1:
        str = str.replace("-", '.')
        str = str.replace(":", '.')
    return str


try:
    """
       (In-Place sorting) 原地排序 会替换原有的
       (Copied sorting) 返回一个排序后的副本
    """
    with open("james.txt", "r") as james, open("julie.txt", "r")as julie:
        """
           python 对字符串的排序依据编码位置
        """
        james_scores = james.readline().strip().split(",")
        print("james score : ", james_scores)
        for james_score in james_scores:
            # print(sanitize(james_score))
            pass
            """
               列表推导，属于函数式编程
            """
        julie_scores = sorted([sanitize(each_score) for each_score in julie.readline().strip().split(",")])
        """
           java中的 set集合，这里直接接受一个可迭代对象，返回该对象set类型的副本
        """
        julie_scores = set(julie_scores)

        print("julie score : ", julie_scores)

    with open("sarah.txt", "r")as sarah, open("mikey.txt", "r")as mikey:
        # objects = sarah.readline().strip().split(",")
        sarah_scores = sorted([sanitize(each_score) for each_score in sarah.readline().strip().split(",")])
        """
           要记住sorted 返回的是副本，传入的集合本身不改变
        """
        sorted(sarah_scores)
        print(sarah_scores)
        # filter duplicate
        print("original sarah_scores= ", sarah_scores)
        for sarah_score in sarah_scores:
            new_scroes = sarah_scores[sarah_scores.index(sarah_score) + 1:]
            # print(sarah_score , "   --- new_scroes == ", new_scroes)
            if sarah_score in new_scroes:
                # print(sarah_score, " is single")
                sarah_scores.remove(sarah_score)
                # print("mikey score : ", mikey.readline().strip().split(","))
        print(sarah_scores[0:3])
except IOError as err:
    print("the cause are ", err, end="")
