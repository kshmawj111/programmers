# https://programmers.co.kr/learn/courses/30/lessons/42884?language=python3



def solution(routes: list):
    num_cameras = 0
    cameras = []
    routes.sort(key=lambda x: x[1])
    camera_pos = -30001
    print(routes)
    for car in routes:
        s, e = car
        if camera_pos < s: # 진입 이전에 카메라가 있어 찍히지 않음
            num_cameras += 1 # 카메라 진출 구간에 하나 추가
            cameras.append(e)
            camera_pos = e # 진입과 진출 시점에서만 유의미한 변화를 가져옴

    print(cameras)
    return num_cameras



if __name__ == '__main__':
    r = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
    print(solution(r))