import random

# Path to the WebDriver executable. This is required for Selenium to interact with the browser.
# Please replace this with the path to your WebDriver executable.
# Default using Microsoft Edge WebDriver.
# Recommend use absolute path.
WEB_DRIVER_PATH = r'[Your WebDriver Path]'

# This is used to wait web page to loading.
DELAY = random.randint(1, 5)

# The start id of the first girl's photo that you want to download.
START_GIRL_ID = 11595

# The end id of the first girl's photo that you want to download.
END_GIRL_ID = 11599
