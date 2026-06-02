import React, { useEffect, useState } from "react";

function App() {

  const [pods, setPods] = useState([]);

  const loadPods = async () => {

    const res = await fetch(
      "/api/pods-json"
    );

    const data = await res.json();

    const items = JSON.parse(data).items;

    setPods(items);
  };

  useEffect(() => {

    loadPods();

  }, []);

  const restartPod = async (podName) => {

    await fetch(
      "/api/restart-pod",
      {
        method: "POST",
        headers: {
          "Content-Type":
            "application/json"
        },
        body: JSON.stringify({
          pod_name: podName,
          namespace: "kubeguardian"
        })
      }
    );

    alert(
      "Auto Remediation Triggered"
    );

    setTimeout(
      loadPods,
      3000
    );
  };

  return (

    <div className="container">

      <h1>
        KubeGuardian AI
      </h1>

      <h2>
        Live Kubernetes Cluster
      </h2>

      <table>

        <thead>

          <tr>

            <th>Pod Name</th>

            <th>Status</th>

            <th>Action</th>

          </tr>

        </thead>

        <tbody>

        {
          pods.map(
            pod => (

            <tr
              key={
                pod.metadata.name
              }
            >

              <td>
                {
                  pod.metadata.name
                }
              </td>

              <td>
                {
                  pod.status.phase
                }
              </td>

              <td>

                <button
                  onClick={() =>
                    restartPod(
                      pod.metadata.name
                    )
                  }
                >
                  Restart
                </button>

              </td>

            </tr>

          ))
        }

        </tbody>

      </table>

    </div>
  );
}

export default App;