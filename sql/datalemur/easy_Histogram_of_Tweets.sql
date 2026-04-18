-- https://datalemur.com/questions/sql-histogram-tweets

-- setup
create or replace table tweets
as 
select 
tweet_id::int tweet_id, user_id::int user_id, msg, strptime(tweet_date, '%m/%d/%Y %H:%M:%S') tweet_date
from (
values 
  ('214252', '111', 'Am considering taking Tesla private at $420. Funding secured.', '12/30/2021 00:00:00')
, ('739252', '111', 'Despite the constant negative press covfefe', '01/01/2022 00:00:00')
, ('846402', '111', 'Following @NickSinghTech on Twitter changed my life!', '02/14/2022 00:00:00')
, ('241425', '254', 'If the salary is so competitive why won’t you tell me what it is?', '03/01/2022 00:00:00')
, ('231574', '148', 'I no longer have a manager. I can''t be managed', '03/23/2022 00:00:00')
) t (tweet_id, user_id, msg, tweet_date)
;

-- solution

with user_cnt as (
SELECT user_id, count(*) tweet_bucket
FROM tweets
where year(tweet_date) = 2022
group by user_id
)
select tweet_bucket, count(user_id) users_num
from user_cnt
group by tweet_bucket
;