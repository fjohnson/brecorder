from sqlalchemy import Sequence, Integer, Column, String, Float, create_engine, ForeignKey, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()

# br = BeerRecord(name="test", og=1.033, fg=1.011, srm=11.1, ibus=40.0, abv=9.9, boil_time=60, batch_size=2.5, yeast='wlp002')
# hop1 = Hops(oz='.4', name='fuggles', time='60', type='boil')
# br.hops = [hop1]
# session.add(br)
# session.add(hop1)
# session.commit()
# print br.hops
