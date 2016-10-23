import os

man, other = [], []
if os.path.exists("sketch"):
    thefile = open("sketch")

    for line in thefile:
        # print( line ,end="")
        if line.find(":") > -1:
            role, line_spoken = line.split(":", 1)
            line_spoken.strip()

            if role == "Man":
                man.append(line_spoken)
            else:
                other.append(line_spoken)

    thefile.close()
    # print(man)
    # print(other)
try:
    """
       with 使用了名为 上下文管理协议的Python技术
            (context management protocol)
    """
    with  open("mansd2","w") as data, open("mansays", "w") as man_out, open("othersays", "w") as other_out:
        # print(data.readline(), end="")
        print(man + other,file=data)
        print(man, file=man_out)
        print(other, file=other_out)
    # todo too many values to unpack
    """
    for man_line, other_line in man, other:
        man_out.write(man_line + " \n")
        other_out.write(other_line)
    """



except IOError as e:
    print("The io has creashed !", e)
"""
   字符串和java一样是不可改变的,当没有指向其的变量时,会被Python回收
"""
