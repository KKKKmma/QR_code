# QR_code
> Simple to create your QR_code

製作屬於自己的QR Code，可以節省輸入網址的時間，方便用於自我介紹或是推廣相關網站。

## 環境要求
1. Python
2. MyQR
<https://pypi.org/project/MyQR/>


## 參數
```
Positional parameter
   words: str

Optional parameters
   version: int, from 1 to 40
   level: str, just one of ('L','M','Q','H')
   picutre: str, a filename of a image
   colorized: bool
   constrast: float
   brightness: float
   save_name: str, the output filename like 'example.png'
   save_dir: str, the output directory
```

### Positional parameter：必須放入的參數
* words：必須為字串形式！內容為要打開頁面的網址

### Optional parameters：可選用是否放入
* version：數值越大，會越難讀取
* level：控制糾錯水平，範圍是L、M、Q、H，從左到右依次升高
* colorized：是否為彩色（默認黑白）
* constrast：對比度
* brightness：亮度
* picture：讀取圖片（使用絕對路徑）為了製作QR code底圖，僅能是’.jpg’, ‘.png’, ‘.bmp’, ‘.gif’幾種檔案類型
* save_name：只能是’.jpg’, ‘.png’, ‘.bmp’, ‘.gif’幾種檔案類型
* save_dir：存取位置
