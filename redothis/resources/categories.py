from flask import request, jsonify, Blueprint
from ..crud.category import register_category, get_all_categories, get_category_by_id
import os 

def init(app):
    bp = Blueprint('categories', __name__)

    @bp.route('/category', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            return register_category()
        else:
            return get_category_by_id()

    @bp.route('/categories', methods=['GET'])
    def get_categories():
        return get_all_categories()
    
    app.register_blueprint(bp, url_prefix="/api/v1")

    
