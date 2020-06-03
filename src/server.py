#!/usr/bin/env python3

import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path=None)

REACT_BUILD_DIR = 'react-js/build'

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory(REACT_BUILD_DIR, path)

def main() :
    # Flask automatically sends static files from ./static, but we override to keep all static files with the React app
    app.static_url_path = f'{REACT_BUILD_DIR}/static/'
    app.static_folder = f'{app.root_path}/{app.static_url_path}'

    print(f"Serving React's build artifacts from path: {app.root_path}/{REACT_BUILD_DIR}")

    app.run()

if __name__ == '__main__':
    main()
