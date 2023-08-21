// Bar plot
function makeplot2() {
  Plotly.d3.csv("https://raw.githubusercontent.com/JulioCesarMS/DDjango/master/Modulo3/datasets/homicidios_estado.csv", function(data){ processData2(data) } );

};

function processData2(allRows) {

  console.log(allRows);
  var x = [], y = [];

  for (var i=0; i<allRows.length; i++) {
    row = allRows[i];
    x.push( row['Etiquetas de fila'] );
    y.push( row['Total'] );
  }
  console.log( 'X1',x, 'Y1',y );
  makePlotly2( x, y);
}

function makePlotly2( x, y ){
  var plotDiv = document.getElementById("plot");
  var traces = [{
    x: x,
    y: y,
    type: 'bar',
  }];

  Plotly.newPlot('grafica02', traces);
};
makeplot2();




