from binary_heap import BHeap

if __name__ == "__main__":
    array = [None]*1
    array.append([90, 'watermelon'])
    array.append([80, 'pear'])
    array.append([70, 'melon'])
    array.append([50, 'lime'])
    array.append([60, 'mango'])
    array.append([20, 'cherry'])
    array.append([30, 'grape'])
    array.append([35, 'orange'])
    array.append([10, 'apricot'])
    array.append([15, 'banana'])
    array.append([45, 'lemon'])
    array.append([40, 'kiwi'])
    bheap = BHeap(array)

    bheap.create_heap()
    print("최소 힙:")
    bheap.print_heap()
