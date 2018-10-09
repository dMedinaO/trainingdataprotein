var trace4 = {
  x: ['Accuracy', 'Recall', 'Precision'],
  y: [0.705508658, 0.7522222222, 0.8183401239],
  name: 'Clustering',
  error_y: {
    type: 'data',
    array: [0.0520973259, 0.1892933782, 0.1493328688],
    visible: true
  },
  type: 'bar'
};
var trace3 = {
  x: ['Accuracy', 'Recall', 'Precision'],
  y: [0.7446269821, 0.9563492063, 0.790430839],
  name: 'Recursive Clustering',
  error_y: {
    type: 'data',
    array: [0.1118538473, 0.1154891445, 0.122538816],
    visible: true
  },
  type: 'bar'
};
var trace2 = {
  x: ['Accuracy', 'Recall', 'Precision'],
  y: [0.7527941503, 0.9807692308, 0.7670573871],
  name: 'Interaction Sector',
  error_y: {
    type: 'data',
    array: [0.1052663858, 0.0693375245, 0.0969620126],
    visible: true
  },
  type: 'bar'
};
var trace1 = {
  x: ['Accuracy', 'Recall', 'Precision'],
  y: [0.6, 0.9, 0.65],
  name: 'Non Splitter',
  error_y: {
    type: 'data',
    array: [0.1052663858, 0.0693375245, 0.0969620126],
    visible: true
  },
  type: 'bar'
};
var data = [trace1, trace2, trace3, trace4];
var layout = {barmode: 'group',
				  title: 'Mean Performance for Models Generated'
				 };
Plotly.newPlot('myDiv', data, layout);
