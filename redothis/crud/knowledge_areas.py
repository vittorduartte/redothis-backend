from flask import request, jsonify
from ..extensions.database import database as db
from ..models import KnowledgeArea, knowledgeArea_schema, knowledgeAreas_schema


def get_all_knowledge_areas():
    try:
        all_knowledge_areas = KnowledgeArea.query.order_by(KnowledgeArea.name).all()
        return jsonify({'message': 'success', 'data': knowledgeAreas_schema.dump(all_knowledge_areas)})
    except:
        return jsonify({'message': 'Erro', 'data': False})

def get_knowledge_area_by_id():
    area_id = request.json['area_id']

    area = KnowledgeArea.query.filter_by(id=area_id).first()

    if area:
        return jsonify({'message': 'success', 'data': knowledgeArea_schema.dump(area)}), 200
    else:
        return jsonify({'message': '_invalid_knowledge_area_id_', 'data': False}), 200
