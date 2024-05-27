
King-Girls-Scrapy 是一个用于下载KindGirls网站(https://www.kindgirls.com/) 上图片的 Python 爬虫。

## 准备

- Python 3.12
- 你需要运行requirements.txt文件安装必要的库：
```
pip install requirements.txt
```
- 下载 Microsoft Edge WebDriver(默认使用)，并WebDriver文件的绝对路径添加到config.py文件中。你可以在这里下载 WebDriver：
```
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
```


## 使用

首先，你需要在 `config.py` 文件中设置以下参数：

- `WEB_DRIVER_PATH`：WebDriver 的路径
- `START_GIRL_ID`：开始的图片 ID
- `END_GIRL_ID`：结束的图片 ID
然后，你可以运行 `main.py` 文件来开始抓取图片：

```bash
python main.py
```

图片会默认下载到`images/images_2024` 目录下,可以在web_driver_handler.py文件中修改第86行代码，实现自定义目录


## 声明

- 本项目仅供学习和研究使用，作者不对任何因使用本项目而产生的后果负责。

## 许可证

本项目采用 MIT 许可证，详情请见 LICENSE 文件
