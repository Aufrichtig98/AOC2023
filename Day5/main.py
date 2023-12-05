def part_one():
    if __name__ == '__main__':
        requests = []
        with open("input.txt", "rt") as myfile:
            for line in myfile:
                requests.append(line.strip("\n").split(" "))
        seeds = [int(i) for i in requests[0][1:]]
        input_parsed_list = list()
        tmp_list = list()

        for request in requests[1:]:
            if request == ['']:
                if tmp_list:
                    input_parsed_list.append(tmp_list)
                tmp_list = list()
                continue
            elif not request[0].isdigit():
                continue
            else:
                tmp_list.append([int(i) for i in request])
        input_parsed_list.append(tmp_list)
        #List containing all the map transformation

        seeds_to_location = list()
        for seed in seeds:
            for mapping in input_parsed_list:
                for transformation in mapping:
                    if transformation[1] <= seed and seed <= transformation[1] + (transformation[2] - 1):
                        seed = transformation[0] + (seed - transformation[1])
                        break
            seeds_to_location.append(seed)
        print(min(seeds_to_location))

if __name__ == '__main__':
    requests = []
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(line.strip("\n").split(" "))
    seeds = [int(i) for i in requests[0][1:]]
    tmp_list = list()
    for i in range(len(seeds)):
        if not i % 2:
            tmp_list.append((seeds[i], seeds[i+1]))
    seeds = tmp_list
    print(seeds)
    input_parsed_list = list()
    tmp_list = list()

    for request in requests[1:]:
        if request == ['']:
            if tmp_list:
                input_parsed_list.append(tmp_list)
            tmp_list = list()
            continue
        elif not request[0].isdigit():
            continue
        else:
            tmp_list.append([int(i) for i in request])
    input_parsed_list.append(tmp_list)
    #List containing all the map transformation

    seeds_to_location = list()
    for seed in seeds:
        for mapping in input_parsed_list:
            for transformation in mapping:
                if transformation[1] <= seed and seed <= transformation[1] + (transformation[2] - 1):
                    seed = transformation[0] + (seed - transformation[1])
                    break
        seeds_to_location.append(seed)
    print(min(seeds_to_location))
