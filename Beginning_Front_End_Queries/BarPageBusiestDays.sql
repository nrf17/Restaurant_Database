select b.date, count(*)
from Bills b, Transactions t
where b.id = t.bill
and b.bar = 'Spilt Milk'
group by b.date
order by b.date