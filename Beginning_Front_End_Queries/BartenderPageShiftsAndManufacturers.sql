select s.date, r.manufacturer, sum(t.count)
from Shifts s, Beers r, Transactions t, Bills b
where s.bartender = 'Addison Morales'
and t.item = r.item
and b.id = t.bill
and (b.time >= s.start
	or b.time <= s.end)
and b.date = s.date
group by s.date, r.manufacturer
order by s.date