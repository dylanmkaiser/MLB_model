//Retrieve predictions data output by predictions.py
d3.csv("static/js/display_data.csv", function(data) {

// Append to website
    d3.select("tbody")
    .selectAll("tr")
    .data(data)
    .enter()
    .append("tr")
    .html(function(d) {
      return `<td>${d.home_name}</td><td>${d.away_name}</td><td><strong>${d.predicted_winner}</strong></td>`;
    });
});