def infinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1


chai = infinite_chai()
user2 = infinite_chai()

for ___ in range(5):
    print(next(chai))

# for ___ in range(4): # print after 5 to range
#     print(next(chai))

for __ in range(6):
    print(next(user2))
