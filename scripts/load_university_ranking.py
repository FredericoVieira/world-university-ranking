import pandas
import math
from flask_script import Command
from app.models.university_ranking import UniversityRanking
from app import db


class LoadUniversityRanking(Command):

    "Loads World University Ranking"

    def run(self):
        data_frame = pandas.read_csv('data/world-univertisy-ranking.csv')

        for index, row in data_frame.iterrows():
            university_ranking = UniversityRanking()
            university_ranking.world_rank = row['world_rank']
            university_ranking.institution = row['institution']
            university_ranking.country = row['country']
            university_ranking.national_rank = row['national_rank']
            university_ranking.quality_of_education = row['quality_of_education']
            university_ranking.alumni_employment = row['alumni_employment'] if not math.isnan(row['alumni_employment']) else None
            university_ranking.quality_of_faculty = row['quality_of_faculty']
            university_ranking.publications = row['publications']
            university_ranking.influence = row['influence']
            university_ranking.citations = row['citations']
            university_ranking.broad_impact = row['broad_impact'] if not math.isnan(row['broad_impact']) else None
            university_ranking.patents = row['patents']
            university_ranking.score = row['score']
            university_ranking.year = row['year']

            db.session.add(university_ranking)

        db.session.commit()
