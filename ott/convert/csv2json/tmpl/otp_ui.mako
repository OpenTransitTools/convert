
%for c in csv:
%if c['gtfs'].strip():
${c['id'].strip()}: ${c['gtfs'].strip()}
%endif
%endfor
