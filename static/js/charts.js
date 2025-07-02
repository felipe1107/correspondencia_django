document.addEventListener("DOMContentLoaded", function () {
    const ctxEntradas = document.getElementById("graficoEntradas");
    const ctxSalidas = document.getElementById("graficoSalidas");

    if (ctxEntradas) {
        fetch("/entradas/por-mes/")
            .then(response => response.json())
            .then(data => {
                new Chart(ctxEntradas, {
                    type: "bar",
                    data: {
                        labels: data.labels,
                        datasets: [{
                            label: "Entradas por mes",
                            data: data.data,
                            borderWidth: 1
                        }]
                    }
                });
            });
    }

    if (ctxSalidas) {
        fetch("/salidas/por-mes/")
            .then(response => response.json())
            .then(data => {
                new Chart(ctxSalidas, {
                    type: "bar",
                    data: {
                        labels: data.labels,
                        datasets: [{
                            label: "Salidas por mes",
                            data: data.data,
                            borderWidth: 1
                        }]
                    }
                });
            });
    }
});
