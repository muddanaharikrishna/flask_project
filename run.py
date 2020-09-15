# This file job is only running the application
from flaskblog import app

if __name__ == '__main__':
    app.run(debug=True)

