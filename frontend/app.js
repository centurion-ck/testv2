async function predictThreat() {

    const processName =
        document.getElementById("process").value;

    const cpu =
        parseFloat(
            document.getElementById("cpu").value
        );

    const memory =
        parseFloat(
            document.getElementById("memory").value
        );

    try {

        const response = await fetch(
            "http://47.129.227.107:8000/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    process_name: processName,
                    cpu_usage: cpu,
                    memory_usage: memory
                })
            }
        );

        const data = await response.json();

        document.getElementById("result").innerHTML = `
    <h3>Prediction: ${data.prediction}</h3>
    <h3>Score: ${data.score}</h3>
    <h3>Severity: ${data.severity}</h3>
    <h3>Threat Type: ${data.threat_type}</h3>
    <h3>Recommendation: ${data.recommendation}</h3>
`;

    }
    catch(error){

        document.getElementById("result").innerHTML =
        "Backend API not reachable";

        console.error(error);
    }
}


async function loadHistory() {

    try {

        const response =
            await fetch(
                "http://47.129.227.107:8000/history"
            );

        const data =
            await response.json();

        let rows = "";

        data.forEach(item => {

            rows += `
            <tr>
                <td>${item.timestamp}</td>
                <td>${item.process_name}</td>
                <td>${item.prediction}</td>
                <td>${item.severity}</td>
            </tr>
            `;
        });

        document.querySelector(
            "#historyTable tbody"
        ).innerHTML = rows;

    }
    catch(error){

        console.log(error);
    }
}

loadHistory();

setInterval(loadHistory, 5000);

async function loadPods() {

    const response = await fetch(
        "http://13.215.252.224:8000/pods"
    );

    const data = await response.json();

    console.log(data);
}


async function loadStats(){

    const response =
        await fetch(
            "http://47.129.227.107:8000/stats"
        );

    const data =
        await response.json();

    document.getElementById(
        "totalThreats"
    ).innerText = data.total;

    document.getElementById(
        "criticalThreats"
    ).innerText = data.critical;

    document.getElementById(
        "lowThreats"
    ).innerText = data.low;
}

loadStats();

setInterval(loadStats,5000);
