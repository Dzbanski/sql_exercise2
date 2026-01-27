
import csv
from datetime import datetime
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

with open("clean_stations.csv", newline="",) as stations_file:
    read = csv.DictReader(stations_file)

    row_station = list(read)

    conn.execute(stations.insert(), row_station)

with open("clean_measure.csv", newline="",) as measure_file:
    read = csv.DictReader(measure_file)

    rows = [] 

    for row_measure in read:
        row_measure["date"] = datetime.strptime(row_measure["date"], "%Y-%m-%d").date()
        rows.append(row_measure)

    conn.execute(measure.insert(), rows)

"""

TESTY 

s = measure.select().where(measure.c.station=="USC00519397")
result = conn.execute(s)

for j in result:
    print(j)

m = stations.insert().values(station="notak", latitude='21.424', longitude='-158.3234', elevation='2.0', name='Stacja', country='US', state='BR')
conn.execute(m)
d = stations.select().where(stations.c.station=="notak")
result3 = conn.execute(d)

for i in result3:
    print(i)

measure.drop(engine)

"""



conn.close()