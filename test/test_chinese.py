# -*- coding: utf-8 -*-

from chinese import generate


def test_generate():
    assert generate(3) == "三"
    assert generate(11) == "十一"
    assert generate(31) == "三十一"
    assert generate(59) == "五十九"
