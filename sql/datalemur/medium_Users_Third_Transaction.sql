with txn_rank as (
SELECT *
, row_number() over (partition by user_id order by transaction_date) as rn
FROM transactions
)
select user_id, spend, transaction_date from txn_rank
where rn= 3
;
