from flask import jsonify, request, g, url_for, current_app
from . import api

@api.route('/beers/')
def get_beers():
	beers = ["weyerbacher", "stella", "guiness"]
	return jsonify({'beers': beers})
