import csv
import json
import os


async def save_to_json(path: str, data: dict, page: int) -> None:
    try:
        async with open(path, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f'Страница {page} успешно сохранена в формате json')
    except Exception as _ex:
        print(f'Произошла ошибка {_ex}')
    
async def save_to_csv(path: str, data: list, boost: bool) -> None:
    if os.path.isfile(path):
        with open(path, 'a') as file:
            writer = csv.writer(file)
            for item in data:
                writer.writerow(item)
    else:
        with open(path, 'w') as file:
            writer = csv.writer(file)
            if boost:
                writer.writerow(
                    [
                        'name',
                        'distinct_id', 
                        'price',
                        'time_to_metro',
                        'nearest_metro', 
                        'price_per_square_meter',
                        'main_square', 
                        'live_square', 
                        'floor',
                        'total_square_footage', 
                        'house_ready_year',
                        'surrendered_or_not', 
                        'finishing', 
                        'parking', 
                        'ceiling_height', 
                        'builder_rating',
                        'how_to_get_to_the_subway'
                    ]
                )
                for item in data:
                    writer.writerow(item)
            else:
                writer.writerow(
                    [
                        'name',
                        'distinct_id', 
                        'price',
                        'time_to_metro',
                        'nearest_metro', 
                        'price_per_square_meter',
                        'main_square', 
                        'live_square', 
                        'floor',
                        'total_square_footage', 
                        'house_ready_year',
                        'surrendered_or_not', 
                        'finishing', 
                        'parking', 
                        'ceiling_height', 
                        'builder_rating',
                        'how_to_get_to_the_subway'
                    ]
                )
                for item in data:
                    writer.writerow(item)
            
            
    