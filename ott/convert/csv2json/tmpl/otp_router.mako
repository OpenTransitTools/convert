  "updaters": [
  %for c in csv:
    %if c['alerts'].strip():
    {
      "type": "real-time-alerts",
      "frequency": "45s",
      "url": "${c['alerts'].strip()}",
      "feedId": "${c['id'].strip()}"
    },
    %endif
    %if c['trips'].strip():
    {
      "type": "stop-time-updater",
      "frequency": "31s",
      "url": "${c['trips'].strip()}",
      "feedId": "${c['id'].strip()}"
    },
    %endif
    %if c['vehicles'].strip():
    {
      "type": "vehicle-positions",
      "frequency": "29s",
      "url": "${c['vehicles'].strip()}",
      "feedId": "${c['id'].strip()}"
    },
    %endif
  %endfor
    ]
