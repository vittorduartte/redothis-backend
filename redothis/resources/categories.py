from flask import request, jsonify, Blueprint
from ..crud.category import register_category, get_all_categories, get_category_by_id
import os 

def init(app):
    bp = Blueprint('categories', __name__)

    @bp.route('/register_category', methods=['POST'])
    def register():
        return register_category()

    @bp.route('/get_categories', methods=['GET'])
    def get_categories():
        return get_all_categories()

    @bp.route('/get_category', methods=['GET'])
    def get_category():
        return get_category_by_id()
    
    app.register_blueprint(bp, url_prefix="/api/v1")

    
