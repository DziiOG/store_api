from src import app
from src.config.config import PORT, DEBUG

if __name__ == '__main__':
    app.run(port=int(PORT), debug=DEBUG)