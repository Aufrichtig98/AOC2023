from collections import defaultdict

def part_one():
    requests = []
    bag_content = {"red": 12, "green": 13, "blue":14}

    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(line.strip("\n").split(":")[1].split(";"))
            game_subset = list()
            for game in requests[-1]:
                ball_map = defaultdict(lambda: 0)
                for balls in game.split(","):
                    #Cut off empty string
                    tmp = (balls[1:].split(" "))
                    ball_map[tmp[1]] = int(tmp[0])
                game_subset.append(ball_map)
            requests[-1] = game_subset

    result_id = list()
    for i in range(len(requests)):
        impossible = False
        for color,amount in bag_content.items():
            for sub_game in requests[i]:
                if sub_game[color] > bag_content[color]:
                    impossible = True
                    break
            if impossible:
                break
        if not impossible:
            result_id.append(i+1)

    print(sum(result_id))



if __name__ == '__main__':
    requests = []
    bag_content = {"red": 12, "green": 13, "blue":14}

    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(line.strip("\n").split(":")[1].split(";"))
            ball_map = defaultdict(lambda: 0)
            for game in requests[-1]:
                for balls in game.split(","):
                    #Cut off empty string
                    tmp = (balls[1:].split(" "))
                    if int(tmp[0]) > ball_map[tmp[1]]:
                        ball_map[tmp[1]] = int(tmp[0])
            requests[-1] = ball_map

    result = list()
    #for i in requests:
    #    print(i)
    for i in range(len(requests)):
        result.append(1)
        for amount in requests[i].values():
            result[-1] *= amount

    print(sum(result))


