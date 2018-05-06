N = input()

for y in xrange(N):
    n = input()
    arr = map(int, raw_input().split(' '))

    sorted_arr = sorted(arr)

    count = 1

    for j in xrange(len(arr)):
        if count == 0:
            break
        else:
            count = 0
        for i in xrange(len(arr) - 2):
            if arr[i] > arr[i + 2]:
                arr[i + 2], arr[i] = arr[i], arr[i + 2]
                count += 1

    if sorted_arr == arr:
        print "Case #" + str(y + 1) + ": OK"
    else:
        a = [i for i in xrange(len(arr)) if arr[i] != sorted_arr[i]]
        print "Case #" + str(y + 1) + ": " + str(a[0])
