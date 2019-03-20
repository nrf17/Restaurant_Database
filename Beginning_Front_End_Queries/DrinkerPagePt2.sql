select t.item, sum(t.count)
from Bills b, Transactions t
where b.drinker = 'Alfred Vang'
and t.item in (select item from Beers)
and t.bill = b.id
group by t.item
order by sum(t.count) desc