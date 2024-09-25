
def make_distinct(dials):
    actions = []
    seen = set()

    for i in range(len(dials)):
        while dials[i] in seen:
            dials[i] = (dials[i] + 1) % 10
            actions.append('+')
        seen.add(dials[i])
        if i < len(dials) - 1:
            actions.append('>')

    return ''.join(actions)

print(make_distinct([3, 2, 7]))  
print(make_distinct([8, 8, 0, 9])) 
print(make_distinct([0, 1, 0, 2, 0]))
