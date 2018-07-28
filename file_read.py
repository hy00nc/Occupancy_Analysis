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
        splitted_line = line.split(',')
        features.append(splitted_line[0:-1])
        changed_splitted_label = sub('\n', '', splitted_line[-1])
        labels.append(int(changed_splitted_label))

    return features, labels
