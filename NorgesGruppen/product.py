
class Product:

    def __init__(self, ng, search):
        self.ng = ng
        self.search = search
        self.json = self.ng.fetch_products(search)

    def get_content_type(self, index=0):
        return self.ng.fetch_products_hits(self.search)[index]["contentType"]

    def get_title(self, index=0):
        return self.ng.fetch_products_hits(self.search)[index]["title"]

    def get_description(self, index=0):
        return self.ng.fetch_products_hits(self.search)[index]["description"]

    def get_content_id(self, index=0):
        return self.ng.fetch_products_hits(self.search)[index]["contentId"]

    def get_content_image(self, index=0):
        return self.ng.fetch_products_hits(self.search)[index]["imageId"]

    def get_content_index(self, index=0):
        return self.ng.fetch_products_content(self.search, index)["_index"]

    def get_content_underscore_type(self, index=0):
        return self.ng.fetch_products_content(self.search, index)["_type"]

    def get_content_underscore_id(self, index=0):
        return self.ng.fetch_products_content(self.search, index)["_id"]

    def get_unit_weight(self, index=0):
        return self.ng.fetch_products_content_source(self.search, index)["unitWeight"]

    def get_shopping_list_group_name(self, index=0):
        return self.ng.fetch_products_content_source(self.search, index)["shoppingListGroupName"]

    def get_source_title(self, index=0):
        return self.ng.fetch_products_content_source(self.search, index)["title"]

    def get_category_name(self, index=0):
        return self.ng.fetch_products_content_source(self.search, index)["categoryName"]

    def get_price(self, index=0):
        return self.ng.fetch_products_content_source(self.search, index)["pricePerUnit"]

    def fetch_product_list(self, index=0):
        return self.ng.fetch_products(self.search)

    def fetch_hits(self, index=0):
        return self.json["hits"]