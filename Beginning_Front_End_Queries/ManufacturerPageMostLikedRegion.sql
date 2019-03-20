select d.city, d.state, count(*)
from Beers r, Drinkers d, Likes l
where r.manufacturer = 'Boston Beer Co'
and l.drinker = d.name
and r.item = l.item
group by d.city, d.state
order by count(*) desc