# import heapq
# class Parking:
#     def __init__(self,n):
#         self.free_slot = list(range(1,n+1))
#         heapq.heapify(self.free_slot)
#         self.car_to_slot = {}
    
#     def park(self,car):
#         if not self.free_slot :
#             return "Parking Full"
#         slot = heapq.heappop(self.free_slot)
#         self.car_to_slot[car]=slot
#         print(f'Car {car} part at {slot}')

#     def leave(self, car):
#         if car not in self.car_to_slot:
#             print("Car not found")
#             return
#         slot = self.car_to_slot.pop(car)
#         heapq.heappush(self.free_slot,slot)
#         print(f"Car {car}leave from {slot}")

# p = Parking(2)
# print(p.free_slot)
# print(p.car_to_slot)
# print()
# p.park("abc")
# print(p.free_slot)
# print(p.car_to_slot)
# print()
# p.park("def")
# print(p.free_slot)
# print(p.car_to_slot)
# print()
# p.park("xyz")
# p.leave("abc")
# print(p.free_slot)
# print(p.car_to_slot)
# print()
# p.park("xyz")
# print(p.free_slot)
# print(p.car_to_slot)
# print()


# from collections import OrderedDict

# class LRUCache:
#     def __init__(self, capacity):
#         self.cache = OrderedDict()
#         self.capacity = capacity

#     def get(self, key):
#         if key not in self.cache:
#             return -1
#         self.cache.move_to_end(key)
#         return self.cache[key]

#     def put(self, key, value):
#         if key in self.cache:
#             self.cache.move_to_end(key)
#         self.cache[key] = value
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last=False)

# from collections import OrderedDict

# class LRUCache:
#     def __init__(self,capacity):
#         self.cache = OrderedDict()
#         self.capacity = capacity


#     def get(self,key):
#         if key not in self.cache:
#             return -1
#         self.cache.move_to_end(key)
#         return self.cache[key]


#     def put(self,key, value):
#         if key in self.cache:
#             self.cache.move_to_end(key)
#         self.cache[key]= value
#         if len(self.cache)>self.capacity:
#             self.cache.popitem(last=False)


# from collections import deque
# class Editor:
#     def __init__(self):
#         self.slack = deque()

#     def add(self,text):
#         self.slack.append(text)

#     def undo(self):
#         if self.slack:
#             self.slack.pop()

#     def get_text(self):
#         return " ".join(self.slack)

# t = Editor()
# t.add("Vipul")
# t.add("Lahe")
# print(t.get_text())
# t.undo()
# t.add('Patil')
# print(t.get_text())


from collections import Counter, deque
import heapq

def taskScheduler(tasks, cooldown):
    freq = Counter(tasks)
    max_heap = [-cnt for cnt in freq.values()]
    heapq.heapify(max_heap)
    q = deque()  # (remaining, return_time)
    time = 0

    while max_heap or q:
        time += 1

        if max_heap:
            cnt = 1 + heapq.heappop(max_heap)
            if cnt != 0:
                q.append((cnt, time + cooldown))

        if q and q[0][1] == time:
            heapq.heappush(max_heap, q.popleft()[0])

    return time
