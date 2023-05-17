# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/16 16:03
@Author  : liyang
@File    : test_ocr2.py
@Software: PyCharm
"""
import easyocr


if __name__ == '__main__':
    print('-------')
    reader = easyocr.Reader(['ch_sim', 'en'], gpu=True)  # this needs to run only once to load the model into memory
    result = reader.readtext('1.jpg')
    # result = reader.readtext('2.jpg')
    print(result)
