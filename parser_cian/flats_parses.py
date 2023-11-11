from selenium_stealth import stealth
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
        urls: list = []
        list_metro: dict = {}
        for box in boxes:
            try:
                url = box.find(class_='_93444fe79c--link--eoxce').get('href')
                metro_ = box.find(class_='_93444fe79c--remoteness--q8IXp').text.split(' ')[-1].replace('транспорте', 'На транспорте').replace('пешком', 'Пешком')
                urls.append(url)
                list_metro[url] = metro_
            except Exception as ex_:
                print(ex_)
        return set(urls), list_metro 

class Flats_Full_Info:
    def __init__(self, boost):
        self.driver = None
        self.boost = boost

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
        
    async def create_page(self) -> None:
        self.driver = await self.setup_driver()
        
    async def get_page(self, url: str, metro) -> None:
        self.driver.get(url)
        metro_ = metro[url]
        if self.boost:
            target_element = self.driver.find_element(By.XPATH, '//*[@id="frontend-offer-card"]/div[2]/div[2]/div[5]/div')
            actions = ActionChains(self.driver)
            actions.move_to_element(target_element).perform()
        return metro_
        
    async def get_full_info(self) -> list:
        try:    
            name = await self.get_item_by_xpath('//*[@id="frontend-offer-card"]/div[2]/div[2]/section/div/div/div[1]/h1')
        except Exception as e:
            pass
            
        try:
            district_id = await self.get_item_by_xpath('//*[@id="frontend-offer-card"]/div[2]/div[2]/section/div/div/div[2]/address/div/div/a[2]')
        except Exception as e:
            pass
        
        try:
            if await self.get_item_by_xpath('//*[@id="frontend-offer-card"]/div[2]/div[3]/div/div[1]/div[1]/div[4]/div/div[1]/span'):
                price = int((await self.get_item_by_xpath('//*[@id="frontend-offer-card"]/div[2]/div[3]/div/div[1]/div[1]/div[4]/div/div[1]/span')).replace(' ₽', '').replace(' ', ''))
            else:
                price = int((await self.get_item_by_xpath('//*[@id="frontend-offer-card"]/div[2]/div[3]/div/div[1]/div[1]/div[3]/div/div[1]/span')).replace(' ₽', '').replace(' ', ''))
        except Exception as e:
            price = None
        
        try:
            time_to_metro = int((await self.get_item_by_xpath('//*[@id="frontend-offer-card"]/div[2]/div[2]/section/div/div/div[2]/address/ul[1]/li[1]/span')).split(' ')[0])
        except Exception as e:
            time_to_metro = None
        
        try:
            nearest_metro = await self.get_item_by_xpath('//*[@id="frontend-offer-card"]/div[2]/div[2]/section/div/div/div[2]/address/ul[1]/li[1]/a')
        except Exception as e:
            nearest_metro = None
        
        try:
            rub_m2 = int((await self.get_item_by_xpath('//*[@id="frontend-offer-card"]/div[2]/div[3]/div/div[1]/div[3]/div/div/div[1]/span[2]')).replace(' ₽/м²', '').replace(' ', ''))
        except Exception as e:
            rub_m2 = None
        
        try:
            main_square = float((await self.get_item_by_text('Общая площадь')).split(' ')[0].replace(',', '.'))
        except Exception as e:
            main_square = None
        
        try:
            live_square = float((await self.get_item_by_text('Жилая площадь')).split(' ')[0].replace(',', '.'))
        except Exception as e:
            live_square = None
        
        try:
            floor = (await self.get_item_by_text('Этаж')).split(' из ')[0]
            max_floor = (await self.get_item_by_text('Этаж')).split(' из ')[1]
        except Exception:
            floor = None
            max_floor = None
            
        if await self.get_item_by_text('Год сдачи'):
            try:
                house_ready_year = await self.get_item_by_text('Год сдачи')
            except Exception as e:
                house_ready_year = None
        else:
            try:
                house_ready_year = await self.get_item_by_text('Год постройки')
            except Exception as e:
                house_ready_year = None
            
        try:
            ready_or_not = await self.get_item_by_text('Дом')
        except Exception as e:
            ready_or_not = None
        
        try:
            finishing = await self.get_item_by_text('Отделка')
        except Exception as e:
            finishing = None
        
        try:
            parking = await self.get_item_by_text('Парковка')
        except Exception as e:
            parking = None
        
        try:
            ceiling_height= float((await self.get_item_by_text('Высота потолков')).split(' ')[0].replace(',', '.'))
        except Exception as e:
            ceiling_height = None
        
        if self.boost:
            
            try:
                raiting = await self.get_item_by_xpath('//*[@id="frontend-offer-card"]/div[2]/div[3]/div/div[1]/div[1]/div[1]/div/div/span')
                return list((name, district_id, price, time_to_metro, nearest_metro, \
                    rub_m2, main_square, live_square, floor, max_floor, house_ready_year, \
                        ready_or_not, finishing, parking, ceiling_height, raiting))
            except Exception as e:
                raiting = None
                return list((name, district_id, price, time_to_metro, nearest_metro, \
                    rub_m2, main_square, live_square, floor, max_floor, house_ready_year, \
                        ready_or_not, finishing, parking, ceiling_height, raiting))
        else:
            return list((name, district_id, price, time_to_metro, nearest_metro, \
                rub_m2, main_square, live_square, floor, max_floor, house_ready_year, \
                    ready_or_not, finishing, parking, ceiling_height))