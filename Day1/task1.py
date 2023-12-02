def part_one():
    if __name__ == '__main__':
        requests = []
        with open("test.txt", "rt") as myfile:
            for line in myfile:
                requests.append(line.strip("\n").split(" "))

        print(sum([int(''.join(filter(str.isdigit, s[0]))[0] + ''.join(filter(str.isdigit, s[0]))[-1] ) for s in requests]))


if __name__ == '__main__':

    name_map = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

    if __name__ == '__main__':
        results = []
        results_tmp = []
        with open("test.txt", "rt") as myfile:
            for line in myfile:
                request_str = (line.strip("\n"))
                tmp = ''
                for i in request_str:
                    found = False
                    tmp += i
                    if i.isdigit():
                        results_tmp.append(i)
                        break
                    for key,value in name_map.items():
                        if key in tmp:
                            results_tmp.append(str(value))
                            found = True
                            break
                    if found:
                        found = False
                        break
                tmp = ''
                for i in reversed(request_str):
                    tmp = i + tmp
                    if i.isdigit():
                        results_tmp.append(i)
                        break
                    for key,value in name_map.items():
                        if key in tmp:
                            results_tmp.append(str(value))
                            found = True
                            break
                    if found:
                        break
                results.append(int(results_tmp[0] + results_tmp[1]))
                print(results_tmp)
                results_tmp = list()
            print(sum(results))
