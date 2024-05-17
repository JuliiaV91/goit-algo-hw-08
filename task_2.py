
import heapq

def merge_k_lists (lists):
    merged = heapq.merge (*lists)
    return list (merged)

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
