
// Bar plot
function makeplot() {
  Plotly.d3.csv("https://raw.githubusercontent.com/JulioCesarMS/DDjango/master/Modulo3/datasets/homicidios_estado.csv", function(data){ processData(data) } );

};

function processData(allRows) {
  
  console.log(allRows);
  var x = [], y = [];

  for (var i=0; i<allRows.length; i++) {
    row = allRows[i];
    x.push( row['Etiquetas de fila'] );
    y.push( row['Total'] );
  }
  console.log( 'X',x, 'Y',y );
  makePlotly( x, y);
}

var data = [
  {
    x: x,
    y: y,
    type: 'bar'
  }
];

Plotly.newPlot('grafica02', data);




