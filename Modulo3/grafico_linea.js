function makeplot() {
    Plotly.d3.csv("https://raw.githubusercontent.com/JulioCesarMS/DDjango/master/Modulo3/datasets/homicidios_anio.csv", function(data){ processData(data) } );
  
  };
  
  function processData(allRows) {
  
    console.log(allRows);
    var x = [], y = [];
  
    for (var i=0; i<allRows.length; i++) {
      row = allRows[i];
      x.push( row['Anio'] );
      y.push( row['Total'] );
    }
    console.log( 'X',x, 'Y',y );
    makePlotly( x, y);
  }
  
  function makePlotly( x, y ){
    var plotDiv = document.getElementById("plot");
    var traces = [{
      x: x,
      y: y
    }];
  
    Plotly.newPlot('grafica01', traces,
      {title: 'Homicidios cometidos por año en México'});
  };
makeplot();


