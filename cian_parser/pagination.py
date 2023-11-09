from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.by import By

class Pagination:
    def __init__(self, parser, next_button_selector) -> None:
        self.parser = parser
        self.next_button_selector = next_button_selector
        
    async def GoToTheNextPage(self) -> None:
        try:
            next_button = self.parser.driver.find_element(By.CSS_SELECTOR, self.next_button_selector)
            next_button.click()
        except Exception as ex_:
            print(ex_)
            
    async def HasNextPage(self) -> bool:
        try:
            self.parser.driver.find_element(By.CSS_SELECTOR, self.next_button_selector)
            return True
        except:
            return False
