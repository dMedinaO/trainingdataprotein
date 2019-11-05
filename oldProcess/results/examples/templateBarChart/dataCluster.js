$(document).ready(function(){

  var trace1 = {
    x: ['Algoritmo 1',
'Algoritmo 2',
'Algoritmo 3',
'Algoritmo 4',
'Algoritmo 5',
'Algoritmo 6',
'Algoritmo 7',
'Algoritmo 8',
'Algoritmo 9',
'Algoritmo 10'
],
    y: [0.597721, 0.597140, 0.596974,0.593425,0.589721,0.589590,0.589425,0.589259,0.586929,0.586028],

    type: 'bar',
    name:'performance A'
  };

  var trace2 = {
    x: ['Algoritmo 1',
'Algoritmo 2',
'Algoritmo 3',
'Algoritmo 4',
'Algoritmo 5',
'Algoritmo 6',
'Algoritmo 7',
'Algoritmo 8',
'Algoritmo 9',
'Algoritmo 10'
],
    y: [0.554129, 0.548105, 0.546796, 0.543306, 0.540572, 0.533333, 0.532340, 0.531685, 0.529445, 0.525097],

    type: 'bar',
    name:'performance B'
  };

  var trace3 = {
    x: ['Algoritmo 1',
'Algoritmo 2',
'Algoritmo 3',
'Algoritmo 4',
'Algoritmo 5',
'Algoritmo 6',
'Algoritmo 7',
'Algoritmo 8',
'Algoritmo 9',
'Algoritmo 10'
],
    y: [0.563594, 0.560083, 0.557383, 0.538243, 0.534083, 0.527691, 0.526212, 0.523309, 0.522833, 0.518846],

    type: 'bar',
    name:'performance C'
  };



  var data = [trace1, trace2, trace3];

  var layout = {
      title: 'División para n grupos',
      barmode:'group'

    };

  Plotly.newPlot('myDiv', data, layout);
});
