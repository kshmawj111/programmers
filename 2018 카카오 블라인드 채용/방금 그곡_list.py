"""
테스트 1 〉	통과 (0.20ms, 10.5MB)
테스트 2 〉	통과 (0.21ms, 10.4MB)
테스트 3 〉	실패 (0.19ms, 10.4MB)
테스트 4 〉	통과 (0.20ms, 10.4MB)
테스트 5 〉	통과 (0.20ms, 10.4MB)
테스트 6 〉	통과 (0.22ms, 10.3MB)
테스트 7 〉	통과 (0.35ms, 10.3MB)
테스트 8 〉	실패 (0.36ms, 10.4MB)
테스트 9 〉	통과 (0.36ms, 10.4MB)
테스트 10 〉	통과 (0.62ms, 10.4MB)
테스트 11 〉	통과 (0.46ms, 10.4MB)
테스트 12 〉	실패 (0.35ms, 10.4MB)
테스트 13 〉	통과 (0.34ms, 10.4MB)
테스트 14 〉	통과 (0.36ms, 10.4MB)
테스트 15 〉	통과 (0.34ms, 10.4MB)
테스트 16 〉	통과 (0.29ms, 10.5MB)
테스트 17 〉	통과 (0.38ms, 10.4MB)
테스트 18 〉	통과 (0.36ms, 10.4MB)
테스트 19 〉	통과 (1.13ms, 10.4MB)
테스트 20 〉	통과 (0.46ms, 10.4MB)
테스트 21 〉	통과 (0.36ms, 10.4MB)
테스트 22 〉	통과 (0.35ms, 10.4MB)
테스트 23 〉	통과 (0.35ms, 10.4MB)
테스트 24 〉	통과 (0.36ms, 10.4MB)
테스트 25 〉	통과 (0.20ms, 10.5MB)
테스트 26 〉	통과 (0.21ms, 10.4MB)
테스트 27 〉	통과 (0.21ms, 10.2MB)
테스트 28 〉	통과 (0.22ms, 10.4MB)
테스트 29 〉	통과 (6.79ms, 10.4MB)
테스트 30 〉	통과 (6.53ms, 10.5MB)
"""
import re


def solution(memory, musicinfos):
    answer = "(None)"
    candidates = {}
    temp = [('C#', 'c'), ('D#', 'd'), ('F#', 'f'), ('G#', 'g'), ('A#', 'a')]

    for target, sub in temp:
        memory = memory.replace(target, sub)

    for music in musicinfos:
        music = re.split(',', music)
        h_d = int(music[1][:2]) - int(music[0][:2])
        m_d = int(music[1][3:]) - int(music[0][3:])
        played_minutes = h_d * 60 + m_d

        full_music = music[3]

        for t, s in temp:
            full_music = full_music.replace(t, s)

        if len(full_music) >= played_minutes:
            full_music = full_music[:played_minutes]

        else:
            while len(full_music) < len(memory) * 3:
                full_music += full_music

        if full_music.find(memory) != -1:
            candidates[music[2]] = played_minutes

    if len(candidates) > 1:
        max = 0
        for k, v in candidates.items():
            if v > max:
                max = v
                answer = k

    else:
        keys = list(candidates.keys())
        if keys:
            answer = keys[0]

    print(answer)
    return answer


if __name__ == '__main__':
    m, i = 	"ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    solution(m, i)