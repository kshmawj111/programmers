import re


def solution(memory, musicinfos):
    answer = "(None)"
    candidates = {}
    m_split = re.findall('[A-G]#*', memory)
    m_split = ''.join(map(lambda x: x + ' ', m_split))

    for music in musicinfos:
        music = re.split(',', music)
        h_d = int(music[1][:2]) - int(music[0][:2])
        m_d = int(music[1][3:]) - int(music[0][3:])
        played_minutes = h_d * 60 + m_d

        full_music = ''.join(map(lambda x: x + ' ', re.findall('[A-G]#*', music[3])))

        if len(full_music) // 2 >= played_minutes:
            full_music = full_music[:played_minutes*2]

        else:
            while len(full_music) < len(m_split) * 3:
                full_music += full_music

        if full_music.find(m_split) != -1:
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

    return answer