import requests
import json
from bs4 import BeautifulSoup
import zipfile
import os


class CMSDataDownloader:
    def __init__(self):
        self.url = 'https://www.cms.gov/medicare/medicare-part-b-drug-average-sales-price/2023-asp-drug-pricing-files'
        self.response = requests.get(self.url)
        self.init_soup = BeautifulSoup(self.response.text, 'html.parser')
        self.date_modified = self.get_date_modified()
        self.data = self.get_data()
        self.file_urls = self.get_file_urls()
        self.date_changed = self.check_date_changed()

    def get_date_modified(self):
        # get the div with class = 'changed-date'
        div = self.init_soup.find('div', {'class': 'changed-date'})
        # get the date
        date_modified = div.find('div', {'class': 'field__item'}).text
        return date_modified

    def get_data(self):
        # open the data.json file
        with open('data.json', 'r') as f:
            data = json.load(f)
        return data

    def get_file_urls(self):
        # get the div with class 'field__items'
        field_ul = self.init_soup.find('ul', {'class': 'field__items'})

        # Define a dictionary to map the file names to their respective URLs and extract paths
        file_urls = {
            'asp-pricing': {
                'url': '',
                'extract_path': 'data/asp-pricing'
            },
            'noc-pricing': {
                'url': '',
                'extract_path': 'data/noc-pricing'
            },
            'asp-ndc-hcpcs': {
                'url': '',
                'extract_path': 'data/asp-ndc-hcpcs'
            }
        }

        # Loop through the li items until all the necessary files have been found
        for li in field_ul.find_all('li'):
            href = li.find('a')['href']
            for key in file_urls.keys():
                if key in href:
                    file_urls[key]['url'] = 'https://www.cms.gov' + href
                    break
            if all(val['url'] != '' for val in file_urls.values()):
                break
        return file_urls

    def check_date_changed(self):
        prev_date = self.data['date_modified']
        if prev_date:
            if prev_date != self.date_modified:
                print('Data has been updated')
                date_changed = True
                self.data['date_modified'] = self.date_modified
            else:
                print('Data has not been updated')
                date_changed = False
        else:
            print('Data has been updated')
            self.data['date_modified'] = self.date_modified
            date_changed = True
        return date_changed

    def write_data(self):
        # write the data back to the file
        with open('data.json', 'w') as f:
            json.dump(self.data, f)

    def download_files(self):
        # Download and extract the necessary files
        for key, value in self.file_urls.items():
            with requests.get(value['url']) as response:
                with open(key + '.zip', 'wb') as f:
                    f.write(response.content)
                with zipfile.ZipFile(key + '.zip', 'r') as zip_ref:
                    # remove the previous files
                    for file in os.listdir(value['extract_path']):
                        os.remove(os.path.join(value['extract_path'], file))
                    zip_ref.extractall(value['extract_path'])

    def run(self):
        if self.date_changed:
            self.download_files()
            self.write_data()
        else:
            print('No need to download files')


if __name__ == '__main__':
    downloader = CMSDataDownloader()
    downloader.run()
