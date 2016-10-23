import pickle

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
            print(james_score)
        print("julie score : ", julie.readline().strip().split(","))

    with open("sarah.txt", "r")as sarah, open("mikey.txt", "r")as mikey:
        objects = sarah.readline().strip().split(",")
        print("sarah score : ", objects.sort())
        print("sarah score : ", sorted(objects))
        print("mikey score : ", mikey.readline().strip().split(","))

except IOError as err:
    print("the cause are ", err, end="")


def sanitize(str):
    print(str ,"-----------")
    if not str.find(".") == -1:
        return str
    if str.find("-") > -1 or str.find(":") > -1:
        str.replace("-", ".")
        print("------",str.replace(":", "."))

        return str
