# min / hour / month-day / month / weekday

# alerts
%for i, c in enumerate(csv):
  %if c['alerts'].strip():
*/15 * * * * source ~/.bashrc; cd ~/rtp/loader; bin/gtfsrt-load -vurl null -turl null -c >> logs/gtfsrt_alerts_load.log 2>&1;
  %endif
%endfor

# vehicles
%for i, c in enumerate(csv):
  %if c['vehicles'].strip():
  "agency_id": "${c['id'].strip()}"
*/15 * * * * source ~/.bashrc; cd ~/rtp/loader; bin/gtfsrt-load -vurl null -turl null -c >> logs/gtfsrt_vehicles_load.log 2>&1;
  %endif
%endfor

# trip updates
%for i, c in enumerate(csv):
  %if c['trip'].strip():
  "agency_id": "${c['id'].strip()}"
*/15 * * * * source ~/.bashrc; cd ~/rtp/loader; bin/gtfsrt-load -vurl null -turl null -c >> logs/gtfsrt_vehicles_load.log 2>&1;
  %endif
%endfor

