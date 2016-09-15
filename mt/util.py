import json
import sys

from amazon.api import AmazonAPI


class ProductInformation:
    title = None
    small_img = None
    medium_img = None
    large_img = None
    actors = None
    model = None
    author = None
    authors = None
    binding = None
    brand = None
    directors = None
    editorial_reviews = None
    genre = None
    features = None
    url = None
    list_price = None
    currency = None
    publication_date = None
    release_date = None
    sales_rank = None
    api_filled = False

    def __init__(self, sku):
        access_key, secret_key, associate_tag = get_config()
        self.sku = sku
        self.get_product_information()

    def __repr__(self):
        ret = "Unknown (%s)" % self.sku

        if self.title:
            ret = "%s (%s)" % (self.title, self.sku)

        # ret += " Field: [%s]" % self.foo

        return ret

    def get_product_information(self):
        access_key, secret_key, associate_tag = get_config()

        amz = AmazonAPI(access_key,
                        secret_key,
                        associate_tag)

        response = amz.lookup(IdType="UPC", ItemId="%s" % self.sku, SearchIndex="Electronics")

        if type(response) is list:
            # If more than one response was found, return the first.
            response = response[0]

        self.asin = response.asin
        self.actors = response.actors
        self.binding = response.binding
        self.brand = response.brand
        self.directors = response.directors
        self.editorial_reviews = response.editorial_reviews
        self.features = response.features
        self.genre = response.genre
        self.large_img = response.large_image_url
        self.medium_img = response.medium_image_url
        self.model = response.model
        self.publication_date = response.publication_date
        self.release_date = response.release_date
        self.sales_rank = response.sales_rank
        self.small_img = response.small_image_url
        self.title = response.title
        self.url = response.offer_url

        self.list_price, self.currency = response.list_price
        if self.list_price is None:
            self.list_price = 0.00

        if self.currency is None:
            self.currency = "USD"

        self.api_filled = True


def get_or_fix_reponse_value(response, pname):
    ret = None
    if response.__getattribute__(pname):
        ret = response.__getattribute__(pname)

    return ret


def get_config():
    cfp = open("/etc/amazon.json", 'r')
    config = json.load(cfp)
    cfp.close()

    access_key = config["access_key"]
    secret_key = config["secret_key"]
    associate_tag = config["associate_tag"]

    return (access_key, secret_key, associate_tag)


if __name__ == '__main__':
    p = ProductInformation("883929115488")
    print(p)
