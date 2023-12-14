feeds: [
  %for row in csv:
    %if row['gtfs'].strip():
    {"url": "${row['gtfs'].strip()}", "name": "${row['id'].strip()}.gtfs.zip"},
    %endif
  %endfor
]