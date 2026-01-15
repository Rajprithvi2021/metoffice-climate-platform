let chart;


async function loadMetrics() {
  const res = await fetch("/api/metrics/");
  const metrics = await res.json();

  const select = document.getElementById("metricSelect");
  select.innerHTML = "";

  metrics.forEach(m => {
    const opt = document.createElement("option");
    opt.value = m.id;
    opt.textContent = `${m.parameter} (${m.region})`;
    select.appendChild(opt);
  });

  updateMetricBadge();
}


function updateMetricBadge() {
  const text =
    document.getElementById("metricSelect")
      .selectedOptions[0].textContent;

  document.getElementById("activeMetric").textContent = text;
}


async function loadMonthly() {
  updateMetricBadge();

  const metricId = metricSelect.value;
  const year = yearInput.value;

  const res = await fetch(
    `/api/weather/monthly/?metric_id=${metricId}&year=${year}`
  );
  const data = await res.json();

  renderChart(
    data.data.map(v => `Month ${v.month}`),
    data.data.map(v => v.value),
    `Monthly Climate Data (${year})`
  );
}


async function loadAnnual() {
  updateMetricBadge();

  const metricId = metricSelect.value;
  const res = await fetch(`/api/weather/annual/?metric_id=${metricId}`);
  const data = await res.json();

  renderChart(
    data.map(v => v.year),
    data.map(v => v.value),
    "Annual Climate Trend"
  );
}

function renderChart(labels, values, title) {
  if (chart) chart.destroy();

  chart = new Chart(document.getElementById("chart"), {
    type: "line",
    data: {
      labels,
      datasets: [{
        label: title,
        data: values,
        borderColor: "#2563eb",
        backgroundColor: "rgba(37,99,235,0.15)",
        borderWidth: 2,
        tension: 0.35,
        fill: true,
        pointRadius: 3,
        pointHoverRadius: 6
      }]
    },
    options: {
      animation: {
        duration: 800,
        easing: "easeOutQuart"
      },
      plugins: {
        legend: {
          labels: {
            usePointStyle: true
          }
        },
        tooltip: {
          backgroundColor: "#111827",
          titleColor: "#fff",
          bodyColor: "#e5e7eb"
        }
      },
      scales: {
        x: { grid: { display: false } },
        y: { beginAtZero: false }
      },
      responsive: true,
      maintainAspectRatio: false
    }
  });
}

document.getElementById("metricSelect")
  .addEventListener("change", updateMetricBadge);

loadMetrics();
