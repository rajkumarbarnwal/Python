def raj(magic, dist):
    if sum(magic) < sum(dist): return -1
    n = len(magic)
    add = 0
    start = 0
    for i in range(n):
        if add < 0:
            start = i
            add = 0
        add += (magic[i] - dist[i])
    return start
magic = [8,4,1,9]
dist = [10,9,3,5]
print(raj(magic,dist))
    
        
