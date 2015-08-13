from database import engine
from sqlalchemy import Sequence, Integer, Column, String, Float, ForeignKey, Text, DateTime, create_engine, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Hops(Base):
    __tablename__ = 'hops'
    id = Column(Integer, Sequence('hops_id_seq'), primary_key=True)
    record_id = Column(Integer, ForeignKey('beer.id'))
    oz = Column(Float)
    name = Column(String)
    time = Column(Integer)
    type_enums = Enum("Boil", "Dryhop", "FWH", "Flame Out")
    type = Column(type_enums)

    def __repr__(self):
        return str((self.id, self.record_id, self.name, self.oz))

class Fermentable(Base):
    __tablename__ = 'fermentable'
    id = Column(Integer, Sequence('fermentable_id_seq'), primary_key=True)
    record_id = Column(Integer, ForeignKey('beer.id'))
    name = Column(String)
    lbs = Column(Float)
    note = Column(String, nullable=True)

class Note(Base):
    __tablename__ = 'note'
    id = Column(Integer, Sequence('note_id_seq'), primary_key=True)
    record_id = Column(Integer, ForeignKey('beer.id'))
    text = Column(Text, nullable=False)
    date = Column(DateTime)

class OtherIngredient(Base):
    __tablename__ = 'otheringredient'
    id = Column(Integer, Sequence('oingredient_id_seq'), primary_key=True)
    record_id = Column(Integer, ForeignKey('beer.id'))
    name = Column(String)
    amount = Column(String)
    note = Column(Text)

class ImagesBeer(Base):
    __tablename__ = 'imagesbeer'
    id = Column(Integer, Sequence('imagebeer_id_seq'), primary_key=True)
    record_id = Column(Integer, ForeignKey('beer.id'))
    path = Column(String)
    note = Column(Text)

class VideosBeer(Base):
    __tablename__ = 'videosbeer'
    id = Column(Integer, Sequence('videosbeer_id_seq'), primary_key=True)
    record_id = Column(Integer, ForeignKey('beer.id'))
    path = Column(String)
    note = Column(Text)

class BeerRecord(Base):
    __tablename__ = 'beer'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    og = Column(Float, nullable=True)
    fg = Column(Float, nullable=True)
    srm = Column(Float, nullable=True)
    ibus = Column(Float, nullable=True)
    abv = Column(Float, nullable=True)
    boil_time = Column(Integer, nullable=True)
    batch_size = Column(Float, nullable=True)
    yeast = Column(String)
    date = Column(DateTime)
    style = Column(String, nullable=True)
    efficiency = Column(Float)
    mash_temperature = Column(Float, nullable=True)
    mash_time = Column(Float, nullable=True)
    fermentation_temperature = Column(Float, nullable=True)
    hops = relationship("Hops", order_by="Hops.time")
    fermentables = relationship("Fermentable", order_by="Fermentable.lbs")
    notes = relationship("Note", order_by="Note.date")
    other_ingredients = relationship("OtherIngredient", order_by="OtherIngredient.name")
    images = relationship("ImagesBeer", order_by="ImagesBeer.id")
    videos = relationship("VideosBeer", order_by="VideosBeer.id")

    def __repr__(self):
        return str((self.id,self.name))

class TestObj(Base):
    __tablename__ = 'testtable'
    id = Column(Integer, Sequence('testobj_id_seq'), primary_key=True)
    name = Column(String)