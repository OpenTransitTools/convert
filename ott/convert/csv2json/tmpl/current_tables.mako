<%def name="route_cols(tbl)">
%for c in ['route_id', 'agency_id', 'route_label', 'route_short_name', 'route_long_name', 'route_type', 'route_color', 'route_text_color', 'route_sort_order']:
    ${tbl}r.${c}, 
%endfor
</%def>

-- create current views (depends on an existing 'current' schema): 
-- psql -d ott -U ott -f current_tables.views.txt

-- routes
drop materialized view if exists current.routes;
create materialized view current.routes as
%for i, c in enumerate(csv):
  %if c['id'].strip():
  <% bid = c['id']; id=bid.strip().lower() %>select CONCAT('${id}', '::', ${id}r.route_id) as id, '${bid}' as feed_id, ${id}a.agency_name, ${route_cols(id)}    ${id}cr.geom
   from ${id}.agency ${id}a, ${id}.routes ${id}r, ${id}.current_routes ${id}cr
   where ${id}a.agency_id = ${id}r.agency_id 
   and ${id}cr.route_id = ${id}r.route_id 
   ${'union all' if len(csv) > i+1 else ''}
  %endif
%endfor
;

create unique index on current.routes(id);
create unique index on current.routes(agency_id, route_id);
create index on current.routes using GIST(geom);
vacuum full analyze current.routes;


-- stops
drop materialized view if exists current.stops;
create materialized view current.stops as
%for i, c in enumerate(csv):
  %if c['id'].strip():
  <% bid = c['id']; id=bid.strip().lower() %>select CONCAT('${bid}', '::', ${id}s.stop_id) as id, '${bid}' as feed_id, ${id}cs.route_short_names, ${id}cs.route_mode, ${id}cs.route_type, ${id}s.* 
   from ${id}.stops ${id}s, ${id}.current_stops ${id}cs
   where ${id}s.stop_id = ${id}cs.stop_id
   ${'union all' if len(csv) > i+1 else ''}
  %endif
%endfor
;

create unique index on current.stops(id);
create unique index on current.stops(feed_id, stop_id);
create index on current.stops using GIST(geom);
vacuum full analyze current.stops;


-- flex regions
drop materialized view if exists current.flex;
create materialized view current.flex as
%for i, c in enumerate(csv):
  %if c['id'].strip():
  <% bid = c['id']; id=bid.strip().lower() %>select CONCAT('${bid}', '::', ${id}l.id) as pk, '${bid}' as feed_id, ${id}l.*
   from ${id}.locations ${id}l
   ${'union all' if len(csv) > i+1 else ''}
  %endif
%endfor
;

create unique index on current.flex(pk);
create index on current.flex using GIST(geom);
vacuum full analyze current.flex;
