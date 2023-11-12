# import os
from api import create_app

app = create_app()

if __name__ == "__main__":
    # port = int(os.environ.get("PORT", 5000))
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(threaded=True, load_dotenv=True)