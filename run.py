import os
from app import app, fask_sqlachemy

if __name__ == '__main__':
    app().run()

app.run(host='0.0.0.0', port=5000, debug=True)