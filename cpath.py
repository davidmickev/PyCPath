import sys
from heapq import heappush, heappop

if __name__ == '__main__':

    # input args for The usage is \cpath <file> <s> <d> <budget>".
    file = sys.argv[1]
    start = int(sys.argv[2])
    dest = int(sys.argv[3])
    budget = int(sys.argv[4])

    # open file, parse the given input of U, V, C, T
    fopen = open(file, 'r')
    lines = fopen.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()

    print("The file you have input: ")
    print(lines)

    numlines = int(lines[0])
    vertices = [[] for i in range(numlines)]

    #for the input file above, starting wtih secon line
    for line in lines[1:]:
        line = line.split(' ')

        # \u v c t" which says there is an edge from
        # u to v with cost c and traversal time t.
        u = int(line[0])
        v = int(line[1])
        c = int(line[2])
        t = int(line[3])

        #cost time ,  U V
        vertices[u].append([c,t,u,v, []])
    print("List of vertices c,t,u,v")
    # for i in range(len(vertices)):
    #     print (vertices[i])

    # print (" (c; t); u v ")
    # print (costTime)
    costTime = [[] for i in range(numlines)]

    heapify = []
    # push cost 0 time 0, S = V (source vertice)
    # (c; t); v >
    heappush(heapify, [0,0,start,start, []])

    while len(heapify) > 0:

        min_e = heappop(heapify)

        # if there is no current best, we have a new current best.
        if len(costTime[min_e[3]]) == 0:
            costTime[min_e[3]].append(min_e)

        # else, we have to check
        else:
            currentBest = costTime[min_e[3]][-1]
            # if current S[v] price is less than compared price, and time is worse on the current best
            if currentBest[0] < min_e[0] and currentBest[1] > min_e[1]:
                costTime[min_e[3]].append(min_e)
        # after we pop from queue, we inspect all of the outgoing edges
        for edges in vertices[min_e[3]]:
            # how to get to (u -> v)? add them, check if there is
            #     cost                  ,   time              ,source  , dest    , path[]
            temp = [edges[0] + min_e[0], edges[1] + min_e[1], min_e[2], edges[3], []]
            #append the path to get to this vertice
            temp[4] = min_e[4].copy()
            temp[4].append(edges[2])

            #check if destination of new path is better or worse, if better, add to heap.
            if len(costTime[temp[3]]) == 0:
                heappush(heapify,temp)
            else:
                currentBest = costTime[temp[3]][-1]
                if currentBest[0] < temp[0] and currentBest[1] > temp[1]:
                    heappush(heapify,temp)

    print("Printing best paths")
    print (costTime)
    for i in range(len(costTime)):

        print (costTime[i])

    print("printing cost/ time")
    print(costTime)
    paths = []





    # # u = int(line[0])
    # # v = int(line[1])
    # # c = int(line[2])
    # # t = int(line[3])
    # paths = []
    # for entry in range(len(costTime)):
    #     for row in entry:
    #         print(entry[row])
    #     #print(type(start),entry[2])
    #     #if start%entry[2] == 0:
    #     # if start == entry[2] and dest == entry[3]:
    #
    #     #paths.append(entry)
    #
    # # for i in range(len(costTime)):
    # #     print(paths[i])
    # #     print("test")
    # print(start,dest)
    # print(paths)




