[gtfs]
feeds: [
  %for c in csv:
    %if c['gtfs'].strip():
    {"url": "${c['gtfs'].strip()}", "name": "${c['id'].strip()}.gtfs.zip"},
    %endif
  %endfor
]


[gtfs_realtime]
feeds: [
  %for c in csv:
    %if c['alerts'].strip() or c['trips'].strip() or c['vehicles'].strip():
    {
        %for n in ['alerts', 'trips', 'vehicles']:
        %if c[n].strip():
        "${n}": "${c[n].strip()}",
        %endif
        %endfor
        "agency_id": "${c['id'].strip()}"
    },
    %endif
  %endfor
]
