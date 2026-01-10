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
      %if c['id'].strip() == "TRIMET":
      "frequency": "11s",
      %else:
      "frequency": "11s",
      %endif
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
      %if c['id'].strip() == "TRIMET":
      "frequency": "13s",
      %else:
      "frequency": "14s",
      %endif
      %if c['fuzzy_trips'].strip():
      "fuzzyTripMatching": true,
      %endif
      "url": "${c['vehicles'].strip()}",
      "feedId": "${c['id'].strip()}"
    }${',' if len(csv) > i+1 else ''}
    %endif
  %endfor
    ]
