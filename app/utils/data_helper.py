import os
import json

class DataHelper:
    
    def check_directory(self, path: str) -> bool:
        return bool(os.path.exists(os.path.dirname(path)))
    
    def check_file(self, path: str) -> bool:
        return bool(os.path.exists(path))
    
    def create_directory(self, path: str) -> None:
        os.makedirs(path)

    def create_file_json(self, path: str) -> None:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump([], file)
            # pass
    def check_data_storage(self, path_data: str, file_name: str) -> None:
        if not self.check_directory(path_data):
            self.create_directory(path_data)
        if not self.check_file(f'{path_data}{file_name}'):
            self.create_file_json(f'{path_data}{file_name}')

data_helper = DataHelper()
