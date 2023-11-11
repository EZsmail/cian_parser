from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import asyncio 

class Pagination:
    def __init__(self, parser) -> None:
        self.parser = parser
        # self.next_button_selector = next_button_selector
        
    async def GoToTheNextPage(self) -> None:
        try:
            self.parser.driver.find_element(By.XPATH, '//*[@id="header-frontend"]/div[1]/div[2]/button').click()
        except Exception as _:
            print(_)
            
        try:
            await asyncio.sleep(5)
            
            try:
                next_button = self.parser.driver.find_element(By.XPATH, '//*[@id="frontend-serp"]/div/div[5]/div[1]/nav/a[2]')
                next_button.click()
            except Exception as _:
                next_button = self.parser.driver.find_element(By.XPATH, '//*[@id="frontend-serp"]/div/div[5]/div[1]/nav/a')
                next_button.click()

        except Exception as _:
            pass
            
    async def HasNextPage(self) -> bool:
        try:
            self.parser.driver.implicitly_wait(2)
            self.parser.driver.find_element(By.XPATH, '//*[@id="frontend-serp"]/div/div[5]/div[1]/nav/a[2]')
            return True
        except Exception as _:
            try:
                self.parser.driver.find_element(By.XPATH, '//*[@id="frontend-serp"]/div/div[5]/div[1]/nav/a')
                return True
            except Exception as _:
                return False
