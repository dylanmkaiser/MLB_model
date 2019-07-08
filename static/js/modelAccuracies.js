// import final_preview
// var modelAccuracies = dict

var modelAccuracies = [{
  Model: "Logistic Regression",
  Accuracy: "58.6 %"
},
{
  Model: "Support Vector Machine",
  Accuracy: "57.8 %"
},
{
  Model: "Deep Neural Network",
  Accuracy: "57.4 %"
},
{
  Model: "Normal Neural Network",
  Accuracy: "57.3 %"
},
{
  Model: "K-Nearest Neighbors",
  Accuracy: "53.8 %"
},
{
  Model: "Random Forest",
  Accuracy: "52.1 %"
},
{
  Model: "Decision Tree",
  Accuracy: "50.6 %"
}
];

 d3.select("tbody")
  .selectAll("tr")
  .data(modelAccuracies)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Model}</td><td><strong>${d.Accuracy}</strong></td>`;
  });

