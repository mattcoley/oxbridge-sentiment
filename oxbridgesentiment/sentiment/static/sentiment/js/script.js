$( document ).ready(function() {
  var ctx = document.getElementById("chart1").getContext("2d");
  var ctx2 = document.getElementById("chart2").getContext("2d");
  var ctx3 = document.getElementById("chart3").getContext("2d");

  var data = {
    labels: ["cats", "dogs"],
    datasets: [
        {
            label: "My First dataset",
            fillColor: "#46BFBD",
            strokeColor: "rgba(220,220,220,0.8)",
            highlightFill: "#5AD3D1",
            highlightStroke: "rgba(220,220,220,1)",
            data: [80, 10]
        },
	    ]
	};


	var data2 = [
	{
        value: 40,
        color: "#46BFBD",
        highlight: "#5AD3D1",
        label: "Positive"
    },
    {
        value: 30,
        color:"#F7464A",
        highlight: "#FF5A5E",
        label: "Negative"
    },
]

	var data3 = [
	{
        value: 80,
        color: "#46BFBD",
        highlight: "#5AD3D1",
        label: "Positive"
    },
    {
        value: 10,
        color:"#F7464A",
        highlight: "#FF5A5E",
        label: "Negative"
    },
]

	var chart = new Chart(ctx).Bar(data, {
	    barShowStroke: false,
	    barValueSpacing: 70
	});

	var chart2 = new Chart(ctx2).Doughnut(data2, {
	});

	var chart3 = new Chart(ctx3).Doughnut(data3, {
	});


    
});