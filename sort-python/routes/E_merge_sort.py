"""
归并排序（Merge sort）是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。

作为一种典型的分而治之思想的算法应用，归并排序的实现由两种方法：

自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第 2 种方法）；
自下而上的迭代；

算法步骤

申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
设定两个指针，最初位置分别为两个已经排序序列的起始位置；
比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
重复步骤 3 直到某一指针达到序列尾；
将另一序列剩下的所有元素直接复制到合并序列尾
"""
from typing import List
from fastapi import APIRouter

router = APIRouter()


def merge(num_list, left, mid, right):
    print(left, mid+1, right+1)
    left_nums = num_list[left:mid+1]
    right_nums = num_list[mid+1:right+1]
    i = 0
    j = 0
    while i < len(left_nums) and j < len(right_nums):
        if left_nums[i] <= right_nums[j]:
            num_list[left] = left_nums[i]
            i += 1
        else:
            num_list[left] = right_nums[j]
            j += 1
        left += 1

    for n in (left_nums[i:] + right_nums[j:]):
        num_list[left] = n
        left += 1


@router.post("/bubble_sort1", tags=["归并排序 - 递归"])
def sort(num_list: List[int]) -> List:
    def merge_sort(left, right):
        if left >= right:
            return
        mid = int((left + right) / 2)
        merge_sort(left, mid)
        merge_sort(mid+1, right)
        merge(num_list, left, mid, right)

    merge_sort(0, len(num_list)-1)
    return num_list


@router.post("/bubble_sort2", tags=["归并排序 - 迭代"])
def sort2(num_list: List[int]) -> List:
    nums_len = len(num_list)
    i = 1
    while i < nums_len:
        for j in range(0, nums_len, 2 * i):
            right = min(j + 2 * i - 1, nums_len - 1)
            mid = j + i - 1
            merge(num_list, j, mid, right)
        i = 2 * i
    return num_list


print(sort([5, 4, 0, 3, 2, 1]))
print(sort2([5, 4, 0, 3, 2, 1]))
