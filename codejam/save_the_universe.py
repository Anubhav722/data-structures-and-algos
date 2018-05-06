N = int(raw_input())


def calculate_current_damage(x):
    min_damage_possible = 0
    damage = 1
    for i in x:
        if i == 'S':
            min_damage_possible += damage
        else:
            damage *= 2
    return min_damage_possible


for i in xrange(N):
    inp = raw_input()
    D = int(inp.split(' ')[0])
    x = inp.split(' ')[1]

    if x.count('S') > D:
        print "Case #" + str(i+1) + ": IMPOSSIBLE"
        continue

    min_damage_possible = calculate_current_damage(x)
    if min_damage_possible <= D:
        print "Case #" + str(i+1) + ": 0"
        continue

    count = 0
    current_damage = 9999999999

    new_str = x
    while current_damage > D:

        index = new_str.find('CS')
        new_str = new_str[:index] + new_str[index+1] + new_str[index] + new_str[index+2:]
        count += 1
        current_damage = calculate_current_damage(new_str)

    print "Case #" + str(i+1) + ": " + str(count)
