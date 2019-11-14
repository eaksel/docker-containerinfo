from flask import Flask, render_template
from datetime import datetime
import os
import socket
import platform


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
        current_time=datetime.utcnow(),
        hostname=socket.getfqdn(),
        ip=" / ".join(socket.gethostbyname_ex(socket.gethostname())[2]),
        cpu=os.cpu_count(),
        system=f"{platform.system()} {platform.release()}",
        distribution=" ".join(platform.linux_distribution()).strip(),
        platform=platform.architecture()[0])


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
