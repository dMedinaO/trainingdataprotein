$(document).ready(function(){

  var trace1 = {
    x: ['LOU', 'CV x'],
    y: [0.597721, 0.597140],

    type: 'bar',
    name:'performance A'
  };

  var trace2 = {
    x: ['LOU', 'CV x'],
    y: [0.554129, 0.548105],

    type: 'bar',
    name:'performance B'
  };

  var trace3 = {
    x: ['LOU', 'CV x'],
    y: [0.563594, 0.560083],

    type: 'bar',
    name:'performance C'
  };

  var trace4 = {
    x: ['LOU', 'CV x'],
    y: [0.653788, 0.628333],

    type: 'bar',
    name:'performance D'
  };

  var trace5 = {
    x: ['LOU', 'CV x'
  ],
    y: [0.630128, 0.587179],

    type: 'bar',
    name:'performance E'
  };


  var data = [trace1, trace2, trace3, trace4, trace5];

  var layout = {
    title: 'Comparación performance values para grupo X',
    barmode: 'group'
  };

  Plotly.newPlot('myDiv', data, layout);
});
