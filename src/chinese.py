# -*- coding: utf-8 -*-

chinese_nums = {
    1: "一",
    2: "二",
    3: "三",
    4: "四",
    5: "五",
    6: "六",
    7: "七",
    8: "八",
    9: "九",
    10: "十",
    100: "百",
    1000: "千",
    10000: "万",
}


def generate(num: int) -> str:
    if num <= 0:
        raise ValueError("Need positive value")

    if num < 11:
        return chinese_nums[num]
    if num < 20:  # handle teens
        return "十" + chinese_nums[num - 10]
    if num < 100:
        return chinese_nums[num // 10] + "十" + chinese_nums[num % 10]
    if num < 1000:
        return (
            chinese_nums[num // 100]
            + "百"
            + chinese_nums[num // 10]
            + "十"
            + chinese_nums[num % 10]
        )
    if num < 10000:
        return (
            chinese_nums[num // 100]
            + "百"
            + chinese_nums[num // 10]
            + "十"
            + chinese_nums[num % 10]
        )
