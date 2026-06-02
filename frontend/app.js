const API = "/api";

async function loadStats() {

    try {

        const res = await fetch(`${API}/stats`);
        const data = await res.json();

        document.getElementById("totalThreats").innerText =
            data.total || 0;

        document.getElementById("criticalThreats").innerText =
            data.critical || 0;

        document.getElementById("lowThreats").innerText =
            data.low || 0;

    } catch (e) {

        console.log(e);

    }
}

async function loadHistory() {

    try {

        const res = await fetch(`${API}/history`);
        const data = await res.json();

        const tbody =
            document.querySelector("#historyTable tbody");

        tbody.innerHTML = "";

        data.reverse().forEach(item => {

            const severityColor =
                item.severity === "Critical"
                    ? "#ef4444"
                    : "#22c55e";

            tbody.innerHTML += `
            <tr>
                <td>${item.timestamp}</td>
                <td>${item.process_name}</td>
                <td>${item.prediction}</td>
                <td style="color:${severityColor};font-weight:bold;">
                    ${item.severity}
                </td>
            </tr>
            `;
        });

    } catch (e) {

        console.log(e);

    }
}

async function loadPods() {

    try {

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

        document.getElementById("podCount").innerText =
            pods.length;

        pods.forEach(pod => {

            const statusColor =
                pod.status.phase === "Running"
                    ? "#22c55e"
                    : "#ef4444";

            table.innerHTML += `
            <tr>
                <td>${pod.metadata.name}</td>
                <td>${pod.metadata.namespace}</td>
                <td style="color:${statusColor};font-weight:bold;">
                    ${pod.status.phase}
                </td>
            </tr>
            `;
        });

    } catch (e) {

        console.log(e);

    }
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
                "Content-Type": "application/json"
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

    let badge =
        result.severity === "Critical"
        ?
        `<span style="
            background:#ef4444;
            color:white;
            padding:8px 16px;
            border-radius:8px;
            font-weight:bold;
        ">
        CRITICAL
        </span>`
        :
        `<span style="
            background:#22c55e;
            color:white;
            padding:8px 16px;
            border-radius:8px;
            font-weight:bold;
        ">
        LOW
        </span>`;

    document.getElementById("result")
        .innerHTML = `

        <h2>
            ${badge}
        </h2>

        <p>
        <b>Prediction:</b>
        ${result.prediction}
        </p>

        <p>
        <b>Threat Type:</b>
        ${result.threat_type}
        </p>

        <p>
        <b>Severity:</b>
        ${result.severity}
        </p>

        <p>
        <b>Confidence:</b>
        ${result.score}
        </p>

        <p>
        <b>Recommendation:</b>
        ${result.recommendation}
        </p>

    `;

    loadStats();
    loadHistory();
}

async function restartPod() {

    const podName =
        prompt(
            "Enter Pod Name"
        );

    if (!podName) return;

    document.getElementById("result")
        .innerHTML = `
        <h3 style="color:#f59e0b;">
        Triggering Auto Remediation...
        </h3>
        `;

    const res = await fetch(
        `${API}/restart-pod`,
        {
            method: "POST",
            headers: {
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

    document.getElementById("result")
        .innerHTML = `
        <h2 style="color:#22c55e;">
        Auto Remediation Completed
        </h2>

        <pre>
${JSON.stringify(result, null, 2)}
        </pre>
        `;

    loadPods();
}

window.predictThreat =
    predictThreat;

window.restartPod =
    restartPod;

loadStats();
loadHistory();
loadPods();

setInterval(() => {

    loadStats();
    loadHistory();
    loadPods();

}, 10000);