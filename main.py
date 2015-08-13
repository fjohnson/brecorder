import datetime
from database import engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import *
from werkzeug.utils import redirect

session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))
Base.metadata.create_all(engine)

from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()

@app.route('/')
def index():
    return redirect(url_for('test'))

@app.route('/test')
def test():

    br = BeerRecord(
        name = "Hogworts",
        og = 1.30,
        fg = 1.01,
        srm = 11.11,
        ibus = 40,
        abv = 2.83,
        boil_time = 60,
        batch_size = 2.5,
        yeast = "wlp002",
        date = datetime.datetime.now(),
        style = "English Bitter",
        efficiency = 70.0,
        mash_temperature = 158.0,
        mash_time = 60,
        fermentation_temperature = 24.3,
    )
    hops = [Hops(oz=1, name="Fuggles", time=60, type="Boil"),
            Hops(oz=1, name="Fuggles", time=30, type="Boil")]
    fermentables = [
        Fermentable(name="Munich", lbs=3),
        Fermentable(name="Maris Otter", lbs=3.5),
        Fermentable(name="Cane Sugar", lbs=1, note="Added after fermentation finished"),
        Fermentable(name="Fruit Puree", lbs=1, note="Added to secondary for 3 weeks @ 18C")
    ]
    other_ingredients = [
        OtherIngredient(name="Oak Chips", amount="1 oz", note="Done @ day 6 in primary then removed 2 weeks later."),
        OtherIngredient(name="Whirlfloc", amount="1 Tab", note="Flame out"),
        OtherIngredient(name="Yeast Nutrient", amount="2.5 Grams", note="Flame out")
    ]

    time_1 = datetime.datetime.now()
    time_2 = time_1 - datetime.timedelta(600)
    notes = [Note(text="""This beer was aged in secondary for a total of 2 weeks at 5C after a 2 week primary.
                  It has finished quite quite clear and bronze in color. Light hop taste with hints of sweetness from the
                  fruit. Brown sugar no different than normal cane sugar.""", date=time_1),
             Note(text="""Now even more mellow in flavour, and despite 1oz of CTZ at flame out, no hop character
              is descernable. Also, oak flavouring is only barely detectable.""", date=time_2)]

    images = [ImagesBeer(path="../static/beer.jpg", note="Here we have beer"),
              ImagesBeer(path="../static/beer.jpg", note="Here we have beer2")]
    videos = [VideosBeer(path="../static/foo.mp4", note="infoz"),
              VideosBeer(path="../static/foo.mp4", note="infoz")]

    br.hops = hops
    br.fermentables = fermentables
    br.notes = notes
    br.other_ingredients = other_ingredients
    br.images = images
    br.videos = videos

    session.add(br)
    session.commit()
    return redirect('record/1')

def compile_fermentables(fermentables):
    total_weight = 0.0
    for fermentable in fermentables:
        total_weight += fermentable.lbs

    fermentable_data = {}
    fermentable_data['total'] = total_weight
    fermentable_data['items'] = []

    for fermentable in fermentables:
        percent_of_bill = "{:.2f}".format(fermentable.lbs/total_weight)
        fermentable_data['items'].append((percent_of_bill, fermentable))

    fermentable_data['items'] = sorted(fermentable_data['items'], reverse=True)

    return fermentable_data
@app.route('/record/<id>')
def display_record(id):
    beer_record = session.query(BeerRecord).filter_by(id=id).first()

    if beer_record:
        fermentable_data = compile_fermentables(beer_record.fermentables)
        return render_template('beer.html', beer=beer_record, fermentables=fermentable_data)
    return internal_server_error(beer_record)

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
if __name__ == '__main__':
    app.run(debug=True)

#br = BeerRecord(name="test", og=1.033, fg=1.011, srm=11.1, ibus=40.0, abv=9.9, boil_time=60, batch_size=2.5, yeast='wlp002')
#hop1 = Hops(oz='.4', name='fuggles', time='60', type='boil')
# n1 = Note('asfd', datetime.datetime())
# session.add(n1)
# session.commit()
# print session.query(Note).filter_by(text='asfd').first()
# br.hops = [hop1]
# session.add(br)
# session.add(hop1)
# session.commit()
# print br.hops