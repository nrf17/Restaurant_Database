select r.manufacturer, b.date, sum(t.count)
from Bills b, Transactions t, Beers r
where b.id = t.bill
and b.bar = 'Spilt Milk'
and t.item = r.item
group by r.manufacturer, b.date
order by b.date