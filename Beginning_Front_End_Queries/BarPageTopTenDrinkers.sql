select drinker, sum(spent) as spend from(
select b.drinker, t.item, (s.price * sum(t.count)) as spent
from Sells s, Bills b, Transactions t
where b.bar = 'Spilt Milk'
and s.bar = 'Spilt Milk'
and b.id = t.bill
and t.item = s.item
group by b.drinker, t.item) as results
group by drinker
order by spend desc