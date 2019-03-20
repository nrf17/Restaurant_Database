select b.city, b.state, sum(t.count)
from Bars b, Bills l, Transactions t, Beers r
where r.item = t.item
and r.manufacturer = 'Boston Beer Co'
and t.bill = l.id
and l.bar = b.name
group by b.city, b.state
order by sum(t.count) desc