import heapq
 
heap = []  
heapq.heappush(heap, 3)  
heapq.heappush(heap, 1)  
heapq.heappush(heap, 10)  
heapq.heappush(heap, 5)  
heapq.heappush(heap, 8)

print(heap) # [1, 3, 10, 5, 8]