from app.site import app
import os 
import sys
from flask_cors import CORS

# Cross origin reference crap
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
