$( document ).ready(function() {
  var ctx = document.getElementById("chart1").getContext("2d");
  var ctx2 = document.getElementById("chart2").getContext("2d");
  var ctx3 = document.getElementById("chart3").getContext("2d");

  var pleaseWait = $('#pleaseWaitDialog');

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
        value: 10,
        color: "rgba(220,220,220,0.5)",
        highlight: "rgba(220,220,220,0.75)",
        label: "Neutral"
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
        value: 30,
        color: "rgba(220,220,220,0.5)",
        highlight: "rgba(220,220,220,0.75)",
        label: "Neutral"
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

	$('#query_button').on('click', function (e) {
		var first = $('#first_input').val();
		var second = $('#second_input').val();

		if (first && second) {
			console.log("Getting information...");
			pleaseWait.modal('show');
			$.when($.getJSON('update/name=' + first), $.getJSON('update/name=' + second)).then(function (resp1, resp2) {
				var first_res = resp1[0];
				var second_res = resp2[0];

				chart.datasets[0].bars[0].value = Math.round(first_res['total-score'] * 100);
				chart.datasets[0].bars[1].value = Math.round(second_res['total-score'] * 100);

				chart2.segments[0].value = first_res['positive'];
				chart2.segments[1].value = first_res['neutral'];
				chart2.segments[2].value = first_res['negative'];


				chart3.segments[0].value = second_res['positive'];
				chart3.segments[1].value = second_res['neutral'];
				chart3.segments[2].value = second_res['negative'];

				chart.update();
				chart2.update();
				chart3.update();

				$('#left_one').text(first_res['best-text']);
				$('#left_two').text(first_res['worst-text']);

				$('#right_one').text(second_res['best-text']);
				$('#right_two').text(second_res['worst-text']);

				pleaseWait.modal('hide');

			});
		}
	});
});