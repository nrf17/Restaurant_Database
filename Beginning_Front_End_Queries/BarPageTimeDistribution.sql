select b.time, count(*)
from Bills b, Transactions t
where b.id = t.bill
and b.bar = 'Spilt Milk'
group by b.time
order by b.time