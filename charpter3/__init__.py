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
    data = open("mansd");
    print(data.readline(), end="")
    man_out = open("mansays", "w")
    other_out = open("othersays", "w")
    # todo too many values to unpack
    """
    for man_line, other_line in man, other:
        man_out.write(man_line + " \n")
        other_out.write(other_line)
    """
    print(man, file=man_out)
    raise IOError
    print(other, file=other_out)
    man_out.close()
    other_out.close()

except IOError as e :
    print("The io has creashed !",e)
finally:
    if "" in locals():
        man_out.close()
        other_out.close()

        print("every io has closed ")
"""
   字符串和java一样是不可改变的,当没有指向其的变量时,会被Python回收
"""
