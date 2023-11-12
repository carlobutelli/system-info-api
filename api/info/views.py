from flask import Blueprint, render_template, current_app as app

import psutil
import platform
import datetime


info = Blueprint("info", __name__)


@info.route("/")
def index():
    return render_template("index.html")


@info.route("/info")
def sysinfo():
    osinfo = {}
    osinfo["plat"] = platform
    osinfo["cpu"] = platform.uname().machine + " x " + str(psutil.cpu_count(logical=False))
    osinfo["mem"] = psutil.virtual_memory()
    osinfo["net"] = psutil.net_if_addrs()
    osinfo["boottime"] = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    return render_template("info.html", info=osinfo)


@info.route("/monitor")
def monitor():
    return render_template("monitor.html")
