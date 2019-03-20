select b.date, t.item, ((sum(t.count)/i.count)*100) as psold
from Bills b, Transactions t, Inventory i
where b.id = t.bill
and b.bar = 'Spilt Milk'
and t.item = i.item
and i.bar = 'Spilt Milk'
group by i.item, b.date
order by b.date