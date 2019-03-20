from sqlalchemy import create_engine
from sqlalchemy import sql
import random

from BarBeerDrinkerPlus import config

engine = create_engine(config.database_uri)

def get_bars():
    with engine.connect() as con:
        rs = con.execute("select name, open, close, license, phone, address, city, state from Bars;")
        return [dict(row) for row in rs]

def find_bar(name):
    with engine.connect() as con:
        query = sql.text(
                "select name, open, close, license, phone, address, city, state from Bars where name = :name;"
                )
        rs = con.execute(query, name=name)
        result = rs.first()
        if result is None:
            return None
        return dict(result)

# top drinkers who are largest spenders
def bar_larspenders(name):
    with engine.connect() as con:
        query = sql.text(
                "select drinker, sum(spent) as spend from( select b.drinker, t.item, (s.price * sum(t.count)) as spent from Sells s, Bills b, Transactions t where b.bar = :name and s.bar = :name and b.id = t.bill and t.item = s.item group by b.drinker, t.item) as results group by drinker order by spend desc limit 10;"
                )
        rs = con.execute(query, name=name)
        results = [dict(row) for row in rs]
        for r in results:
                r['spend'] = int(r['spend'])
        return results

# top 10 bars brands
def bar_toptenbrand(name):
    with engine.connect() as con:
        query = sql.text(
                "select r.manufacturer, b.date, sum(t.count) count from Bills b, Transactions t, Beers r where b.id = t.bill and b.bar = :name and t.item = r.item group by r.manufacturer, b.date order by b.date limit 10;"
                )
        rs = con.execute(query, name=name)
        results = [dict(row) for row in rs]
        for r in results:
                r['count'] = int(r['count'])
        return results

#bar time distributions
def bar_timedistr(name):
    with engine.connect() as con:
        query = sql.text(
                "select b.time, count(*) sales from Bills b, Transactions t where b.id = t.bill and b.bar = :name group by b.time order by b.time;"
                )
        rs = con.execute(query, name=name)
        results = [dict(row) for row in rs]
        for r in results:
                r['sales'] = int(r['sales'])
        return results

def bar_busiestdays(name):
    with engine.connect() as con:
        query = sql.text(
                "select b.date, count(*) sold from Bills b, Transactions t where b.id = t.bill and b.bar = :name group by b.date order by b.date;"
                )
        rs = con.execute(query, name=name)
        results = [dict(row) for row in rs]
        for r in results:
                r['sold'] = float(r['sold'])
        return results

#fraction sold
def bar_fractionsold(name):
    with engine.connect() as con:
        query = sql.text(
                "select b.date, t.item, ((sum(t.count)/i.count)*100) as fsold from Bills b, Transactions t, Inventory i where b.id = t.bill and b.bar = :name and t.item = i.item and i.bar = :name group by i.item, b.date order by b.date;"
                )
        rs = con.execute(query, name=name)
        results = [dict(row) for row in rs]
        for r in results:
                r['fsold'] = float(r['fsold'])
        return results







def get_beers():
    with engine.connect() as con:
        rs = con.execute("select item, manufacturer from Beers;")
        return [dict(row) for row in rs]

def beers_top_ten(beer_name):
  with engine.connect() as con:
        query = sql.text(
                "select b1.bar, sum(t1.count) sells from Transactions t1, Bills b1 where t1.item = :name and t1.bill = b1.id group by b1.bar order by sells desc limit 10"
                )
        rs = con.execute(query, name=beer_name)
        results = [dict(row) for row in rs]
        for r in results:
                r['sells'] = int(r['sells'])
        return results


def beers_consumer(beer_name):
  with engine.connect() as con:
        query = sql.text(
                "select b1.drinker, sum(t1.count) consumes from Transactions t1, Bills b1 where t1.item = 'Busch' and t1.bill = b1.id group by b1.bar, b1.drinker order by consumes desc"
                )
        rs = con.execute(query, name=beer_name)
        results = [dict(row) for row in rs]
        for r in results:
                r['consumes'] = int(r['consumes'])
        return results

def beers_time(beer_name):
  with engine.connect() as con:
        query = sql.text(
                "select b1.time, sum(t1.count) sells from Transactions t1, Bills b1 where t1.item = :name and t1.bill = b1.id group by b1.time order by b1.time"
                )
        rs = con.execute(query, name=beer_name)
        results = [dict(row) for row in rs]
        for r in results:
                r['sells'] = int(r['sells'])
        return results


def get_drinkers():
    with engine.connect() as con:
        rs = con.execute("select name, phone, address, city, state from Drinkers;")
        return [dict(row) for row in rs]

def find_drinker_info(drinker_name):
  with engine.connect() as con:
        query = sql.text(
                "select name, phone, address, city, state from Drinkers where name=:name;"
                )
        rs = con.execute(query, name=drinker_name)
        result = rs.first()
        if result is None:
            return None
        return dict(result)


def find_drinker_trans(drinker_name):
  with engine.connect() as con:
        query = sql.text(
                 "select b1.id, b1.bar, t1.item, b1.time, b1.date, t1.count, s1.price from Bills b1, Transactions t1, Sells s1 where b1.drinker = :name and t1.item in (select item from Beers) and b1.id = t1.bill and s1.bar = b1.bar and s1.item = t1.item order by b1.date;"
                )
        rs = con.execute(query, name=drinker_name)
        results = [dict(row) for row in rs]
        for r in results:
                r['price'] = float(r['price'])
        for r in results:
                r['count'] = int(r['count'])
        return results

def get_drinker_graph1(drinker_name):
  with engine.connect() as con:
        query = sql.text(
                "select t.item, sum(t.count) ordermost from Bills b, Transactions t where b.drinker = :name and t.item in (select item from Beers) and t.bill = b.id group by t.item order by ordermost desc"
                )
        rs = con.execute(query, name=drinker_name)
        results = [dict(row) for row in rs]
        for r in results:
                r['ordermost'] = int(r['ordermost'])
        return results

def get_drinker_graph2(drinker_name):
  with engine.connect() as con:
        query = sql.text(
                "select bar, date, sum(spent) as spend from( select b.bar, b.date, t.item, (s.price * sum(t.count)) as spent from Sells s, Bills b, Transactions t where b.drinker = :name and s.bar = b.bar and b.id = t.bill and t.item = s.item group by b.bar, b.date, t.item) as results group by bar, date order by spend desc"
                )
        rs = con.execute(query, name=drinker_name)
        results = [dict(row) for row in rs]
        for r in results:
                r['spend'] = float(r['spend'])
        return results

def get_bartenders():
        with engine.connect() as con:
                rs = con.execute("select name from Bartenders;")
                return [dict(row) for row in rs]



   
def get_manufacturers():
        with engine.connect() as con:
                rs = con.execute("select distinct manufacturer from Beers")
                return [dict(row) for row in rs]


def manuf_high_sales(name):
    with engine.connect() as con:
        query = sql.text(
                "select b.city, b.state, sum(t.count) sales from Bars b, Bills l, Transactions t, Beers r where r.item = t.item and r.manufacturer = :name and t.bill = l.id and l.bar = b.name group by b.city, b.state order by sum(t.count) desc"
                )
        rs = con.execute(query, name=name)
        result = [dict(row) for row in rs]
        for r in result:
                r['sales'] = int(r['sales'])
        return result


def manuf_likes(name):
    with engine.connect() as con:
        query = sql.text(
                "select d.city, d.state, count(*) as likes from Beers r, Drinkers d, Likes l where r.manufacturer = :name and l.drinker = d.name and r.item = l.item group by d.city, d.state order by likes desc"
                )
        rs = con.execute(query, name=name)
        result = [dict(row) for row in rs]
        for r in result:
                r['likes'] = int(r['likes'])
        return result




def shift_sold(name):
    with engine.connect() as con:
        query = sql.text(
                "select s.date, s.bar, r.item, sum(t.count) as sold from Shifts s, Beers r, Transactions t, Bills b where s.bartender = :name and t.item = r.item and b.id = t.bill and (b.time >= s.start or b.time <= s.end) and b.date = s.date group by s.date, r.item order by date, sold"
                )
        rs = con.execute(query, name=name)
        result = [dict(row) for row in rs]
        for r in result:
                r['sold'] = int(r['sold'])
        return result



def tryQuery(q):
         with engine.connect() as con:
                query = sql.text(q)
                rs = con.execute(query)

                if rs is None:
                        print("ERROR WHILE EXECUTING QUERY")
                        return None
                else:
                        return "SUCCESS"



def insertBar(name, open, close, license, phone, address, city, state):
        with engine.connect() as con:
                query = sql.text(
                        "INSERT INTO Bars (name, open, close, license, phone, address, city, state) \
                        VALUES (:name, :open, :close, :license, :phone, :address, :city, :state);"
                )
                rs = con.execute(query, name=name, open=open, close=close, license=license, phone=phone, address=address, city=city, state=state)

                if rs.rowcount>0:
                       return "Successfully added bar "
                else:
                        return "Failed to add bar" 

def deleteBar(name):
        with engine.connect() as con:
                query = sql.text(
                        "DELETE FROM Bars WHERE name = :name;"
                )
                rs = con.execute(query, name = name)
                if rs.rowcount>0:
                       return "Successfully deleted bar "
                else:
                        return "Failed to delete bar "



def addBartender(name):
        with engine.connect() as con:
                query = sql.text(
                        "INSERT INTO Bartenders (name) \
                        VALUES (:name);"
                )
                rs = con.execute(query, name=name)

                if rs.rowcount>0:
                       return "Successfully added bartender "
                else:
                        return "Failed to add bartender" 

def deleteBartender(name):
        with engine.connect() as con:
                query = sql.text(
                        "DELETE FROM Bartenders WHERE name = :name;"
                )
                rs = con.execute(query, name = name)
                if rs.rowcount>0:
                       return "Successfully deleted bartender "
                else:
                        return "Failed to delete bartender "     

def get_inventorys():
        with engine.connect() as con:
                rs = con.execute("select count,bar,item from Inventory;")
                return [dict(row) for row in rs]





def get_items():
        with engine.connect() as con:
                rs = con.execute("select name from Items;")
                return [dict(row) for row in rs]




def get_likes():
        with engine.connect() as con:
                rs = con.execute("select drinker, item from Likes;")
                return [dict(row) for row in rs]




def get_sells():
        with engine.connect() as con:
                rs = con.execute("select price,bar,item from Sells;")
                return [dict(row) for row in rs]





def get_shifts():
        with engine.connect() as con:
                rs = con.execute("select bar, bartender, start, end, date from Shifts;")
                return [dict(row) for row in rs]

def addShift(bar, bartender, start, end, date):
        with engine.connect() as con:
                query = sql.text(
                        "INSERT INTO Shifts (bar, bartender, start, end, date) \
                        VALUES (:bar, :bartender, :start, :end, :date);"
                )
                rs = con.execute(query, bar=bar, bartender=bartender, start=start, end=end, date=date)

                if rs.rowcount>0:
                       return "Successfully added Shift "
                else:
                        return "Failed to add Shift" 

def deleteShift(bar, bartender, start, end, date):
        with engine.connect() as con:
                query = sql.text(
                        "DELETE FROM Shifts WHERE bar = :bill AND bartender = :bartender AND start = :start AND end = :end AND date =:date;"
                )
                rs = con.execute(query, bar=bar, bartender=bartender, start=start, end=end, date=date)
                if rs.rowcount>0:
                       return "Successfully deleted Shift "
                else:
                        return "Failed to delete Shift "


def get_transactions():
        with engine.connect() as con:
                rs = con.execute("select bill, item, count from Transactions;")
                return [dict(row) for row in rs]

def addTransaction(bill, item, count):
        with engine.connect() as con:
                query = sql.text(
                        "INSERT INTO Transactions (bill, item, count) \
                        VALUES (:bill, :item, :count);"
                )
                rs = con.execute(query, bill=bill, item = item, count=count)

                if rs.rowcount>0:
                       return "Successfully added Transaction "
                else:
                        return "Failed to add Transaction" 

def deleteTransaction(bill):
        with engine.connect() as con:
                query = sql.text(
                        "DELETE FROM Transactions WHERE bill = :bill;"
                )
                rs = con.execute(query, bill = bill)
                if rs.rowcount>0:
                       return "Successfully deleted Transaction "
                else:
                        return "Failed to delete Transaction "


def addBeer(item, manufacturer):
        with engine.connect() as con:
                query = sql.text(
                        "INSERT INTO Beers (item, manufacturer) \
                        VALUES (:item, :manufacturer);"
                )
                rs = con.execute(query, item=item, manufacturer = manufacturer)

                if rs.rowcount>0:
                       return "Successfully added beer "
                else:
                        return "Failed to add beer" 

def deleteBeer(item):
        with engine.connect() as con:
                query = sql.text(
                        "DELETE FROM Beers WHERE item = :item;"
                )
                rs = con.execute(query, item = item)
                if rs.rowcount>0:
                       return "Successfully deleted beer "
                else:
                        return "Failed to delete beer "     


def getBills():
        with engine.connect() as con:
                query = sql.text(
                        "SELECT * FROM BBDPlus.Bills;"
                )
                rs = con.execute(query)
                return [dict(row) for row in rs]



def getFood():
        with engine.connect() as con:
                query = sql.text(
                        "SELECT * FROM BBDPlus.Food;"
                )
                rs = con.execute(query)
                return [dict(row) for row in rs]


def addDrinker(name, city, state, phone, address):
        with engine.connect() as con:
                query = sql.text(
                        "INSERT INTO Drinkers (name, city, state, phone, address) \
                        VALUES (:name, :city, :state, :phone, :address);"
                )
                rs = con.execute(query, name=name, city=city, state=state, phone=phone, address=address)

                if rs.rowcount>0:
                       return "Successfully added drinker "
                else:
                        return "Failed to add drinker" 

def deleteDrinker(name):
        with engine.connect() as con:
                query = sql.text(
                        "DELETE FROM Drinkers WHERE name = :name;"
                )
                rs = con.execute(query, name=name)
                if rs.rowcount>0:
                       return "Successfully deleted drinker "
                else:
                        return "Failed to delete drinker " 


def getFreqs():
        with engine.connect() as con:
                query = sql.text(
                        "SELECT * FROM BBDPlus.Frequents;"
                )
                rs = con.execute(query)
                return [dict(row) for row in rs]

