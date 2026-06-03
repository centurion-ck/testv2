const API = "/api";

/* ==========================
   Cluster Metrics
========================== */

async function loadClusterMetrics() {

    try {

        const res =
            await fetch(
                `${API}/cluster-metrics`
            );

        const data =
            await res.json();

        document.getElementById(
            "healthScore"
        ).innerText =
            (data.health_score || 0) + "%";

        document.getElementById(
            "podCount"
        ).innerText =
            data.running_pods || 0;

        document.getElementById(
            "cpuUsage"
        ).innerText =
            (data.cpu_millicores || 0) + "m";

        document.getElementById(
            "memoryUsage"
        ).innerText =
            (data.memory_mib || 0) + "Mi";

    } catch (e) {

        console.log(
            "Metrics Error",
            e
        );

    }
}

/* ==========================
   Threat Stats
========================== */

async function loadStats() {

    try {

        const res =
            await fetch(
                `${API}/stats`
            );

        const data =
            await res.json();

        document.getElementById(
            "totalThreats"
        ).innerText =
            data.total || 0;

        document.getElementById(
            "criticalThreats"
        ).innerText =
            data.critical || 0;

        document.getElementById(
            "lowThreats"
        ).innerText =
            data.low || 0;

    } catch (e) {

        console.log(
            "Stats Error",
            e
        );

    }
}

/* ==========================
   Threat History
========================== */

async function loadHistory() {

    try {

        const res =
            await fetch(
                `${API}/history`
            );

        const data =
            await res.json();

        const tbody =
            document.querySelector(
                "#historyTable tbody"
            );

        tbody.innerHTML = "";

        data.reverse().forEach(item => {

            const color =
                item.severity ===
                "Critical"
                    ? "#ef4444"
                    : "#22c55e";

            tbody.innerHTML += `
            <tr>
                <td>${item.timestamp}</td>
                <td>${item.process_name}</td>
                <td>${item.prediction}</td>
                <td style="color:${color};font-weight:bold;">
                    ${item.severity}
                </td>
            </tr>
            `;
        });

    } catch (e) {

        console.log(
            "History Error",
            e
        );

    }
}

/* ==========================
   Pods
========================== */

async function loadPods() {

    try {

        const res =
            await fetch(
                `${API}/pods-json`
            );

        const data =
            await res.json();

        let pods = [];

        try {

            if (
                typeof data ===
                "string"
            ) {

                pods =
                    JSON.parse(data)
                    .items;

            } else if (
                data.items
            ) {

                pods =
                    data.items;

            }

        } catch {

            pods = [];

        }

        const table =
            document.getElementById(
                "podsTable"
            );

        table.innerHTML = "";

        pods.forEach(pod => {

            const statusColor =
                pod.status.phase ===
                "Running"
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

        console.log(
            "Pods Error",
            e
        );

    }
}

/* ==========================
   AI Prediction
========================== */

async function predictThreat() {

    const process_name =
        document.getElementById(
            "process"
        ).value;

    const cpu_usage =
        parseInt(
            document.getElementById(
                "cpu"
            ).value
        );

    const memory_usage =
        parseInt(
            document.getElementById(
                "memory"
            ).value
        );

    const res =
        await fetch(
            `${API}/predict`,
            {
                method:"POST",

                headers:{
                    "Content-Type":
                    "application/json"
                },

                body:
                JSON.stringify({
                    process_name,
                    cpu_usage,
                    memory_usage
                })
            }
        );

    const result =
        await res.json();

    const color =
        result.severity ===
        "Critical"
        ? "#ef4444"
        : "#22c55e";

    document.getElementById(
        "result"
    ).innerHTML = `

        <h2 style="color:${color}">
            ${result.prediction.toUpperCase()}
        </h2>

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

    const aiRes =
        await fetch(
            `${API}/recommendation`,
            {
                method:"POST",

                headers:{
                    "Content-Type":
                    "application/json"
                },

                body:JSON.stringify({

                    process_name,

                    cpu_usage,

                    memory_usage,

                    prediction:
                    result.prediction

                })
            }
        );

    const ai =
        await aiRes.json();

    document.getElementById(
        "recommendation"
    ).innerHTML = `

    <div
    style="
    background:#0f172a;
    padding:20px;
    border-radius:12px;
    border:1px solid #334155;
    "
    >

    <h2 style="color:#22c55e;">
    🧠 AI Security Analysis
    </h2>

    <p>
    <b>Security Score:</b>
    ${ai.security_score}/100
    </p>

    <p>
    <b>Severity:</b>
    ${ai.severity}
    </p>

    <p>
    <b>Root Cause:</b><br>
    ${ai.root_cause}
    </p>

    <p>
    <b>Impact:</b><br>
    ${ai.impact}
    </p>

    <h3>
    Recommended Actions
    </h3>

    <ul>

    ${ai.actions
        .map(
            a => `<li>${a}</li>`
        )
        .join("")}

    </ul>

    </div>
    `;

    loadStats();

    loadHistory();
}

/* ==========================
   Auto Remediation
========================== */

async function restartPod() {

    const podName =
        prompt(
            "Enter Pod Name"
        );

    if(!podName)
        return;

    const res =
        await fetch(
            `${API}/restart-pod`,
            {
                method:"POST",

                headers:{
                    "Content-Type":
                    "application/json"
                },

                body:
                JSON.stringify({
                    pod_name:podName,
                    namespace:
                    "kubeguardian"
                })
            }
        );

    const result =
        await res.json();

    alert(
        "Auto Remediation Completed"
    );

    console.log(result);

    loadPods();
}

/* ==========================
   Export
========================== */

window.predictThreat =
    predictThreat;

window.restartPod =
    restartPod;

/* ==========================
   Initial Load
========================== */

loadClusterMetrics();
loadStats();
loadHistory();
loadPods();

/* ==========================
   Auto Refresh
========================== */

setInterval(() => {

    loadClusterMetrics();
    loadStats();
    loadHistory();
    loadPods();

},10000);