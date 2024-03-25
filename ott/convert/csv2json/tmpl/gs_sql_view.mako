create or replace view routes as
%for i, c in enumerate(csv):     
  %if c['id'].strip():
  <% id=c['id'].strip().lower() %>select ${id}a.agency_name, ${id}r.* 
   from ${id}.agency ${id}a, ${id}.routes ${id}r 
   where ${id}a.agency_id = ${id}r.agency_id ${'union all' if len(csv) > i+1 else ''}
  %endif
%endfor
;