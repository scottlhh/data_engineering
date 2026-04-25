SELECT p.page_id FROM pages p
where not EXISTS
(select 1 from page_likes pl where pl.page_id = p.page_id)
order by p.page_id
;
