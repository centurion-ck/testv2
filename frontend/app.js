const API = "/api";

async function loadStats() {

    const res = await fetch(`${API}/stats`);
    const data = await res.json();

    document.getElementById("totalThreats").innerText =
        data.total || 0;

    document.getElementById("criticalThreats").innerText =
        data.critical || 0;

    document.getElementById("lowThreats").innerText =
        data.low || 0;
}

async function loadHistory() {

    const res = await fetch(`${API}/history`);

    const data = await res.json();

    const tbody =
        document.querySelector("#historyTable tbody");

    tbody.innerHTML = "";

    data.reverse().forEach(item => {

        tbody.innerHTML += `
        <tr>
            <td>${item.timestamp}</td>
            <td>${item.process_name}</td>
            <td>${item.prediction}</td>
            <td>${item.severity}</td>
        </tr>
        `;
    });
}

async function loadPods() {

    const res = await fetch(`${API}/pods-json`);

    const data = await res.json();

    let pods = [];

    try {
        pods = JSON.parse(data).items;
    } catch {
        pods = [];
    }

    const table =
        document.getElementById("podsTable");

    table.innerHTML = "";

    pods.forEach(pod => {

        table.innerHTML += `
        <tr>
            <td>${pod.metadata.name}</td>
            <td>${pod.metadata.namespace}</td>
            <td>${pod.status.phase}</td>
        </tr>
        `;
    });
}

async function predictThreat() {

    const process_name =
        document.getElementById("process").value;

    const cpu_usage =
        parseInt(
            document.getElementById("cpu").value
        );

    const memory_usage =
        parseInt(
            document.getElementById("memory").value
        );

    const res = await fetch(
        `${API}/predict`,
        {
            method: "POST",
            headers: {
                "Content-Type":"application/json"
            },
            body: JSON.stringify({
                process_name,
                cpu_usage,
                memory_usage
            })
        }
    );

    const result =
        await res.json();

    document.getElementById("result")
        .innerHTML = `
        <h3>${result.prediction}</h3>

        <p>
        Threat Type:
        ${result.threat_type}
        </p>

        <p>
        Severity:
        ${result.severity}
        </p>

        <p>
        Confidence:
        ${result.score}
        </p>

        <p>
        Recommendation:
        ${result.recommendation}
        </p>
    `;

    loadStats();
    loadHistory();
}

async function restartPod() {

    const podName =
        prompt(
            "Enter pod name to restart"
        );

    if(!podName) return;

    const res = await fetch(
        `${API}/restart-pod`,
        {
            method:"POST",
            headers:{
                "Content-Type":
                "application/json"
            },
            body: JSON.stringify({
                pod_name: podName,
                namespace:
                "kubeguardian"
            })
        }
    );

    const result =
        await res.json();

    alert(
        "Remediation Completed"
    );

    console.log(result);

    loadPods();
}

window.predictThreat =
    predictThreat;

window.restartPod =
    restartPod;

loadStats();
loadHistory();
loadPods();

setInterval(
    loadPods,
    15000
);