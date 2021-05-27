"""
快速排序

算法步骤

从数列中挑出一个元素，称为 “基准”（pivot）;
重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；

递归的最底部情形，是数列的大小是零或一，也就是永远都已经被排序好了。
虽然一直递归下去，但是这个算法总会退出，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。
"""
from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.post("/quick_sort", tags=["快速排序"])
def sort(num_list: List[int]) -> List:

    def quick_sort(left, right):
        if left >= right:
            return
        pivot = num_list[left]
        # 左右分片
        i = left + 1
        j = right
        while True:
            while True:
                if num_list[i] <= pivot and i != right:
                    i += 1
                else:
                    break
            while True:
                if num_list[j] > pivot and j != left:
                    j -= 1
                else:
                    break

            if i >= j:
                break

            num_list[i], num_list[j] = num_list[j], num_list[i]

        num_list[left], num_list[j] = num_list[j], num_list[left]

        quick_sort(left, j - 1)
        quick_sort(j + 1, right)

    quick_sort(0, len(num_list) - 1)

    return num_list
