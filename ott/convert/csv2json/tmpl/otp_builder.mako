  %for i, c in enumerate(csv):
    %if c['gtfs'].strip():
    {
      "type": "gtfs",
      "feedId": "${c['id'].strip()}",
      "source": "${c['id'].strip()}.gtfs.zip"
    }${',' if len(csv) > i+1 else ''}
    %endif
  %endfor
