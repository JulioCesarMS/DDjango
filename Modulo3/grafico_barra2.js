// Bar plot
function makeplot4() {
  Plotly.d3.csv("https://raw.githubusercontent.com/JulioCesarMS/DDjango/master/Modulo3/datasets/homicidios_por_mes.csv", function(data){ processData4(data) } );

};

function processData4(allRows) {

  console.log(allRows);
  var x = [], y = [];

  for (var i=0; i<allRows.length; i++) {
    row = allRows[i];
    x.push( row['Total'] );
    y.push( row['Mes '] );
  }
  console.log( 'X1',x, 'Y1',y );
  makePlotly4( x, y);
}

function makePlotly4( x, y ){
  var plotDiv = document.getElementById("plot");
  var traces = [{
    x: x,
    y: y,
    type: 'bar',
    orientation: 'h',
  }];

  Plotly.newPlot('grafica04', traces);
};
makeplot4();


