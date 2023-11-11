from parser_cian.flats_parses import Flats_Full_Info, Flats_URL
from parser_cian.pagination import Pagination
from parser_cian.file_operation import save_to_csv
import asyncio


class Cian_Parser:
    
    def __init__(self, URL, PATH, boost=False):
        self.url = URL
        self.path = PATH
        self.boost = boost
        
    async def get_data(self) -> None:
        
        parser = Flats_URL()
        
        try:

            await parser.get_page(url=self.url)
        
            pagination = Pagination(parser)
            all_flats = []
            all_time_to_metro = []
            
            # u can add counter 
            k = 0
            while (await pagination.HasNextPage()) and k < 5:
                k += 1
                html = await parser.get_html()
                try:
                    flats_on_page = (await parser.find_urls(html))[0]
                    time_to_metro = (await parser.find_urls(html))[1]
                except Exception as ex:
                    print(ex)
                all_flats.extend(flats_on_page)
                all_time_to_metro.append(time_to_metro)
                await pagination.GoToTheNextPage()
            
            
            try:
                for i in range(1, len(all_time_to_metro)):
                    all_time_to_metro[0].update(all_time_to_metro[i])
                
                all_metro_list = all_time_to_metro[0]
            except Exception as ex_:
                print(ex_)
            
            print(len(all_flats))
            print(len(set(all_flats)))
            
            details_parser = Flats_Full_Info(self.boost)
            
            csv_data = []
            
            await details_parser.create_page()
            
            async def get_info(flat):
                metro_ = await details_parser.get_page(flat, metro=all_metro_list)
                return (*await details_parser.get_full_info(), metro_)

            tasks = [get_info(flat) for flat in set(all_flats)]
            csv_data = await asyncio.gather(*tasks)    

            await save_to_csv(self.path, csv_data, self.boost)

        except Exception as ex_:
            print(ex_) 
        finally:
            if parser.driver:
                parser.driver.close()
            