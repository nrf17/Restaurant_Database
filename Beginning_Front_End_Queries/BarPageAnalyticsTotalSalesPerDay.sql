select b.bar, s.bartender, sum(t.count) as total
from Bills b, Transactions t, Shifts s
where t.bill = b.id
and b.date = '1/2/2018'
and t.item = 'Busch'
and s.bar = b.bar
and s.date = b.date
group by b.bar
order by sum(t.count) desc