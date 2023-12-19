<h1>
${len(csv)} agencies included
The Portland Regional Trip Planner currently aggregates data for the following agencies:
<h1>

<table>
<tr>
  <th>Agency</th><th>Dates</th><th>Days</th><th>Alerts</th><th>Trip Updates</th><th>Vehicle Positions</th>
</tr>
feeds: [
  %for c in csv:
    %if c['gtfs'].strip():
<tr>
  <td>${c['id'].strip()}</td>
  <td>TBD</td>
  <td>-111</td>
  <td>TBD</td>
  %if c['alerts'].strip(): <td>YES</td> else: <td>NO</td> %endif
  %if c['alerts'].strip(): <td>YES</td> else: <td>NO</td> %endif
  %if c['alerts'].strip(): <td>YES</td> else: <td>NO</td> %endif
</tr>
    %endif
  %endfor
</table>
