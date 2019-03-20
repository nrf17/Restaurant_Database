select b1.bar, sum(t1.count) s
from Transactions t1, Bills b1
where t1.item = 'Busch'
and t1.bill = b1.id
group by b1.bar
order by s desc
limit 10