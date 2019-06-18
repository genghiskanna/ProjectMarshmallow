    var ctx = document.getElementById("sentiment-chart");
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["Success", "Current"],
            datasets: [{
                label: 'Probability of success',
                data: sentiData,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
