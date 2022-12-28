
// npm i python-shell

const PythonShell = require('python-shell').PythonShell;

function loop() {

    let pyprog = new PythonShell('joystick.py', { mode: 'text'});
    pyprog.on('message', function (message) {
        // handle message (a line of text from stdout)
        console.log(message);
    });
   
}

loop();