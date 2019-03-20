select exists(
select 1 from Items where name = 'Busch') 
as resultsitem;
select exists(
select 1 from Drinkers where name = 'Aaron')
as resultsdrinker;
select exists(
select 1 from Bars where name = 'Thing')
as resultsbar;
select exists(
select 1 from Bartenders where name = 'Someone')
as resultsbartender;
select exists(
select 1 from Bills where id = 'Number')
as resultsbill;