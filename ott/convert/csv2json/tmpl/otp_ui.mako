transitOperators:
%for c in csv:
%if c['gtfs'].strip():
  %for l in logo(c):
  - feedId: ${c['id']}
    agencyId: ${l['id']}
    logo: ${l['url']}
    order: ${num(c['order'])}
    %if loop.index == 0:
    name: ${c['id']}
    %endif
  %endfor
%endif
%endfor
