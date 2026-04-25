SELECT 
  sum(case when device_type in ('laptop') then 1 else null end) laptop_views
, sum(case when device_type in ('tablet', 'phone') then 1 else null end) mobile_views
FROM viewership;
