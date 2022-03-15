from sys import getsizeof, version
from typing import Collection
from MyQR import myqr
import os
# 一般黑白QR Code
myqr.run (
    words = "https://www.google.com.tw/?hl=zh_TW",
    level = "H",
    colorized = False,
    save_name = '黑白qrcode.jpg',
)

# 藝術QR (中間是圖片)
myqr.run(
    words = "https://www.google.com.tw/?hl=zh_TW",
    picture = "放置的圖片",
    version = 20,
    level = "H",
    colorized = True,
    save_name = '彩色qrcode.png'
)