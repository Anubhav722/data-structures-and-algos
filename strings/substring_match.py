x = 'strongest'
y = 'whythestrongboy'


def check(x, y):
    i = 0
    z = ''
    start = -1
    for j in range(len(y)):
        if len(z) == len(x):
            return start

        if y[j] == x[i]:
            i += 1
            z += y[j]
            if start == -1:
                start = j

        else:
            i = 0
            z = ''
            start = -1
    return start

print check(x, y)
