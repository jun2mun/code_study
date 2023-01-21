def turn_left(M,key):
    new_key = [[0] * M for _ in range(M)]
    #key[0][:] -> new_key[:][-1]
    #key[1][:] -> new_key[:][-2]
    for k in range(M):
        for i in range(M):
            new_key[i][-k-1] = key[k][i] 
    return new_key


if __name__ == '__main__':
    keys = [[0,0,0],[1,0,0],[0,1,1]]; lock = [[1,1,1],[1,1,0],[1,0,1]]
    rotate_90_key =turn_left(len(keys),keys)
    rotate_180_key = turn_left(len(keys),rotate_90_key)
    rotate_270_key = turn_left(len(keys),rotate_180_key)
    graph = [[0]*9 for _ in range(9)]
    for i in range(3,6):
        for k in range(3,6):
            graph[i][k] = keys[i-3][k-3]
    
    temp = graph[:]
    
    for i in range(6):
        for k in range(6):
            for x in range(3):
                for y in range(3):
                    graph[i+x][k+x] = keys[x][y]
            
            if graph[3:6][3:6] == keys:
                print('true')
            graph = temp

    for i in range(6):
        for k in range(6):
            for x in range(3):
                for y in range(3):
                    graph[i+x][k+x] = rotate_90_key[x][y]
            
            if graph[3:6][3:6] == rotate_90_key:
                print('true')
            graph = temp
    for i in range(6):
        for k in range(6):
            for x in range(3):
                for y in range(3):
                    graph[i+x][k+x] = rotate_180_key[x][y]
            
            if graph[3:6][3:6] == rotate_180_key:
                print('true')
            graph = temp

    for i in range(6):
        for k in range(6):
            for x in range(3):
                for y in range(3):
                    graph[i+x][k+x] = rotate_270_key[x][y]
            
            if graph[3:6][3:6] == rotate_270_key:
                print('true')
            graph = temp