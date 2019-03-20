select b1.time, sum(t1.count)
from Transactions t1, Bills b1
where t1.item = 'Busch'
and t1.bill = b1.id
group by b1.time
order by b1.time