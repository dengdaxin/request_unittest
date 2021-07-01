import requests


class BasePage:
    def __init__(self):
        self.session = requests.session()