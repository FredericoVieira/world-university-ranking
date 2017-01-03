from flask_script import Command
from app.models.university_ranking import UniversityRanking
from load_university_ranking import LoadUniversityRanking


class LoadData(Command):

    "Loads data"

    def run(self):
        UniversityRanking.query.delete()
        LoadUniversityRanking().run()
