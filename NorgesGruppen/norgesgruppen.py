import json
import requests

"""
    This is an unofficial wrapper for NorgesGruppens' (unintentionally?) public API.
    There are multiple stores using this API and therefore it requires a store id.
#
    ID:
         1210 - Spar
         1220 - Joker
         1300 - Meny
#
    Initially written for non-commercial use, but licensed under MIT so feel free to do as you please.
"""


class NorgesGruppen:

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

    def fetch_products(self, search) -> dict:
        return self.fetch_json(search)["products"]

    def fetch_recipes(self, search) -> dict:
        return self.fetch_json(search)["recipes"]

    def fetch_stores(self, search) -> dict:
        return self.fetch_json(search)["stores"]

    def fetch_articles(self, search) -> dict:
        return self.fetch_json(search)["articles"]

    def fetch_products_hits(self, search) -> list:
        pretty = self.fetch_products(search)
        if pretty is not None:
            return pretty["hits"]

    def fetch_products_content(self, search, index) -> dict:
        return self.fetch_products_hits(search)[index]["contentData"]

    def fetch_products_content_source(self, search, index) -> dict:
        return self.fetch_products_hits(search)[index]["contentData"]["_source"]

    def fetch_json(self, search) -> dict:
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


class Product:

    def __init__(self, ng, search):
        self.ng = ng
        self.search = search
        self.json = self.ng.fetch_products(search)

    def get_content_type(self, index=0) -> str:
        return self.fetch_products_hits()[index]["contentType"]

    def get_title(self, index=0) -> str:
        return self.fetch_products_hits()[index]["title"]

    def get_description(self, index=0) -> str:
        return self.fetch_products_hits()[index]["description"]

    def get_content_id(self, index=0) -> str:
        return self.fetch_products_hits()[index]["contentId"]

    def get_content_image(self, index=0) -> str:
        return self.fetch_products_hits()[index]["imageId"]

    def get_content_index(self, index=0) -> str:
        return self.fetch_products_content(index)["_index"]

    def get_content_underscore_type(self, index=0) -> str:
        return self.fetch_products_content(index)["_type"]

    def get_content_underscore_id(self, index=0) -> str:
        return self.fetch_products_content(index)["_id"]

    def get_unit_weight(self, index=0) -> float:
        return self.ng.fetch_products_content_source(self.search, index)["unitWeight"]

    def get_shopping_list_group_name(self, index=0) -> str:
        return self.fetch_product_source(index)["shoppingListGroupName"]

    def get_source_title(self, index=0) -> str:
        return self.fetch_product_source(index)["title"]

    def get_category_name(self, index=0) -> str:
        return self.fetch_product_source(index)["categoryName"]

    def get_calc_unit(self, index=0) -> str:
        return self.fetch_product_source(index)["calcUnit"]

    def get_price(self, index=0) -> float:
        return self.fetch_product_source(index)["pricePerUnit"]

    def get_unit_type(self, index=0) -> str:
        return self.fetch_product_source(index)["unitType"]

    def get_age_limit(self, index=0) -> int:
        return self.fetch_product_source(index)["ageLimit"]

    def get_recycle_value(self, index=0) -> int:
        return self.fetch_product_source(index)["recycleValue"]

    def get_ean(self, index=0) -> str:
        return self.fetch_product_source(index)["ean"]

    def get_total_hits(self) -> int:
        return len(self.fetch_products_hits())

    def fetch_product_list(self):
        return self.ng.fetch_products(self.search)

    def fetch_product_content(self, index=0):
        return self.fetch_products_hits()[index]["contentData"]

    def fetch_product_source(self, index=0):
        return self.fetch_products_hits()[index]["contentData"]["_source"]

    def fetch_products_content(self, index):
        return self.fetch_products_hits()[index]["contentData"]

    def fetch_products_hits(self):
        return self.json["hits"]


