def a(courses):
    result = []
    for course in courses:
        if course not in result:
            result.append(course)

    return '\n'.join(result)


if __name__ == '__main__':
    count = int(input())
    courses = []
    for i in range(count):
        course = input()
        courses.append(course)
    print(a(courses))
