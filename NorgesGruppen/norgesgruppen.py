import json
import requests


class NorgesGruppen():
    """
        This is an unofficial wrapper for NorgesGruppens' (unintentionally?) public API.
        There are multiple stores using this API and therefore it requires a store id.

        ID:
             1210 - Spar
             1220 - Joker
             1300 - Meny

        Initially written for non-commercial use, but licensed under MIT so feel free to do as you please.

    """

    id_dict_url = {
        1210: "https://spar.no/",
        1220: "https://joker.no/",
        1300: "https://meny.no/"
    }

    id_dict_param_id = {
        1210: "7080001266110",
        1220: "7080001420567",
        1300: "7080000886050"
    }

    def __init__(self, store_id=1210):
        if store_id in self.id_dict_url:
            self.store_id = store_id
            self.rest_url = "https://platform-rest-prod.ngdata.no/api/episearch/{}/autosuggest".format(self.store_id)
            self.session = requests.Session()
            self.token = None
            self.params = None
            self.headers = {'x-csrf-token': '0'}

    def fetch_products(self, search):
        return self.fetch_json(search)["products"]

    def fetch_recipes(self, search):
        return self.fetch_json(search)["recipes"]

    def fetch_stores(self, search):
        return self.fetch_json(search)["stores"]

    def fetch_articles(self, search):
        return self.fetch_json(search)["articles"]

    def fetch_products_hits(self, search):
        pretty = self.fetch_products(search)
        if pretty is not None:
            return pretty["hits"]

    def fetch_products_content(self, search, index):
        return self.fetch_products_hits(search)[index]["contentData"]

    def fetch_products_content_source(self, search, index):
        return self.fetch_products_hits(search)[index]["contentData"]["_source"]

    def fetch_json(self, search):
        self.refresh_token()
        self.set_params(search)
        r = self.session.get(self.rest_url, headers=self.headers, params=self.params)
        if r.status_code == 200:
            return json.loads(r.text)
        else:
            return None

    """
        Every request to the API needs a x-csrf-token, which is just a value of a cookie so its easy to fetch.
    """

    def refresh_token(self):
        self.session.get(self.id_dict_url[self.store_id])
        self.token = self.session.cookies.get_dict()["_app_token_"]
        self.headers = {'x-csrf-token': self.token}

    def set_params(self, search):
        self.params = (
            ('types', 'suggest,products,articles,recipes,stores'),
            ('search', search),
            ('page_size', '14'),
            ('store_id', self.id_dict_param_id[self.store_id]),
            ('popularity', 'true'),
        )
