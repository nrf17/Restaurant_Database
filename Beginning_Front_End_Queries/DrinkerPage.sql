select b1.id, b1.bar, t1.item, b1.time, b1.date, t1.count, s1.price
from Bills b1, Transactions t1, Sells s1
where b1.drinker = 'Rubi Paul'
and t1.item in (select item from Beers)
and b1.id = t1.bill
and s1.bar = b1.bar
and s1.item = t1.item
order by b1.date