def read_file(path):
    f = open(path, "r")
    ret = []
    for x in f:
        s = x.split(" ")
        ret.append([float(s[0]), float(s[1]), float(s[2])])
    return ret
