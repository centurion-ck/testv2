from fastapi import APIRouter
import subprocess

router = APIRouter(prefix="/api")

@router.get("/cluster-metrics")
def cluster_metrics():

    try:

        output = subprocess.check_output(
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
        mem_total = 0
        pod_count = 0

        for line in output.splitlines():

            parts = line.split()

            cpu = parts[1]
            mem = parts[2]

            cpu_total += int(
                cpu.replace("m","")
            )

            mem_total += int(
                mem.replace("Mi","")
            )

            pod_count += 1

        health = 100

        if cpu_total > 500:
            health = 80

        if cpu_total > 1000:
            health = 60

        return {
            "health_score": health,
            "running_pods": pod_count,
            "cpu_millicores": cpu_total,
            "memory_mib": mem_total
        }

    except Exception as e:

        return {
            "error": str(e)
        }