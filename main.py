from sqlalchemy import create_engine, Date, Table, ForeignKey, Float, Integer, String, Column, MetaData

engine = create_engine('sqlite:///database.db')

conn = engine.connect()

meta = MetaData()

stations = Table(
    'stations', meta,
    Column('id', Integer, primary_key=True),
    Column('station', String, unique=True),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('elevation', Float),
    Column('name', String),
    Column('country', String),
    Column('state', String),

)

measure = Table(
    'measure', meta,
    Column('station', String, ForeignKey('stations.station')),
    Column('date', Date),
    Column('precip', Float),
    Column('tobs', Integer),
)

meta.create_all(engine)
