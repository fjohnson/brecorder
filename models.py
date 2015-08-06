class Hops(Base):
    __tablename__ = 'hops'
    id = Column(Integer, Sequence('hops_id_seq'), primary_key=True)
    record_id = Column(Integer, ForeignKey('beer.id'))
    oz = Column(Float)
    name = Column(String)
    time = Column(Integer)
    type = Column(String)

    def __repr__(self):
        return str((self.id, self.record_id, self.name, self.oz))

class Fermentable(Base):
    __tablename__ = 'fermentable'
    id = Column(Integer, Sequence('fermentable_id_seq'), primary_key=True)
    name = Column(String)
    lbs = Column(Float)
    note = Column(String, nullable=True)

class Note(Base):
    __tablename__ = 'note'
    id = Column(Integer, Sequence('note_id_seq'), primary_key=True)
    text = Column(Text, nullable=False)
    date = Column(DateTime)

class OtherIngredient(Base):
    __tablename__ = 'otheringredient'
    id = Column(Integer, Sequence('oingredient_id_seq'), primary_key=True)
    name = Column(String)
    amount = Column(String)
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
    temperature = Column(Float, nullable=True)
    hops = relationship("Hops", order_by="hops.time")
    fermentable = relationship("Fermentable", order_by="fermentable.lbs")
    notes = relationship("Note", order_by="note.date")
    other_ingredients = relationship("OtherIngredient", order_by="name")


    def __repr__(self):
        return str((self.id,self.name))

