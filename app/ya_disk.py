import os
import requests


class YaUploader:
    TOKEN = os.getenv('YA_TOKEN')
    URL = "https://cloud-api.yandex.net/v1/disk/resources"

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.TOKEN}'
                }

    def create_folder(self, folder_name):
        headers = self.get_headers()
        params = {'path': folder_name}
        response = requests.put(self.URL, headers=headers, params=params)
        return response.status_code

    def check_created_folder(self, folder_name):
        headers = self.get_headers()
        params = {'path': 'disk:/',
                  'fields': '_embedded.items.name, _embedded.items.type'}
        files_list = requests.get(
            self.URL, headers=headers, params=params
                                 ).json()['_embedded']['items']
        for file in files_list:
            if file['name'] == folder_name and file['type'] == 'dir':
                return True
        return False
