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


@blueprint.route('/top<int:top>')
def top(top):
    years_query = UniversityRanking.query.distinct(UniversityRanking.year).all()
    years = [x.year for x in years_query]
    university_ranking = []
    for year in years:
        university_ranking = university_ranking + (UniversityRanking.query.filter_by(year=year).limit(top).all())
    return jsonify(data=[dict(x) for x in university_ranking])
