from belial_backend import create_app
from belial_backend.database import map_repository

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
    print(map_repository.get_map(1))
