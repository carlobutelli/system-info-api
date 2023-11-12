import logging
import os
import sys
import uuid

from flask import Flask, request, g
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    with app.app_context():

        CORS(app)

        from .info.views import info as info_bp
        from .monitor.apis import monitor as monitor_bp
        app.register_blueprint(info_bp)
        app.register_blueprint(monitor_bp)

        # shell context for flask cli
        app.shell_context_processor({"app": app})

        # log handler
        log_level = logging.INFO if not app.config.get("DEBUG") else logging.DEBUG
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(log_level)
        handler.setFormatter(logging.Formatter(
            "[%(asctime)s] %(levelname)s: %(message)s "
            "[in %(pathname)s:%(lineno)d]"
        ))

        logging.getLogger("flask_cors").level = logging.DEBUG

        for h in app.logger.handlers:
            app.logger.removeHandler(h)
        app.logger.addHandler(handler)
        app.logger.setLevel(log_level)

        app.logger.info("[WARMUP]: app successfully instantiated")

        @app.before_request
        def set_transaction_id():
            transaction_id = request.headers.get("X-Request-ID")
            g.transaction_id = transaction_id if transaction_id else str(uuid.uuid4().hex)

    return app

