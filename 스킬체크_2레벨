# 방문길이
def solution(dirs):
    control = {'U' : (0, 1), 'D' : (0, -1), 'L' : (-1, 0), 'R' : (1, 0)}
    road = set()

    cha_x, cha_y = (0, 0)

    for i in dirs:
        next_x, next_y = cha_x + control[i][0], cha_y + control[i][1]
        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            road.add((cha_x,cha_y,next_x,next_y))
            road.add((next_x,next_y,cha_x,cha_y))
            cha_x, cha_y = next_x, next_y

    return len(road) // 2
    
# 캐시
def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = [city.lower() for city in cities]

    if cacheSize != 0:
        for city in cities:
            if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
            else:
                if len(cache) < cacheSize:
                    cache.append(city)
                    answer += 5
                else:
                    cache.pop(0)
                    cache.append(city)
                    answer += 5
    else:
        answer += len(cities) * 5
    return answer
