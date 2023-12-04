def part_one():
    requests = []
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(line.strip("\n").split(":")[1].split(" "))
    for scratch_indx, scratch in enumerate(requests):
        list_indx = 0
        tmp_list = [[],[]]
        for char in scratch:
            if char == "|":
                list_indx += 1
                continue
            if char.isdigit():
                tmp_list[list_indx].append(char)
        requests[scratch_indx] = tmp_list

    result = 0
    for scratch in requests:
        len_both = len(scratch[0]) + len(scratch[1])
        len_unique = len(set(scratch[0]).union(scratch[1]))
        duplicates = len_both - len_unique
        if duplicates:
            result += 2 ** (duplicates-1)
    print(result)

if __name__ == '__main__':
    requests = []
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(line.strip("\n").split(":")[1].split(" "))
    for scratch_indx, scratch in enumerate(requests):
        list_indx = 0
        tmp_list = [[],[]]
        for char in scratch:
            if char == "|":
                list_indx += 1
                continue
            if char.isdigit():
                tmp_list[list_indx].append(char)
        requests[scratch_indx] = (1, tmp_list)

    result = 0
    for scratch_indx, scratch in enumerate(requests):
        len_both = len(scratch[1][0]) + len(scratch[1][1])
        len_unique = len(set(scratch[1][0]).union(scratch[1][1]))
        duplicates = len_both - len_unique
        for i in range(duplicates):
            requests[scratch_indx + i + 1] = (requests[scratch_indx + i + 1][0] + requests[scratch_indx][0], requests[scratch_indx + i + 1][1])

    print(sum([i[0] for i in requests]))
