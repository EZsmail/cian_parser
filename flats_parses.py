from selenium_stealth import stealth
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


class Flats_URL:
    def __init__(self) -> None :
        self.driver = None

        
    async def setup_driver(self) -> webdriver:
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        options.add_argument("--headless")
        
        driver = webdriver.Chrome(options=options)
        stealth(
            driver,
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
            languages = ['en-US','en;q=0.9','ru-RU;q=0.8','ru;q=0.7'],
            vendor = "Google Inc.",
            platform = "macOS",
            webgl_vendor = "Intel Inc.",
            renderer = "Intel Iris OpenGL Engine",
            fix_hairline = False,
            run_on_insecure_origins = False
        )
        return driver        
    
    async def get_page(self, url) -> None:
        self.driver = await self.setup_driver()
        self.driver.get(url)
        
        
    async def get_html(self) -> str:
        try:
            return self.driver.page_source
        except Exception as _ex:
            print(_ex)
            
    async def find_urls(self, html: str) -> list:
        soup = BeautifulSoup(html, 'lxml')
        boxes = soup.find_all(class_='_93444fe79c--general--BCXJ4')
        urls = []
        metro = []
        for box in boxes:
            url = box.find(class_='_93444fe79c--link--eoxce').get('href')
            metro_ = box.find(class_='_93444fe79c--remoteness--q8IXp').text.split(' ')[-1].replace('пешком', 'Пешком').replace('транспорте', 'На транспорте ')
            urls.append(url)
            metro.append(metro_)
        return urls, metro

class Flats_Full_Info:
    def __init__(self):
        self.driver = None

        
    async def setup_driver(self) -> webdriver:
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        options.add_argument("--headless")
        
        driver = webdriver.Chrome(options=options)
        stealth(
            driver,
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
            languages = ['en-US','en;q=0.9','ru-RU;q=0.8','ru;q=0.7'],
            vendor = "Google Inc.",
            platform = "macOS",
            webgl_vendor = "Intel Inc.",
            renderer = "Intel Iris OpenGL Engine",
            fix_hairline = False,
            run_on_insecure_origins = False
        ) 
        return driver
    
    async def get_item_by_xpath(self, path) -> str:
        try:
            return self.driver.find_element(By.XPATH, path).text

        except Exception as ex:
            return None
        
    async def get_item_by_class(self, path) -> str:
        try:
            return self.driver.find_element(By.CLASS_NAME, path).text

        except Exception as ex:
            return None
        
    async def get_item_by_text(self, text) -> str:
        try:
            return self.driver.find_element(By.XPATH, f"//*[contains(text(), '{text}')]/following-sibling::*[1]").text

        except Exception as ex:
            return None
        
    async def get_page(self, url) -> None:
        self.driver = await self.setup_driver()
        self.driver.get(url)
        
    async def get_full_info(self) -> list:
        name = await self.get_item_by_xpath('//*[@id="frontend-offer-card"]/div[2]/div[2]/section/div/div/div[1]/h1')
        district_id = await self.get_item_by_xpath('//*[@id="frontend-offer-card"]/div[2]/div[2]/section/div/div/div[2]/address/div/div/a[2]')
        if await self.get_item_by_xpath('//*[@id="frontend-offer-card"]/div[2]/div[3]/div/div[1]/div[1]/div[4]/div/div[1]/span'):
            price = await self.get_item_by_xpath('//*[@id="frontend-offer-card"]/div[2]/div[3]/div/div[1]/div[1]/div[4]/div/div[1]/span')
        else:
            price = await self.get_item_by_xpath('//*[@id="frontend-offer-card"]/div[2]/div[3]/div/div[1]/div[1]/div[3]/div/div[1]/span')
        time_to_metro = await self.get_item_by_xpath('//*[@id="frontend-offer-card"]/div[2]/div[2]/section/div/div/div[2]/address/ul[1]/li[1]/span')
        nearest_metro = await self.get_item_by_xpath('//*[@id="frontend-offer-card"]/div[2]/div[2]/section/div/div/div[2]/address/ul[1]/li[1]/a')
        rub_m2 = await self.get_item_by_xpath('//*[@id="frontend-offer-card"]/div[2]/div[3]/div/div[1]/div[3]/div/div/div[1]/span[2]')
        main_square = await self.get_item_by_text('Общая площадь')
        live_square = await self.get_item_by_text('Жилая площадь')
        try:
            floor = (await self.get_item_by_text('Этаж')).split(' из ')[0]
            max_floor = (await self.get_item_by_text('Этаж')).split(' из ')[1]
        except Exception:
            floor = None
            max_floor = None
            
        if await self.get_item_by_text('Год сдачи'):
            house_ready_year = await self.get_item_by_text('Год сдачи')
        else:
            house_ready_year = await self.get_item_by_text('Год постройки')
            
        ready_or_not = await self.get_item_by_text('Дом')
        finishing = await self.get_item_by_text('Отделка')
        parking = await self.get_item_by_text('Парковка')
        ceiling_height= await self.get_item_by_text('Высота потолков')
        raiting = await self.get_item_by_xpath('//*[@id="frontend-offer-card"]/div[2]/div[3]/div/div[1]/div[1]/div[1]/div/div/span')
        return list((name, district_id, price, time_to_metro, nearest_metro, \
            rub_m2, main_square, live_square, floor, max_floor, house_ready_year, \
                ready_or_not, finishing, parking, ceiling_height, raiting))