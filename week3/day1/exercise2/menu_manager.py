import json


class MenuManager:
    def __init__(self):
        self.file_path = '../../restaurant-menu.json'
        with open(self.file_path) as f:
            self.menu = json.load(f)

    def add_item(self, name, price):
        self.menu['items'].append({
            'name': name,
            'price': price
        })

    def remove_item(self, name):
        for i, item in enumerate(self.menu['items']):
            if item['name'] == name:
                self.menu['items'].remove(item)
                return True
        else:
            return False

    def save_to_file(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.menu, f, indent=4)
