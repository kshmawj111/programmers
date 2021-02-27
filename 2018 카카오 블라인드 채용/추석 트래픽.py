# https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3
from datetime import datetime, timedelta


def convert_string_to_time(input_string):
    end_time = datetime.strptime(input_string[:23], '%Y-%m-%d %H:%M:%S.%f')
    start_time = end_time - timedelta(milliseconds=int(float(input_string[24:-1]) * 1000)) + timedelta(milliseconds=1)
    return start_time, end_time


def solution(lines):
    max_exe = 0
    i = -1
    table = {}
    for x in lines:
        i += 1
        start, end = convert_string_to_time(x)
        threshold_s = start + timedelta(seconds=1)
        threshold_e = end + timedelta(seconds=1)
        num_of_executions = 1

        for j in range(i+1, len(lines)):
            if not lines[j] in table.keys():
                s, e = convert_string_to_time(lines[j])
                table[lines[j]] = (s, e)

            else:
                s, e = table[lines[j]]

            if s < threshold_e:
                num_of_executions += 1
            
            else:
                break

        if max_exe < num_of_executions:
            max_exe = num_of_executions

    return max_exe


if __name__ == '__main__':
    l = ["2016-09-15 01:00:04.000 2.0s", "2016-09-15 01:00:06.999 2s"]
    print(solution(l))
