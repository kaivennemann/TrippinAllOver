from bs4 import BeautifulSoup  # pip install beautifulsoup4
from selenium import webdriver  # pip install selenium webdriver-manager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime


class HostelWorldApi:

    @staticmethod
    def __setup_driver():
        # instantiate options
        options = webdriver.ChromeOptions()

        # run browser in headless mode
        options.add_argument('--headless')

        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=options)

        return driver

    @staticmethod
    def __process_information_card(card):
        """
        :param card: a soup object, div containing information for a single hostel
        :return: dictionary with keys: name, rating, price
        """
        print("card:")
        print(card.prettify())
        hostel_name = card.find("div", {"class": "property-name"}).get_text()

        return hostel_name

    def __init__(self):
        self.driver = self.__setup_driver()

    def get_details_from_(self, city, country, date1: datetime.date, date2: datetime.date, guests=1):
        print("getting details...")
        all_info_cards = self.__get_information_cards_from(city, country, date1, date2, guests)
        details = []
        for card in all_info_cards:
            info = self.__process_information_card(card)
            print(info)
            details.append(info)

        return details

    def __get_information_cards_from(self, city, country, date1: datetime.date, date2: datetime.date, guests):
        _from = date1.strftime("%Y-%m-%d")
        _to = date2.strftime("%Y-%m-%d")
        url = f"https://www.hostelworld.com/pwa/wds/s?q={city},%20{city},%20{country}&country={country}&city={city}" \
              f"&type=city&id=117&from={_from}&to={_to}&guests={guests}&page=1"

        self.driver.get(url)

        html = self.driver.page_source

        soup = BeautifulSoup(html, "html.parser")

        # div with information for each hostel has class property-info-container
        all_info_cards = soup.find_all("div", "property-info-container")

        return all_info_cards

