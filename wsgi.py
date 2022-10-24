from app import create_app
import os

app=create_app(os.environ.get("ENVIRONMENT",None))

if __name__=="__main__":
    app.run()
    