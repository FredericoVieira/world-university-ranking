from flask import Blueprint, jsonify
from app.models.university_ranking import UniversityRanking
from app import db


blueprint = Blueprint('pokemon_api', __name__, url_prefix='/api/university-ranking')


@blueprint.route('/')
def json():
    university_ranking = db.session.query(UniversityRanking).all()
    return jsonify(data=[dict(x) for x in university_ranking])
