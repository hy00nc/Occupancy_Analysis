from re import sub

def file_open(txt):
    f = open(txt, mode="r", encoding="utf-8")

    return f

def makeData(mode):
    if mode == "training":
        f = file_open("datatraining.txt")
    elif mode == "test":
        f = file_open("datatest.txt")

    lines = f.readlines()

    features = list()
    labels = list()

    is_first_line = True
    for line in lines:
        if is_first_line:
            is_first_line = False
            continue
        splitted_line = line.split(',')[2:]
        splitted_line[-1] = sub("\n", "", splitted_line[-1])
        new_list = list()
        for attribute in splitted_line:
            new_list.append(float(attribute))
        features.append(new_list[0:-1])
        labels.append(new_list[-1])

    return features, labels
