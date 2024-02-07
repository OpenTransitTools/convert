transitOperators:
%for c in csv:
  %if c['id'].strip():
  - feedId: ${c['id']}
    agencyId: ${agency(c)}
    logo: ${c['url']}
    order: ${num(c['order'])}
    %if c['name'].strip():
    name: "${c['name']}"
    %endif
  %endif
%endfor
