;with s as (SELECT extract(year from transaction_date) t_year
, product_id
, sum(spend) spend
FROM user_transactions
group by 1, 2
)
, s2 as (
select t_year, product_id, spend
, lag(spend) over (partition by product_id order by t_year) prev_spend
from s
)
select t_year as year
,product_id
,spend as curr_year_spend
,prev_spend as prev_year_spend
,cast((spend - prev_spend)/prev_spend * 100 as decimal(19, 2)) as yoy_rate
from s2
order by 2, 1
;
