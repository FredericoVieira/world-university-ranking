from flask import Blueprint, jsonify
from app.models.university_ranking import UniversityRanking


blueprint = Blueprint('university_ranking_api', __name__, url_prefix='/api/university-ranking')


@blueprint.route('/')
def all():
    university_ranking = UniversityRanking.query.all()
    return jsonify(data=[dict(x) for x in university_ranking])


@blueprint.route('/<int:year>')
def year(year):
    university_ranking = UniversityRanking.query.filter_by(year=year).all()
    return jsonify(data=[dict(x) for x in university_ranking])
