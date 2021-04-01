"""
选择排序是一种简单直观的排序算法，无论什么数据进去都是 O(n²) 的时间复杂度
所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧

算法步骤

1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾
3. 重复第二步，直到所有元素均排序完毕
"""
from typing import List
from fastapi import APIRouter

router = APIRouter()

@router.post("/selection_sort", tags=["选择排序"])
def sort(num_list: List[int]) -> List:
    num_len = len(num_list)
    # 当前位置
    cur_i = 0

    while num_len > cur_i + 1:
        # 取后半部分最小值
        min_i = cur_i
        min_num = num_list[cur_i]
        for i in range(cur_i+1, num_len):
            if min_num > num_list[i]:
                min_num = num_list[i]
                min_i = i
        # 与 cur_i 互换位置
        if cur_i != min_i:
            num_list[min_i] = num_list[cur_i]
            num_list[cur_i] = min_num
        cur_i += 1

    return num_list
