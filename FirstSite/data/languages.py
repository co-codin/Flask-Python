from datetime import datetime
import sqlalchemy as sa
from data.modelbase import SqlAlchemyBase

class ProgrammingLanguage(SqlAlchemyBase):
    __tablename__ = 'languages'

    id = sa.Column(sa.String, primary_key=True)
    created_date = sa.Column(sa.DateTime, default=datetime.now, index=True)
    description = sa.Column(sa.String)