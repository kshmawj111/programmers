# https://programmers.co.kr/learn/challenges


class Cache:
    def __init__(self, size):
        self.cache_table = []
        self.MAX_CACHE_SIZE = size
        self.exec_time = 0

    def calculate(self, data):
        if data in self.cache_table:
            self.cache_table.remove(data)
            self.cache_table.append(data)
            self.exec_time += 1
            return True

        else:
            if len(self.cache_table) >= self.MAX_CACHE_SIZE:
                self.cache_table.pop(0)
                self.cache_table.append(data)

            else:
                self.cache_table.append(data)

            self.exec_time += 5
            return False

    def swap(self, data1, data2):
        idx1 = self.cache_table.index(data1)
        idx2 = self.cache_table.index(data2)

        self.cache_table[idx1] = data2
        self.cache_table[idx2] = data1


def solution(cacheSize, cities):
    if cacheSize > 0:
        cache = Cache(cacheSize)
        cities = [c.lower() for c in cities]
        for c in cities:
            cache.calculate(c)

        answer = cache.exec_time
        print(answer)
        return answer

    else:
        return len(cities) * 5



if __name__ == '__main__':
    c_size, cities = 	2, ["Jeju", "Pangyo", "NewYork", "newyork"]
    solution(c_size, cities)