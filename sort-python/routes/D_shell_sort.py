"""
希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。
希尔排序是非稳定排序算法。

希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。

算法步骤

选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；
按增量序列个数 k，对序列进行 k 趟排序；
每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。
仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
"""
from typing import List
from fastapi import APIRouter

router = APIRouter()

@router.post("/shell_sort", tags=["希尔排序"])
def sort(num_list: List[int]) -> List:
    num_len = len(num_list)
    gap = int(num_len / 2)

    while gap > 0:
        for cur_i in range(gap, num_len):
            # 取后半部分第一个
            cur_num = num_list[cur_i]

            # 遍历前半部分序列插入
            j = cur_i - gap
            while j >= 0 and num_list[j] > cur_num:
                num_list[j+gap] = num_list[j]
                j -= gap
            num_list[j+gap] = cur_num

        gap = int(gap / 2)

    return num_list
