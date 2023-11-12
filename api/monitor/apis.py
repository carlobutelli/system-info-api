import logging
import psutil
from flask import Blueprint, jsonify, current_app as app


monitor = Blueprint("monitor", __name__)

log = logging.getLogger()

olddata = {}
olddata["disk_write"] = 0
olddata["disk_read"] = 0
olddata["net_sent"] = 0
olddata["net_recv"] = 0


#
# This route returns real time process information as a REST API
#
@monitor.route("/api/process")
def api_process():
    data = {}
    data["processes"] = []
    for proc in psutil.process_iter():
        try:
            cmdline = proc.cmdline()
        except psutil.AccessDenied:
            continue
        except (psutil.ZombieProcess, psutil.NoSuchProcess):
            pass
        except Exception:
            log.exception("something is wrong: " + ' '.join(cmdline))
            continue

        process_info = proc.as_dict(
            attrs=["pid", "name", "memory_percent", "num_threads", "cpu_times"]
        )
        data["processes"].append(process_info)

    return jsonify(data)


#
# This route returns real time system metrics as a REST API
#
@monitor.route("/api/monitor")
def api_monitor():
    apidata = {}
    apidata["cpu"] = psutil.cpu_percent(interval=0.9)
    apidata["mem"] = psutil.virtual_memory().percent
    apidata["disk"] = psutil.disk_usage("/").percent

    try:
        netio = psutil.net_io_counters()
        apidata["net_sent"] = (
            0 if olddata["net_sent"] == 0 else netio.bytes_sent - olddata["net_sent"]
        )
        olddata["net_sent"] = netio.bytes_sent
        apidata["net_recv"] = (
            0 if olddata["net_recv"] == 0 else netio.bytes_recv - olddata["net_recv"]
        )
        olddata["net_recv"] = netio.bytes_recv
    except Exception:
        apidata["net_sent"] = -1
        apidata["net_recv"] = -1

    try:
        diskio = psutil.disk_io_counters()
        apidata["disk_write"] = (
            0
            if olddata["disk_write"] == 0
            else diskio.write_bytes - olddata["disk_write"]
        )
        olddata["disk_write"] = diskio.write_bytes
        apidata["disk_read"] = (
            0 if olddata["disk_read"] == 0 else diskio.read_bytes - olddata["disk_read"]
        )
        olddata["disk_read"] = diskio.read_bytes
    except Exception:
        apidata["disk_write"] = -1
        apidata["disk_read"] = -1

    return jsonify(apidata)
