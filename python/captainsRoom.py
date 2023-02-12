k, orders = int(input()), list(map(int, input().split()))
rooms = set(orders)

large_sum = sum(rooms)*k

small_sum = sum(orders)

print((large_sum - small_sum)//(k-1))