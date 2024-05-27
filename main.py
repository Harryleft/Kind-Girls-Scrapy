import time
from concurrent.futures import ThreadPoolExecutor
from config import START_GIRL_ID, END_GIRL_ID, DELAY
from web_driver_handler import WebDriverHandler

class KingGirlsImageScraper:
    """
    A class used to scrape images from the KindGirls website.

    Attributes:
        start_time (float): The time when the scraping starts.
    """
    def __init__(self):
        """
        Initializes the start time.
        """
        self.start_time = time.time()

    def download_girl_images(self, photo_id, dir_name='images'):
        """
        Downloads images of a specific girl identified by the photo ID.

        Args:
            photo_id (int): The ID of the photo to download.
            :param photo_id: girl's photo id
            :param dir_name: default "images" dictionary
         """
        wd = WebDriverHandler()
        start_url = f'https://www.kindgirls.com/gallery.php?id={photo_id}'
        wd.open_page(start_url)

        girl_name_element_a = wd.wait_for_element("#cuerpo > h2 > a")
        girl_name_element_b = wd.wait_for_element("#cuerpo > h2")

        girl_name = girl_name_element_a.text if girl_name_element_a and girl_name_element_a.text is not None else girl_name_element_b.text \
            if girl_name_element_b and girl_name_element_b.text is not None else None
        num = 3
        while True:
            image_element = wd.wait_for_element(f"#cuerpo > div:nth-child({num}) > a:nth-child(1) > img")
            if image_element is None:
                wd.driver.quit()
                break
            else:
                wd.download_images(f"#cuerpo > div:nth-child({num}) > a:nth-child(1) > img", photo_id, dir_name,
                                   girl_name)
                num += 1
        wd.driver.quit()

    def start_scraping(self):
        """
        Starts the scraping process using a ThreadPoolExecutor for concurrency.
        """
        with ThreadPoolExecutor(max_workers=5) as executor:
            photo_ids = range(START_GIRL_ID, END_GIRL_ID + 1)
            executor.map(self.download_girl_images, photo_ids)

    def run(self):
        """
        Runs the scraper and prints the total execution time.
        """
        self.start_scraping()
        end_time = time.time()
        print(">> Total consumed time：", (end_time - self.start_time)/60, "Minutes")


if __name__ == '__main__':
    # Creates an instance of the scraper and runs it.
    scraper = KingGirlsImageScraper()
    scraper.run()

