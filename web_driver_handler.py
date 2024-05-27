import os
import requests
from requests.adapters import HTTPAdapter
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib3 import Retry
from config import *


class WebDriverHandler:
    """
    A class used to interact with the browser using Selenium WebDriver.

    Attributes:
        options (Options): A set of desired capabilities for the WebDriver.
        driver (WebDriver): The WebDriver instance.
        image_count (int): A counter for the downloaded images.
    """
    def __init__(self):
        """
        Initializes WebDriver and related parameters.

        Others:
            If you want to use other Browser, please replace the WebDriver path of the config.py.
            Chrome WebDriver:
                self.driver = webdriver.Chrome(service=webdriver.ChromeService(executable_path=WEB_DRIVER_PATH), options=self.options)
            Firefox WebDriver:
                self.driver = webdriver.Firefox(service=webdriver.FirefoxService(executable_path=WEB_DRIVER_PATH), options=self.options)
        """
        self.options = Options()
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument('--headless')
        self.driver = webdriver.Edge(service=webdriver.EdgeService(executable_path=WEB_DRIVER_PATH),
                                     options=self.options)
        self.image_count = 1

    def open_page(self, start_url):
        """
        Opens a webpage.

        Args:
            start_url (str): The URL of the webpage to open.
        """
        self.driver.get(start_url)

    def wait_for_element(self, selector):
        """
        Waits for an element to load.

        Args:
            selector (str): The CSS selector of the element to wait for.

        Returns:
            element (selenium.webdriver.remote.webelement.WebElement): The loaded element.
            None if the element does not load within the delay time.
        """
        try:
            element = WebDriverWait(self.driver, DELAY).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            return element
        except TimeoutException:
            return None

    def download_images(self, selector, photo_id, dir_name, girl_name):
        """
        Downloads images.

        Args:
            selector (str): The CSS selector of the images to download.
            photo_id (int): The ID of the photo to download.
            :param girl_name:
            :param photo_id:
            :param selector:
            :param dir_name: default "images" dictionary, you can add second dictionary to save images,
                such as images_2024

        Returns:
            None

        """
        download_dir = os.path.join(f"{dir_name}/images_2024", girl_name)

        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        img_url = self.wait_for_element(selector).get_attribute("src")

        session = requests.Session()
        retry = Retry(
            total=5,  # Total retry attempts
            read=5,  # Retry attempts for reading
            connect=5,  # Retry attempts for connecting
            backoff_factor=10,  # Delay time for each retry
            status_forcelist=(500, 502, 504) # HTTP error codes to retry
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('https://', adapter)
        response = session.get(img_url, timeout=5)

        # Download the image
        with open(os.path.join(download_dir, f"{girl_name}_{photo_id}_{self.image_count}.jpg"), "wb") as f:
            f.write(response.content)
        print(f">> Image downloaded: {girl_name}: {photo_id}: {self.image_count}")
        self.image_count += 1
