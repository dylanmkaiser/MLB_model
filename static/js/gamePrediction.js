// Need a list of dictionaries to display
// var text;
// for (var i = 0; i < 5; i++) {
//   text += "The number is " + i + "<br>";
// }

// for games in today: 
//     "HomeTeam" = df[0]
//     "AwayTeam" = df[1]  

var gamePrediction = [{
  HomeTeam: "Baltimore Orioles",
  AwayTeam: "Cleveland Indians",
  PredictedWinner: "Baltimore Orioles"
},
{
  HomeTeam: "Baltimore Orioles",
  AwayTeam: "Cleveland Indians",
  PredictedWinner: "Win"
},
// {
//   "HomeTeam": "Baltimore Orioles",
//   "AwayTeam": "Cleveland Indians",
//   "PredictedWinner": "Win"
// },
// {
//   "HomeTeam": "Baltimore Orioles",
//   "AwayTeam": "Cleveland Indians",
//   "PredictedWinner": "Win"
// },
// {
//   "HomeTeam": "Baltimore Orioles",
//   "AwayTeam": "Cleveland Indians",
//   "PredictedWinner": "Win"
// }
];

 d3.select("tbody")
  .selectAll("tr")
  .data(gamePrediction)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.HomeTeam}</td><td>${d.AwayTeam}</td><td><strong>${d.PredictedWinner}</strong></td>`;
  });

