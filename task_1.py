
import heapq

def min_costs (cables):
    heapq.heapify (cables)
    cost = 0
    while len(cables) > 1:
        first = heapq.heappop (cables)
        second = heapq.heappop (cables)

        total = first + second
        cost += total

        heapq.heappush (cables, cost)

    return cost



cables = [10, 3, 25, 100]
print(f"Мінімальна вартість з'єднання кабелів: {min_costs(cables)}")
