import logging
import json
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, abort
from flask_caching import Cache
from ebay import ebay_get_html

logging.basicConfig(level=logging.INFO)

config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300,
}

app = Flask(__name__)
app.config.from_mapping(config)

cache = Cache(app)
api = Api(app)


class Ebay_parse(Resource):
    def url_proxy(self):
        if request.get_json():
            logging.info(f" JSON {request.json}")
            productid = request.json.get("productid")
            proxy = request.json.get("proxy")
            if not productid:
                abort(400, error="productid not found in JSON")
            return int(productid), proxy
        args = request.args
        if args.get("productid"):
            productid = args.get("productid")
        else:
            abort(400, error="ProductId not found in args")
        if args.get("proxy"):
            proxy = args.get("proxy")
        else:
            proxy = None
        return int(productid), proxy

    def get(self):
        productid, proxy = self.url_proxy()
        logging.info(f"Proxy {proxy} ")
        logging.info(f"ProductID = {productid}")
        response = ebay_get_html(productid, proxy)
        return response

    def post(self):
        productid, proxy = self.url_proxy()
        logging.info(f"Proxy {proxy} ")
        logging.info(f"ProductID = {productid}")
        response = ebay_get_html(productid, proxy)
        return response


api.add_resource(Ebay_parse, "/parser/ebay")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    
