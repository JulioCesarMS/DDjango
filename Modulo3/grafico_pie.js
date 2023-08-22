// Bar plot
function makeplot3() {
  Plotly.d3.csv("https://raw.githubusercontent.com/JulioCesarMS/DDjango/master/Modulo3/datasets/delitos_porcentaje2.csv", function(data){ processData3(data) } );

};

function processData3(allRows) {

  console.log(allRows);
  var x = [], y = [];

  for (var i=0; i<allRows.length; i++) {
    row = allRows[i];
    x.push( row['Porcentaje'] );
    y.push( row['Tipo de delito'] );
  }
  console.log( 'X1',x, 'Y1',y );
  makePlotly3( x, y);
}

function makePlotly3( x, y ){
  var plotDiv = document.getElementById("plot");
  var traces = [{
    values: x,
    labels: y,
    hole: .5,
    type: 'pie',
  }];

  Plotly.newPlot('grafica03', traces);
};
makeplot3();


