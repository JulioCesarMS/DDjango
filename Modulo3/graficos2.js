var milesRun = [2, 5, 4, 1, 2, 6, 5];
 
d3.select('body').append('svg')
    .attr('height', 300)
    .attr('width', 800)
    .selectAll('rect')
        .data(milesRun)
        .enter()
        .append('rect')
        .attr('y', function (d, i) { return i * 40 })
        .attr('height', 35)
        .attr('x', 0)
        .attr('width', function (d) { return d*100})
        .style('fill', 'steelblue');