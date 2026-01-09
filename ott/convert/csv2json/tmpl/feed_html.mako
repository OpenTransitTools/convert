<h1>
The Regional Trip Planner (Portland, OR) currently loads the following agency feeds:
</h1>
<h2>
${len(csv)} feeds are being processed
</h2>
<%
  YES="&#9989;"
  NO="&#10060;"
%>
<table>
<tr>
  <th>Agency</th><th>GTFS</th><th>Alerts</th><th>Trip Updates</th><th>Vehicle Positions</th>
</tr>
  %for c in csv:
    %if c['gtfs'].strip():
<tr>
  <td>${c['id'].strip()} (fares${c['fare_type']})</td>
  <td><a href="${c['gtfs'].strip()}" target="#">GTFS</a> ${c['gtfs']}</td>
  %if c['alerts'].strip():
  <td><a href="${c['alerts'].strip()}&text=true" target="#">${YES} ${c['id']} Alerts </a></td>
  %else:
  <td>${NO}</td>
  %endif
  %if c['trips'].strip():
  <td><a href="${c['trips'].strip()}&text=true" target="#">${YES} ${c['id']} Trips </a></td>
  %else:
  <td>${NO}</td>
  %endif
  %if c['vehicles'].strip():
  <td><a href="${c['vehicles'].strip()}&text=true" target="#">${YES} ${c['id']} Vehicles </a></td>
  %else:
  <td>${NO}</td>
  %endif
</tr>
    %endif
  %endfor
</table>
