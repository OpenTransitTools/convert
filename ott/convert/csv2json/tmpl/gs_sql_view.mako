drop materialized view if exists routes;
create materialized view routes as
%for i, c in enumerate(csv):     
  %if c['id'].strip():
  <% id=c['id'].strip().lower() %>select ${id}a.agency_name, ${id}r.* 
   from ${id}.agency ${id}a, ${id}.routes ${id}r, ${id}.current_routes ${id}cr
   where ${id}a.agency_id = ${id}r.agency_id 
   and ${id}cr.route_id = ${id}r.route_id 
   ${'union all' if len(csv) > i+1 else ''}
  %endif
%endfor
;

create unique index on routes(agency_id, route_id);
create index on routes using GIST(geom);
vacuum full analyze routes;
