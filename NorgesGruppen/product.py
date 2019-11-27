class Product:

    def __init__(self, ng, search):
        self.ng = ng
        self.search = search
        self.json = self.ng.fetch_products(search)

    def get_content_type(self, index=0):
        return self.fetch_products_hits()[index]["contentType"]

    def get_title(self, index=0):
        return self.fetch_products_hits()[index]["title"]

    def get_description(self, index=0):
        return self.fetch_products_hits()[index]["description"]

    def get_content_id(self, index=0):
        return self.fetch_products_hits()[index]["contentId"]

    def get_content_image(self, index=0):
        return self.fetch_products_hits()[index]["imageId"]

    def get_content_index(self, index=0):
        return self.fetch_products_content(index)["_index"]

    def get_content_underscore_type(self, index=0):
        return self.fetch_products_content(index)["_type"]

    def get_content_underscore_id(self, index=0):
        return self.fetch_products_content(index)["_id"]

    def get_unit_weight(self, index=0):
        return self.ng.fetch_products_content_source(self.search, index)["unitWeight"]

    def get_shopping_list_group_name(self, index=0):
        return self.fetch_product_source(index)["shoppingListGroupName"]

    def get_source_title(self, index=0):
        return self.fetch_product_source(index)["title"]

    def get_category_name(self, index=0):
        return self.fetch_product_source(index)["categoryName"]

    def get_calc_unit(self, index=0):
        return self.fetch_product_source(index)["calcUnit"]

    def get_price(self, index=0):
        return self.fetch_product_source(index)["pricePerUnit"]

    def get_unit_type(self, index=0):
        return self.fetch_product_source(index)["unitType"]

    def get_age_limit(self, index=0):
        return self.fetch_product_source(index)["ageLimit"]

    def get_recycle_value(self, index=0):
        return self.fetch_product_source(index)["recycleValue"]

    def get_ean(self, index=0):
        return self.fetch_product_source(index)["ean"]

    def get_total_hits(self):
        return enumerate(self.fetch_products_hits())

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
