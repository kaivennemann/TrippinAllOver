from bs4 import BeautifulSoup  # pip install beautifulsoup4
from selenium import webdriver  # pip install selenium webdriver-manager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import process_time

url = "https://www.hostelworld.com/pwa/wds/s?q=Madrid,%20Madrid,%20Spain&country=Spain&city=Madrid&type=city&id=117&from=2023-07-12&to=2023-07-15&guests=2&page=1"

# instantiate options
options = webdriver.ChromeOptions()

# run browser in headless mode
options.add_argument('--headless')

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=options)

t1_start = process_time()
driver.get(url)
t1_stop = process_time()

print("process time: " + str(t1_stop - t1_start))
html = driver.page_source

# this renders the JS code and stores all
# of the information in static HTML code.

# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find_all("strong", "current")
print(all_divs)
driver.close()
