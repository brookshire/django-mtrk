from amazon.api import AmazonAPI

import json

if __name__ == '__main__':
    cfp = open("/etc/amazon.json", 'r')
    config = json.load(cfp)
    cfp.close()

    access_key = config["access_key"]
    secret_key = config["secret_key"]
    associate_tag = config["associate_tag"]


    print(access_key)
    print(secret_key)
    print(associate_tag)
    amz = AmazonAPI(access_key,
                    secret_key,
                    associate_tag)

    # response = amz.item_search(host="us",
    #                        IdType="ISBN",
    #                        ItemId="883929115488",
    #                        ResponseGroup="ItemAttributes,Images")

    try:
        response = amz.lookup(ItemId="B00EOE0WKQ")
        print(response)
    except Exception as e:
        print(e.url)
