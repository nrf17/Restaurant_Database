from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request
import json

from BarBeerDrinkerPlus import database

app = Flask(__name__)

@app.route('/api/bar', methods=["GET"])
def get_bars():
    try:
        return jsonify(database.get_bars())
    except Exception as e:
        return make_response(str(e), 500)


@app.route("/api/bar/<name>", methods = ["GET"])
def find_bar(name):
    try:
        if name is None:
            raise ValueError("Bar is not specified.")
        bar = database.find_bar(name)
        if bar is None:
            return make_response("No bar found with given name", 404)
        return jsonify(bar)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/larspender/<name>", methods = ["GET"])
def bar_larspender(name):
    try:
        if name is None:
            raise ValueError("Bar is not specified.")
        bar = database.bar_larspenders(name)
        if bar is None:
            return make_response("No bar found with given name", 404)
        return jsonify(bar)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/toptenbrand/<name>", methods = ["GET"])
def bar_toptenbrand(name):
    try:
        if name is None:
            raise ValueError("Bar is not specified.")
        bar = database.bar_toptenbrand(name)
        if bar is None:
            return make_response("No bar found with given name", 404)
        return jsonify(bar)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/timedistr/<name>", methods = ["GET"])
def bar_timedistr(name):
    try:
        if name is None:
            raise ValueError("Bar is not specified.")
        bar = database.bar_timedistr(name)
        if bar is None:
            return make_response("No bar found with given name", 404)
        return jsonify(bar)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/busiestdays/<name>", methods = ["GET"])
def bar_busiestdays(name):
    try:
        if name is None:
            raise ValueError("Bar is not specified.")
        bar = database.bar_busiestdays(name)
        if bar is None:
            return make_response("No bar found with given name", 404)
        return jsonify(bar)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)


@app.route("/api/fractionsold/<name>", methods = ["GET"])
def bar_fractionsold(name):
    try:
        if name is None:
            raise ValueError("Bar is not specified.")
        bar = database.bar_fractionsold(name)
        if bar is None:
            return make_response("No bar found with given name", 404)
        return jsonify(bar)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)


@app.route('/api/beer', methods=["GET"])
def get_beers():
    try:
        return jsonify(database.get_beers())
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/beer/<name>', methods=["GET"])
def get_beer(name):
    try:
        if name is None:
            raise ValueError("Beer is not specified.")
        return jsonify(database.beers_top_ten(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/consume/<name>', methods=["GET"])
def get_consumers(name):
    try:
        if name is None:
            raise ValueError("Beer is not specified.")
        return jsonify(database.beers_consumer(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)


@app.route('/api/time/<name>', methods=["GET"])
def get_times(name):
    try:
        if name is None:
            raise ValueError("Beer is not specified.")
        return jsonify(database.beers_time(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)


@app.route('/api/drinker', methods=["GET"])
def get_drinkers():
    try:
        return jsonify(database.get_drinkers())
    except Exception as e:
        return make_response(str(e), 500)


@app.route('/api/drinker/<name>', methods=["GET"])
def find_drinker(name):
    try:
        if name is None:
            raise ValueError("Drinker is not specified.")
        return jsonify(database.find_drinker_info(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/transaction/<name>', methods=["GET"])
def drinker_trans(name):
    try:
        if name is None:
            raise ValueError("Drinker is not specified.")
        return jsonify(database.find_drinker_trans(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/drinkergraph1/<name>', methods=["GET"])
def drinker_graph1(name):
    try:
        if name is None:
            raise ValueError("Drinker is not specified.")
        return jsonify(database.get_drinker_graph1(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/drinkergraph2/<name>', methods=["GET"])
def drinker_graph2(name):
    try:
        if name is None:
            raise ValueError("Drinker is not specified.")
        return jsonify(database.get_drinker_graph2(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)


@app.route('/api/bartender', methods=["GET"])
def get_bartenders():
    try:
        return jsonify(database.get_bartenders())
    except Exception as e:
        return make_response(str(e), 500)



@app.route('/api/manufacturers', methods=["GET"])
def get_manufacturers():
    try:
        return jsonify(database.get_manufacturers())
    except Exception as e:
        return make_response(str(e), 500)


@app.route('/api/manufacturers/<name>', methods=["GET"])
def manuf_high_sales(name):
    try:
        if name is None:
            raise ValueError("Manufacturer is not specified.")
        return jsonify(database.manuf_high_sales(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)


@app.route('/api/manufacturers/<name>/likes', methods=["GET"])
def manuf_likes(name):
    try:
        if name is None:
            raise ValueError("Manufacturer is not specified.")
        return jsonify(database.manuf_likes(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/bartender/<name>', methods=["GET"])
def shift_sold(name):
    try:
        if name is None:
            raise ValueError("Bartender is not specified.")
        return jsonify(database.shift_sold(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)


@app.route('/api/sqlQuery', methods=["POST"])
def post_Query():
    try:
        body = json.loads(request.data)
        queryString = body["q"]
        print(queryString)
        return jsonify(database.tryQuery(queryString))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)     

@app.route('/api/addBar', methods=["POST"])
def addBar():
    try:
        body = json.loads(request.data)
        name = body["barName"]
        open = body["barOpen"]
        close = body["barClose"]
        license = body["barLicense"]
        phone = body["barPhone"]
        address = body["barAddress"]
        city = body["barCity"]
        state = body["barState"]
        return jsonify(database.insertBar(name, open, close, license, phone, address, city, state))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)   


@app.route('/api/bar/delete/<name>', methods=["GET"])
def deleteBar(name):
        return jsonify(database.deleteBar(name))




@app.route('/api/addBartender', methods=["POST"])
def addBartender():
    try:
        body = json.loads(request.data)
        name = body["bartenderName"]
        return jsonify(database.addBartender(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)   


@app.route('/api/bartender/delete/<name>', methods=["GET"])
def deleteBartender(name):
        return jsonify(database.deleteBartender(name))


@app.route('/api/inventory', methods=["GET"])
def get_inventorys():
    try:
        return jsonify(database.get_inventorys())
    except Exception as e:
        return make_response(str(e), 500)





@app.route('/api/item', methods=["GET"])
def get_items():
    try:
        return jsonify(database.get_items())
    except Exception as e:
        return make_response(str(e), 500)



@app.route('/api/like', methods=["GET"])
def get_likes():
    try:
        return jsonify(database.get_likes())
    except Exception as e:
        return make_response(str(e), 500)




@app.route('/api/sell', methods=["GET"])
def get_sells():
    try:
        return jsonify(database.get_sells())
    except Exception as e:
        return make_response(str(e), 500)



@app.route('/api/shift', methods=["GET"])
def get_shifts():
    try:
        return jsonify(database.get_shifts())
    except Exception as e:
        return make_response(str(e), 500)


@app.route('/api/addShift', methods=["POST"])
def addShift():
    try:
        body = json.loads(request.data)
        bar = body["shiftBar"]
        bartender = body["shiftBartender"]
        start = body["shiftStart"]
        end = body["shiftEnd"]
        date = body["shiftDate"]
        return jsonify(database.addShift(bar, bartender, start, end, date))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)   


@app.route('/api/shift/delete/<name>', methods=["GET"])
def deleteShift(bar,bartender,start,end,date):
        return jsonify(database.deleteShift(bar, bartender, start, end, date))


@app.route('/api/transaction', methods=["GET"])
def get_transactions():
    try:
        return jsonify(database.get_transactions())
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/addTransaction', methods=["POST"])
def addTransaction():
    try:
        body = json.loads(request.data)
        bill = body["transactionBill"]
        item = body["transactionItem"]
        count = body["transactionCount"]

        return jsonify(database.addTransaction(bill, item, count))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)   


@app.route('/api/transaction/delete/<name>', methods=["GET"])
def deleteTransaction(name):
        return jsonify(database.deleteTransaction(name))

@app.route('/api/addBeer', methods=["POST"])
def addBeer():
    try:
        body = json.loads(request.data)
        item = body["itemName"]
        manufacturer = body["manufacturerName"]
        return jsonify(database.addBeer(item, manufacturer))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)         

@app.route('/api/beer/delete/<name>', methods=["GET"])
def deleteBeer(item):
        return jsonify(database.deleteBeer(item))



@app.route('/api/bill', methods=["GET"])
def getBills():
    try:
        return jsonify(database.getBills())
    except Exception as e:
        return make_response(str(e), 500)





@app.route('/api/addDrinker', methods=["POST"])
def addDrinker():
    try:
        body = json.loads(request.data)
        name = body["drinkerName"]
        city = body["cityName"]
        state = body["stateName"]
        phone = body["phoneName"]
        address = body["addressName"]
        return jsonify(database.addDrinker(name, city, state, phone, address))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)   


@app.route('/api/drinker/delete/<name>', methods=["GET"])
def deleteDrinker(name):
        return jsonify(database.deleteDrinker(name))


@app.route('/api/food', methods=["GET"])
def getFood():
    try:
        return jsonify(database.getFood())
    except Exception as e:
        return make_response(str(e), 500)




@app.route('/api/freqs', methods=["GET"])
def getFreqs():
    try:
        return jsonify(database.getFreqs())
    except Exception as e:
        return make_response(str(e), 500)
