def read_classification(path: str, inputs_count: int, outputs_count: int):
    file = open(path, "r")
    ret = []
    for x in file:
        inputs = []
        outputs = []
        s = x.split(" ")
        counter = 0
        for i in range(inputs_count):
            inputs.append(s[counter])
            counter += 1
        for i in range(outputs_count):
            outputs.append(s[counter])
            counter += 1
        ret.append([inputs, outputs])
    return ret
