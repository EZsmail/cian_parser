from cian_parser.flats_parses import Flats_Full_Info, Flats_URL
from cian_parser.pagination import Pagination
from cian_parser.file_operation import save_to_csv
import asyncio


class Cian_Parser:
    
    def __init__(self, URL, PATH):
        self.url = URL
        self.path = PATH
        
    async def get_data(self) -> None:
        
        parser = Flats_URL()
        
        try:
            await parser.get_page(url=self.url)
        
            pagination = Pagination(parser, next_button_selector='#frontend-serp > div > div._93444fe79c--pagination-section--DBmk6 > div._93444fe79c--pagination--UX22n > nav > a')
            all_flats = []
            all_time_to_metro = []
            
            # u can add counter 
            k = 0
            while await pagination.HasNextPage() and k < 5:
                k += 1
                html = await parser.get_html()
                flats_on_page = (await parser.find_urls(html))[0]
                time_to_metro = (await parser.find_urls(html))[1]
                all_flats.extend(flats_on_page)
                all_time_to_metro.extend(time_to_metro)
                await pagination.GoToTheNextPage()
                
                
            details_parser = Flats_Full_Info()
            detailed_flats = []
            
            for flat in all_flats:
                await details_parser.get_page(flat)
                await save_to_csv(self.path, (* await details_parser.get_full_info(), all_time_to_metro[k]))
            
        except Exception as ex_:
            print(ex_) 
        finally:
            if parser.driver:
                parser.driver.close()
                
        
if __name__ == '__main__':
    
    import tracemalloc
    
    tracemalloc.start()
    
    URL = 'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=1&region=1&room2=1'
    PATH = 'data/flats_info.csv'
    
    parser = Cian_Parser(URL=URL, PATH=PATH)
    asyncio.run(parser.scrape_flats_details())
        
            