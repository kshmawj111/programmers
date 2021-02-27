# https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3


def cal_milliseconds(iso_time_format: str):
    hour = int(iso_time_format[:2])
    minute = int(iso_time_format[3:5])
    seconds = int(iso_time_format[6:8])
    msec = int(iso_time_format[9:])
    total = msec + seconds * 1000 + minute * 60 * 1000 + hour * 3600 * 1000
    return total


def calculate_start_time(input_string):
    s = input_string.split(' ')
    end_time_msec = cal_milliseconds(s[1])
    exe_time = int(float(s[2][:-1])*1000)
    start_time_msec = end_time_msec - exe_time + 1
    return start_time_msec, end_time_msec


def solution(lines):
    max_exe = 0
    i = -1
    table = {}
    for x in lines:
        i += 1
        start, end = calculate_start_time(x)
        threshold_e = end + 1000
        num_of_executed = 1

        for j in range(i+1, len(lines)):
            if not lines[j] in table.keys():
                s, e = calculate_start_time(lines[j])
                table[lines[j]] = (s, e)

            else:
                s, e = table[lines[j]]

            if s < threshold_e:
                num_of_executed += 1

            else:
                break

        if max_exe < num_of_executed:
            max_exe = num_of_executed

    return max_exe


if __name__ == '__main__':
    '''l =		["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s",
                "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s",
                "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s",
                "2016-09-15 21:00:02.066 2.62s"]'''
    l = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
    print(solution(l))
