def insert_into_heap(heap, x):
    heap.append(x)
    curr = len(heap)-1
    parent = (curr - 1)//2

    while True:
        if heap[curr] > heap[parent]:
            heap[curr],heap[parent] = heap[parent],heap[curr]
            curr = parent
            parent = (curr-1)//2
            if parent < 0:
                break
        else:
            break
    return heap
    
