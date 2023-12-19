<h1>
${len(csv)} agencies included
The Portland Regional Trip Planner currently aggregates data for the following agencies:
<h1>

<%
  YES="&#9989;"
  NO="&#10060;"
%>
<table>
<tr>
  <th>Agency</th><th>Dates</th><th>Days</th><th>Alerts</th><th>Trip Updates</th><th>Vehicle Positions</th>
</tr>
  %for c in csv:
    %if c['gtfs'].strip():
<tr>
  <td>${c['id'].strip()}</td>
  <td>TBD</td>
  <td>-111</td>
  %if c['alerts'].strip():
  <td>${YES}</td>
  %else:
  <td>${NO}</td>
  %endif
  %if c['trips'].strip():
  <td>${YES}</td>
  %else:
  <td>${NO}</td>
  %endif
  %if c['vehicles'].strip():
  <td>${YES}</td>
  %else:
  <td>${NO}</td>
  %endif
</tr>
    %endif
  %endfor
</table>
