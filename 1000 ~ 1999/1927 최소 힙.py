import sys
import heapq

heap = []
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if(n > 0):
        heapq.heappush(heap, n)
    elif(n == 0):
        try:
            print(heapq.heappop(heap))
        except:
            print(0)