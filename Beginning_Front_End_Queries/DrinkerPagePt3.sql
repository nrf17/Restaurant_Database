select bar, date, sum(spent) as spend from(
select b.bar, b.date, t.item, (s.price * sum(t.count)) as spent
from Sells s, Bills b, Transactions t
where b.drinker = 'Aaron Rogers'
and s.bar = b.bar
and b.id = t.bill
and t.item = s.item
group by b.bar, b.date, t.item) as results
group by bar, date
order by spend desc