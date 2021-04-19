def a():
    count = int(input())
    lessons = []
    for i in range(count):
        lesson = list(map(float, input().split(' ')))
        lessons.append(lesson)
    lessons = sorted(lessons, key=lambda item: (item[1], item[0]))
    for i in range(count):
        while i < count - 1 and lessons[i][1] > lessons[i + 1][0]:
            lessons.pop(i + 1)
            count -= 1
        if i < count - 1 and (int(lessons[i][1]) > int(lessons[i+1][0])):
            lessons[i][1] = int(lessons[i][1])
            lessons[i+1][0] = int(lessons[i+1][0])
    lessons[0][0] = int(lessons[0][0])
    print(count)
    for lesson in lessons:
        print(*lesson)


a()
