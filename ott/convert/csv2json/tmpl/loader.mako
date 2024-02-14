[gtfs]
feeds: [
  %for i, c in enumerate(csv):
    %if c['gtfs'].strip():
    {"url": "${c['gtfs'].strip()}", "name": "${c['id'].strip()}.gtfs.zip"}${',' if len(csv) > i+1 else ''}
    %endif
  %endfor
  ]


[gtfs_realtime]
feeds: [
  %for i, c in enumerate(csv):
    %if c['alerts'].strip() or c['trips'].strip() or c['vehicles'].strip():
    {
        %for n in ['alerts', 'trips', 'vehicles']:
        %if c[n].strip():
        "${n}": "${c[n].strip()}",
        %endif
        %endfor
        "agency_id": "${c['id'].strip()}"
    }${',' if len(csv) > i+1 else ''}
    %endif
  %endfor
  ]
