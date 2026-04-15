Chart.defaults.color = '#ffffff';
Chart.defaults.font.size = 16;
Chart.defaults.font.family = 'Poppins';


const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'pie',
    data: {
      datasets: [{
        data: [3, 2, 4, 2, 4],
        backgroundColor: [
        '#ff9100',
        '#f8e800',
        '#9775fa',
        '#007fb9', 
        '#51cf66' 
      ],
      borderColor: '#222',
    }],

    labels: [
        'HTML/CSS',
        'JS',
        'C/C++',
        'SQL',
        'Python'
    ]
    },

    options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            position: 'right'
        }
    }
}


    
  });

  