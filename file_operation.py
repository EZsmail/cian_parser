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
    
async def save_to_csv(path: str, data: list) -> None:
    if os.path.isfile(path):
        with open(path, 'a') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    else:
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    'name',
                    'distinct_id', 
                    'price',
                    'time_to_metro',
                    'nearest_metro', 
                    'rub_to_m2',
                    'main_square', 
                    'live_square', 
                    'floor',
                    'max_floor', 
                    'house_ready_year',
                    'house_full_ready_year', 
                    'ready_or_not', 
                    'finishing', 
                    'parking', 
                    'ceiling_height', 
                    'raiting',
                    'car_or_on_foot'
                ]
            )
            writer.writerow(data)
            
    