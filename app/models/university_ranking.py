from sqlalchemy import Column, Integer, Numeric, String
from app import db


class UniversityRanking(db.Model):
    __tablename__ = 'university_ranking'

    id = Column(Integer, primary_key=True)
    world_rank = Column(Integer)
    institution = Column(String)
    country = Column(String)
    national_rank = Column(Integer)
    quality_of_education = Column(Integer)
    alumni_employment = Column(Integer)
    quality_of_faculty = Column(Integer)
    publications = Column(Integer)
    influence = Column(Integer)
    citations = Column(Integer)
    broad_impact = Column(Integer)
    patents = Column(Integer)
    score = Column(Numeric)
    year = Column(Integer)

    def __iter__(self):
        yield 'id', self.id
        yield 'world_rank', self.world_rank
        yield 'institution', self.institution
        yield 'country', self.country
        yield 'national_rank', self.national_rank
        yield 'quality_of_education', self.quality_of_education
        yield 'alumni_employment', self.alumni_employment
        yield 'quality_of_faculty', self.quality_of_faculty
        yield 'publications', self.publications
        yield 'influence', self.influence
        yield 'citations', self.citations
        yield 'broad_impact', self.broad_impact
        yield 'patents', self.patents
        yield 'score', float(self.score)
        yield 'year', self.year
