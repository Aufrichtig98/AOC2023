def part_one():
    result = []
    time = [52, 94, 75, 94]
    distance = [426, 1374, 1279, 1216]
    #stupid solution because faster to code, could be solveable with a bit math
  #  time = [7,15,30]
   # distance = [9,40,200]


    for i in range(len(time)):
        time_for_dist = time[i]
        dist_to_beat = distance[i]
        dist_per_mil = 0
        valid_choices = 0
        for j in range(0,time_for_dist+1):
            if (time_for_dist - j) * dist_per_mil > dist_to_beat:
                valid_choices += 1
            dist_per_mil += 1
        result.append(valid_choices)
    res = 1
    for i in result:
        res *= i
    print(res)



if __name__ == '__main__':
    result = []
    time = [52947594]
    distance = [426137412791216]
    #stupid solution because faster to code, could be solveable with a bit math
  #  time = [7,15,30]
   # distance = [9,40,200]


    for i in range(len(time)):
        time_for_dist = time[i]
        dist_to_beat = distance[i]
        dist_per_mil = 0
        valid_choices = 0
        for j in range(0,time_for_dist+1):
            if (time_for_dist - j) * dist_per_mil > dist_to_beat:
                valid_choices += 1
            dist_per_mil += 1
        result.append(valid_choices)
    res = 1
    for i in result:
        res *= i
    print(res)
