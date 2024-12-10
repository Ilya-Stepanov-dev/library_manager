import os
import json

class DataHelper:    
    def _create_directory(self, path: str) -> None:
        os.makedirs(path)

    def _create_file_json(self, path: str) -> None:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump([], file)
        
    def check_data_storage(self, path_data: str) -> bool:
        return all((os.path.exists(os.path.dirname(path_data)), os.path.exists(path_data)))

    def create_data_storage_json(self, path_data: str) -> None:
        directory = os.path.dirname(path_data)
        try:
            self._create_directory(directory)
        except FileExistsError:
            if not os.path.exists(path_data):
                self._create_file_json(path_data)


    def save_data_json(self, path: str, data: dict | list[dict]) -> None:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    def load_data_json(self, path: str) -> list:
        try: 
            with open(path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

data_helper = DataHelper()
