  "transitFeeds": [
  %for c in csv:
    %if c['gtfs'].strip():
    {
      "type": "gtfs",
      "feedId": "${c['id'].strip()}",
      "source": "${c['id'].strip()}.gtfs.zip"
    },
    %endif
  %endfor
  ]
