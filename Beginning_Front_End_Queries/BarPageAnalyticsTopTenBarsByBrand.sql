select r.item, b.bar, sum(t.count)
from Beers r, Bills b, Transactions t
where r.item = t.item
and t.bill = b.id
and r.item = 'Ballast Point'
group by r.item, b.bar
order by r.item, sum(t.count) desc