#setup fastpip install fastapi[standard]==0.112.0

# setup alebic and sql alchemy
1 # setup 
pip install alembic

2 # init for migrations in root core
alembic init migrations

3 # setup connector in test -> alembic
# rdms = reational database  managment system
# sqlalchemy.url = driver://user:pass@localhost/dbname
# setup connector
sqlalchemy.url = sqlite:///./sqlite.db

4 # setup env 
# target_metadata = None
from models import Base
target_metadata = Base.metadata

5 # create model for track database make migrations
alembic revision --autogenerate -m "created model"

6 # migrate to database
alembic upgrade heads

7 # downgrade-reverse
alembic downgrade 'tag' or 00000000

