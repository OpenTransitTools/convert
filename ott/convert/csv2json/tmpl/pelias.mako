    "transit": {
      "datapath": "/data/transit",
      "feeds": [
        %for c in csv:
          %if c['gtfs'].strip():
          {
            "layerId": "stops",
            "layerName": "stops",
            "url": "${c['gtfs'].strip()}",
            "filename": "${c['id'].strip()}-stops.txt",
            "agencyId": "${c['id'].strip()}",
            "agencyName": "${c['id'].strip()}"
          },
          %endif
        %endfor
      ]
