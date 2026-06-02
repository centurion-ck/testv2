from fastapi import APIRouter
import subprocess

router = APIRouter(
    prefix="/api",
    tags=["Metrics"]
)

@router.get("/cluster-metrics")
def cluster_metrics():

    try:

        nodes = subprocess.check_output(
            ["kubectl", "get", "nodes", "--no-headers"]
        ).decode()

        node_count = len(
            nodes.strip().split("\n")
        )

        pods = subprocess.check_output(
            [
                "kubectl",
                "get",
                "pods",
                "-n",
                "kubeguardian",
                "--no-headers"
            ]
        ).decode()

        pod_count = len(
            pods.strip().split("\n")
        )

        top = subprocess.check_output(
            [
                "kubectl",
                "top",
                "pods",
                "-n",
                "kubeguardian",
                "--no-headers"
            ]
        ).decode()

        cpu_total = 0
        memory_total = 0

        for line in top.splitlines():

            parts = line.split()

            if len(parts) >= 3:

                cpu = parts[1]
                memory = parts[2]

                cpu_total += int(
                    cpu.replace("m", "")
                )

                memory_total += int(
                    memory.replace("Mi", "")
                )

        return {

            "cluster_health": 98,

            "nodes": node_count,

            "pods": pod_count,

            "cpu_usage_millicores":
                cpu_total,

            "memory_usage_mib":
                memory_total
        }

    except Exception as e:

        return {
            "error": str(e)
        }