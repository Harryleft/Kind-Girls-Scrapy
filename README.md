# Kind-Girls-Scrapy

Kind-Girls-Scrapy is a Python crawler designed to download images from the KindGirls website (https://www.kindgirls.com/).

## Prerequisites

- Python 3.12
- You need to install the necessary libraries by running the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
- Download Microsoft Edge WebDriver (default) and add the absolute path of the WebDriver file to the `config.py` file. You can download the WebDriver here:
```
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
```

## Usage

First, set the following parameters in the `config.py` file:

- `WEB_DRIVER_PATH`: Path to the WebDriver
- `START_GIRL_ID`: Starting image ID, example: `https://www.kindgirls.com/gallery.php?id=11576`
- `END_GIRL_ID`: Ending image ID, example: `https://www.kindgirls.com/gallery.php?id=11598`

Then, you can start the image scraping by running the `main.py` file:

```bash
python main.py
```

Images will be downloaded to the `images/images_2024` directory by default. You can customize the directory by modifying line 86 in the `web_driver_handler.py` file.

## Disclaimer

- This project is for learning and research purposes only. The author is not responsible for any consequences resulting from the use of this project.

## License

This project is licensed under the MIT License.
