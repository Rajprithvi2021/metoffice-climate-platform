let chart;

const MONTH_NAMES = [
  "Jan", "Feb", "Mar", "Apr", "May", "Jun",
  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
];


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
  const selected =
    document.getElementById("metricSelect")
      .selectedOptions[0].textContent;

  document.getElementById("activeMetric").textContent = selected;
}


async function loadMonthly() {
  updateMetricBadge();

  const metricId = document.getElementById("metricSelect").value;
  const year = document.getElementById("yearInput").value;

  const res = await fetch(
    `/api/weather/monthly/?metric_id=${metricId}&year=${year}`
  );
  const data = await res.json();

  renderChart(
    data.data.map(v => MONTH_NAMES[v.month - 1] ?? `Month ${v.month}`),
    data.data.map(v => v.value),
    `Monthly Climate Data (${year})`
  );
}


async function loadAnnual() {
  updateMetricBadge();

  const metricId = document.getElementById("metricSelect").value;
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
      labels: labels,
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
          titleColor: "#ffffff",
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

document
  .getElementById("metricSelect")
  .addEventListener("change", updateMetricBadge);

loadMetrics();
