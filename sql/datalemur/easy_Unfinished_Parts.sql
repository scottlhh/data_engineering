SELECT part, assembly_step FROM parts_assembly p
where finish_date is NULL
and exists (select 1 from parts_assembly ps where ps.part = p.part and ps.assembly_step=1)
;
