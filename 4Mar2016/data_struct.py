# list
print('List')
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1)
a.append(333)
print(a)
print(a.index(333))
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.pop()
print(a)

#Using Lists as Stacks
print("Using Lists as Stacks")

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)


# Using Lists as Queues
print('\n  Using Lists as Queues')

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue)
print(queue.popleft() )                # The first to arrive now leaves
print(queue.popleft()  )
print(queue)


squares = []
for x in range(10):
     squares.append(x**2)


print(squares)

 


squares = [x**2 for x in range(10)]
print(squares)

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])


combs = []
for x in [1,2,3]:
     for y in [3,1,4]:
         if x != y:
              combs.append((x, y))
print(combs)




























