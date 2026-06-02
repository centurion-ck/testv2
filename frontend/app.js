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
            "http://127.0.0.1:8000/predict",
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
        `;

    }
    catch(error){

        document.getElementById("result").innerHTML =
        "Backend API not reachable";

        console.error(error);
    }
}