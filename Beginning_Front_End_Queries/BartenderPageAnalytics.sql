select s.bartender, sum(t.count)
from Bills b, Transactions t, Shifts s
where t.bill = b.id
and b.date = '1/2/2018'
and s.bar = b.bar
and s.date = b.date
and t.item in (select item from Beers)
group by s.bartender
order by sum(t.count) desc