from flask import jsonify, request, Blueprint
from ..crud.projects import register_project, get_user_projects

def init(app):
    bp = Blueprint('projects', __name__)

    @bp.route('/project', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            return register_project()
        else:
            # Aqui pegaremos o id do projeto via query params
            return função_que_pega_os_dados_pelo_id_do_projeto()
    
    @bp.route('/project/<int:id_project>/users', methods=['GET'])
    def get_users_from_project:
        # Aqui vamos usar URL params que é chamado lá no decorator com o template "tipo:nome_parametro"
        # e depois é só chamar lá embaixo passando como parâmetro na nossa função
        return função_que_pega_os_user_do_projeto(id_project)

    app.register_blueprint(bp, url_prefix="/api/v1")
