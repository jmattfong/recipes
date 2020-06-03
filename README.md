## Recipes!

This app is implemented as a React.js frontend app, and a Python3 Flask backend server.

## Initial Setup
```
pip3 install -r requirements.txt
```

## Build React Frontend to vanilla HTML/CSS/JS files
```
./build.sh
```

You must compile the React application before running the production python server.

## Run Production Python Server
```
python3 src/server.py
```

Endpoint: http://localhost:5000/

## Debug React Frontend with Node.js Server
Useful when debugging UI issues

```
cd src/react-js
npm run start
```

Endpoint: http://localhost:3000/
