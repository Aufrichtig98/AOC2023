def part_one():
    pass


    def find_number(pos:(int,int), map:list[list[str]]):

        full_number = map[pos[0]][pos[1]]
        #check_left
        for i in range(pos[1] - 1, -1, -1):
            if map[pos[0]][i].isdigit():
                full_number = map[pos[0]][i] + full_number
            else:
                break
        #check right
        for i in range(pos[1] + 1, len(map[pos[0]])):
            if map[pos[0]][i].isdigit():
                full_number = full_number + map[pos[0]][i]
            else:
                break

        return int(full_number)

    def search_number(pos:(int,int), map:list[list[str]]):

        result_list = list()
        #left
        if map[pos[0]][pos[1]-1].isdigit():
             result_list.append(find_number((pos[0], pos[1]-1), map))
        #right
        if map[pos[0]][pos[1]+1].isdigit():
            result_list.append(find_number((pos[0], pos[1]+1), map))
        #down
        if map[pos[0]+1][pos[1]].isdigit():
            result_list.append(find_number((pos[0]+1, pos[1]), map))
        #up
        if map[pos[0]-1][pos[1]].isdigit():
            result_list.append(find_number((pos[0]-1, pos[1]), map))
        #up left
        if map[pos[0]-1][pos[1]-1].isdigit():
            result_list.append(find_number((pos[0]-1, pos[1]-1), map))
        #down right
        if map[pos[0]+1][pos[1]+1].isdigit():
            result_list.append(find_number((pos[0]+1, pos[1]+1), map))
        #down left
        if map[pos[0]+1][pos[1]-1].isdigit():
            result_list.append(find_number((pos[0]+1, pos[1]-1), map))
        #up right
        if map[pos[0]-1][pos[1]+1].isdigit():
            result_list.append(find_number((pos[0]-1, pos[1]+1), map))

        return result_list

    if __name__ == '__main__':
        map:list[list[str]] = []
        with open("input.txt", "rt") as myfile:
            for line in myfile:
                map.append(list(line.strip("\n")))

        result_list = list()


        for i in range(len(map)):
            for j in range(len(map[i])):
                if not map[i][j].isdigit() and (map[i][j] != '.'):
                    nums = search_number((i,j), map)
                    #nothing found
                    if not nums:
                        continue
                    else:
                        #remove all duplicates
                        result_list.append(list(set(nums)))

        for i in result_list:
            print(i)
        print(sum([sum(i) for i in result_list]))


"__________________________________________________Part Two__________________________________________________________"


def find_number(pos:(int,int), map:list[list[str]]):

    full_number = map[pos[0]][pos[1]]
    #check_left
    for i in range(pos[1] - 1, -1, -1):
        if map[pos[0]][i].isdigit():
            full_number = map[pos[0]][i] + full_number
        else:
            break
    #check right
    for i in range(pos[1] + 1, len(map[pos[0]])):
        if map[pos[0]][i].isdigit():
            full_number = full_number + map[pos[0]][i]
        else:
            break

    return int(full_number)

def search_number(pos:(int,int), map:list[list[str]]):

    result_list = list()
    #left
    if map[pos[0]][pos[1]-1].isdigit():
         result_list.append(find_number((pos[0], pos[1]-1), map))
    #right
    if map[pos[0]][pos[1]+1].isdigit():
        result_list.append(find_number((pos[0], pos[1]+1), map))
    #down
    if map[pos[0]+1][pos[1]].isdigit():
        result_list.append(find_number((pos[0]+1, pos[1]), map))
    #up
    if map[pos[0]-1][pos[1]].isdigit():
        result_list.append(find_number((pos[0]-1, pos[1]), map))
    #up left
    if map[pos[0]-1][pos[1]-1].isdigit():
        result_list.append(find_number((pos[0]-1, pos[1]-1), map))
    #down right
    if map[pos[0]+1][pos[1]+1].isdigit():
        result_list.append(find_number((pos[0]+1, pos[1]+1), map))
    #down left
    if map[pos[0]+1][pos[1]-1].isdigit():
        result_list.append(find_number((pos[0]+1, pos[1]-1), map))
    #up right
    if map[pos[0]-1][pos[1]+1].isdigit():
        result_list.append(find_number((pos[0]-1, pos[1]+1), map))

    if len(list(set(result_list))) == 2 and map[pos[0]][pos[1]] =='*':
        return [list(set(result_list))[0]*list(set(result_list))[1]]
    return [0]

if __name__ == '__main__':
    map:list[list[str]] = []
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            map.append(list(line.strip("\n")))

    result_list = list()


    for i in range(len(map)):
        for j in range(len(map[i])):
            if not map[i][j].isdigit() and (map[i][j] != '.'):
                nums = search_number((i,j), map)
                #nothing found
                if not nums:
                    continue
                else:
                    #remove all duplicates
                    result_list.append(list(set(nums)))

    for i in result_list:
        print(i)
    print(sum([sum(i) for i in result_list]))
