# from array import *
# vals=array('i',[5,3,2,4])
# for i in range():
#    print(vals[i])

# from array import *
# arr=array('i',[])

# n=int(input("Enter the length of the array: "))
# for i in range(n):
#     x=int(input("Enter the next value: "))
#     arr.append(x)
# print("The values in the array are: ",arr,end="")

# val=int(input("Enter the  value for search: "))
# k=0
# for e in arr:
#     if e==val:
#         print(k)
#         break
#     k+=1


queue = []

def is_empty():
    return len(queue) == 0

def enqueue(item):
    queue.append(item)
    print(f"{item} enqueued")

def dequeue():
    if is_empty():
        print("Queue is empty, cannot dequeue")
        return None
    return queue.pop(0)

def peek():
    if is_empty():
        return None
    return queue[0]

def display():
    print("Queue:", queue)


enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)
display()

print("Dequeued:", dequeue())
display()
