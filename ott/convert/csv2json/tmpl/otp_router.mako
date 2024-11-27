  "updaters": [
  %for i, c in enumerate(csv):
    %if c['alerts'].strip():
    {
      "type": "real-time-alerts",
      "frequency": "45s",
      %if c['fuzzy_trips'].strip():
      "fuzzyTripMatching": true,
      %endif
      "url": "${c['alerts'].strip()}",
      "feedId": "${c['id'].strip()}"
    },
    %endif
    %if c['trips'].strip():
    {
      "type": "stop-time-updater",
      "frequency": "31s",
      %if c['fuzzy_trips'].strip():
      "fuzzyTripMatching": true,
      %endif
      "url": "${c['trips'].strip()}",
      "feedId": "${c['id'].strip()}"
    },
    %endif
    %if c['vehicles'].strip():
    {
      "type": "vehicle-positions",
      "frequency": "29s",
      %if c['fuzzy_trips'].strip():
      "fuzzyTripMatching": true,
      %endif
      "url": "${c['vehicles'].strip()}",
      "feedId": "${c['id'].strip()}"
    }${',' if len(csv) > i+1 else ''}
    %endif
  %endfor
    ]
