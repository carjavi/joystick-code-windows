<p align="center"><img src="https://raw.githubusercontent.com/carjavi/joystick-code-windows/master/img/joystick.png" height="200" alt=" " /></p>
<h1 align="center">Joystick Code Windows</h1> 
<h4 align="right">Dic 22</h4>

<img src="https://img.shields.io/badge/OS-Windows%2011-blue">
<img src="https://img.shields.io/badge/Node%20-V18.7.0-green">
<img src="https://img.shields.io/badge/Python%20-V3.9.2-orange">

<br>

Programming to Receive Joystick Input in Windows

<br>

## Displaying Physical Buttons
GameSir T4 Pro Joystick. Compatible Joystick  X-BOX 360 pad / EasySMX ESM-9110.

<img src="https://raw.githubusercontent.com/carjavi/joystick-code-windows/master/img/GameSir-T4-Pro.png" height="250" alt="">
<img src="https://raw.githubusercontent.com/carjavi/joystick-code-windows/master/img/GameSir-T4-Pro2.png" height="300" alt="">

<br>

## Buttons / Variables Input Library Python
* A. Left Analog (LSB Left Stick Button) ```Absolute ABS_Y / Absolute ABS_X```
* B. Direction Button
  * UP ```Absolute ABS_HAT0Y```
  * DOWN ```Absolute ABS_HAT0Y```
  * LEFT ```Absolute ABS_HAT0X```
  * RIGHT ```Absolute ABS_HAT0X```
* C. Select Button ```Key BTN_START```
* D. Home Button ```none```
* E. Start Button ```Key BTN_SELECT```
* F. Right Analog (RSB Right Stick Button) ```Absolute ABS_RY / Absolute ABS_RX```
* G. ABXY Button
  *  A Button (Bottom) ```Key BTN_SOUTH```
  *  B Button (Right) ```Key BTN_EAST```
  *  X Button (Left) ```Key BTN_WEST```
  *  Y Button (Top) ```Key BTN_NORTH```
* H. Turbo Button ```none```
* K. LB Button ```Key BTN_TL```
* M. LT Button  ```Absolute ABS_Z``` 
* L. RB Button  ```Key BTN_TR```
* N. RT Button ```Absolute ABS_RZ```
* R. M1 M3 Button
  * M1 ```Key BTN_EAST```
  * M3 ```Key BTN_NORTH```
* S. M2 M4 Button
  * M2 ```Key BTN_SOUTH```
  * M4 ```Key BTN_WEST```

<br>

## Variables GamePad
### NORTH, SOUTH, EAST, WEST
```Key BTN_xxx 1``` KeyPress <br>
```Key BTN_xxx 0``` Key-Release
### Direction Button
```Absolute ABS_HAT0Y 0``` Key-Release<br>
```Absolute ABS_HAT0X 0``` Key-Release<br>
```Absolute ABS_HAT0Y -1``` KeyUP<br>
```Absolute ABS_HAT0Y 1``` KeyDown<br>
```Absolute ABS_HAT0X 1``` KeyRight<br>
```Absolute ABS_HAT0X -1``` KeyLeft
### Left Analog (-32768 -0- 32768)
```Absolute ABS_Y 0``` Key-Release<br>
```Absolute ABS_X 0``` Key-Release<br>
```Absolute ABS_Y 32768``` KeyUP<br>
```Absolute ABS_Y -32768``` KeyDown<br>
```Absolute ABS_X 32768``` KeyRight<br>
```Absolute ABS_X -32768``` KeyLeft
### Right Analog (-32768 -0- 32768)
```Absolute ABS_RY 0``` Key-Release<br>
```Absolute ABS_RX 0``` Key-Release<br>
```Absolute ABS_RY 32768``` KeyUP<br>
```Absolute ABS_RY -32768``` KeyDown<br>
```Absolute ABS_RX 32768``` KeyRight<br>
```Absolute ABS_RX -32768``` KeyLeft
### LB & RB (TL & TR Trigger) 
```Key BTN_Tx 1``` KeyPress<br>
```Key BTN_Tx 0``` Key-Release
###  LT & RT (0-255 Trigger)
```Absolute ABS_Z 0``` Key-Release<br>
```Absolute ABS_RZ 0``` Key-Release<br>
```Absolute ABS_Z 255``` KeyPress (left)<br>
```Absolute ABS_RZ 255``` KeyPress (rigth)<br>
 
<br>

## RawInput Joystick Input Examples
## Python
Library
```
pip install inputs
```
Getting events from input library. ```event.ev_type --> Absolute o Sync```  / ``` event.code --> ABS_xxx```

<br>

file **joystick.py** 
```
import inputs
import sys


def joystick():
    while True:
        try: 
            events = inputs.get_gamepad()
            for event in events:
                # print(event.ev_type, event.code, event.state)

                # Buttons
                if event.code == 'BTN_SOUTH' and event.state == 1:
                    print('A 1') # Button Press
                if event.code == 'BTN_SOUTH' and event.state == 0:
                    print('A 0') # Button Release
                if event.code == 'BTN_NORTH' and event.state == 1:
                    print('Y 1') # Button Press
                if event.code == 'BTN_NORTH' and event.state == 0:
                    print('Y 0') # Button Release
                if event.code == 'BTN_WEST' and event.state == 1:
                    print('X 1') # Button Press
                if event.code == 'BTN_WEST' and event.state == 0:
                    print('X 0') # Button Release
                if event.code == 'BTN_EAST' and event.state == 1:
                    print('B 1') # Button Press
                if event.code == 'BTN_EAST' and event.state == 0:
                    print('B 0') # Button Release
                if event.code == 'BTN_TR' and event.state == 1:
                    print('TR 1') # Button Press
                if event.code == 'BTN_TR' and event.state == 0:
                    print('TR 0') # Button Release
                if event.code == 'BTN_TL' and event.state == 1:
                    print('TL 1') # Button Press
                if event.code == 'BTN_TL' and event.state == 0:
                    print('TL 0') # Button Release
                if event.code == 'BTN_START' and event.state == 1:
                    print('SELECT 1') # Button Press
                if event.code == 'BTN_START' and event.state == 0:
                    print('SELECT 0') # Button Release
                if event.code == 'BTN_SELECT' and event.state == 1:
                    print('START 1') # Button Press
                if event.code == 'BTN_SELECT' and event.state == 0:
                    print('START 0') # Button Release
                
                # Direction Button
                if event.code == 'ABS_HAT0Y' and event.state == 0:
                    print('ABS_HAT0Y 0 ') # Release Y
                if event.code == 'ABS_HAT0Y' and event.state == -1:
                    print('ABS_HAT0Y -1 ') # Up
                if event.code == 'ABS_HAT0Y' and event.state == 1:
                    print('ABS_HAT0Y 1 ') # Down
                if event.code == 'ABS_HAT0X' and event.state == 0:
                    print('ABS_HAT0X 0 ') # Release X
                if event.code == 'ABS_HAT0X' and event.state == -1:
                    print('ABS_HAT0X -1 ') # Left
                if event.code == 'ABS_HAT0X' and event.state == 1:
                    print('ABS_HAT0X 1 ') # Right
                
                # Analog Right
                if event.code == 'ABS_RY' and event.state == 0:
                    print('ABS_RY 0')
                if event.code == 'ABS_RX' and event.state == 0:
                    print('ABS_RX 0')
                if event.code == 'ABS_RY' and event.state != 0:
                    print('ABS_RY', event.state) # ABS_RY > 0 Up / RSB < 0 Down
                if event.code == 'ABS_RX' and event.state != 0:
                    print('ABS_RX', event.state) # ABS_RX > 0 Right / RSB < 0 Left

                #Left Analog
                if event.code == 'ABS_Y' and event.state == 0:
                    print('ABS_Y 0')
                if event.code == 'ABS_X' and event.state == 0:
                    print('ABS_X 0')
                if event.code == 'ABS_Y' and event.state != 0:
                    print('ABS_Y', event.state) # ABS_Y > 0 Up / RSB < 0 Down
                if event.code == 'ABS_X' and event.state != 0:
                    print('ABS_X', event.state) # ABS_X > 0 Right / RSB < 0 Left
                
                #Left LT & RT
                if event.code == 'ABS_Z' and event.state == 0:
                    print('ABS_Z 0') 
                if event.code == 'ABS_RZ' and event.state == 0:
                    print('ABS_RZ 0') 
                if event.code == 'ABS_Z' and event.state != 0:
                    print('ABS_Z', event.state) # ABS_Z > 0 Press Left
                if event.code == 'ABS_RZ' and event.state != 0:
                    print('ABS_RZ', event.state) # ABS_RZ > 0 Press Right

                #Exportar Data to NodeJS
                sys.stdout.flush()
                
        except Exception:
            print("joystick disconnected")
            return

if __name__ == "__main__":
    while True:
        joystick()
   
```

> :warning: **Warning:** 
> Si inicia con el gamepad desconectado no lo va a reconocer hasta que se reinicie el archivo Python.

> :memo: **Note:** 
> Si se inicia con el gamepad instalado y se desconecta la app espera que se vuelva a conectar.

> :memo: **Note:** 
 -Botones M1=(A button),M2=(B button),M3=(X button),M4=(Y button) 
 -Botones Turbo, Home, Mode no funcionan.

<br>

<img  align="middle" width="32" height="32" src="https://raw.githubusercontent.com/carjavi/joystick-code-windows/master/img/python.svg"> [joystick.py](https://url.com)

<br>

more inf: <br>
https://pypi.org/project/inputs/ <br>
https://pypi.org/project/inputs/

<br>

## NodeJS 
install
```
npm i python-shell
```

file **py-from-node.js**
```
const PythonShell = require('python-shell').PythonShell;

function loop() {

    let pyprog = new PythonShell('joystick.py', { mode: 'text'});
    pyprog.on('message', function (message) {
        // handle message (a line of text from stdout)
        console.log(message);
    });
   
}

loop();
```

<img  align="middle" width="32" height="32" src="https://raw.githubusercontent.com/carjavi/joystick-code-windows/master/img/js.svg"> [py-from-node.js](https://url.com)

<br>

---
Copyright &copy; 2022 [carjavi](https://github.com/carjavi). <br>
```www.instintodigital.net``` <br>
carjavi@hotmail.com <br>
<p align="center">
    <a href="https://instintodigital.net/" target="_blank"><img src="https://raw.githubusercontent.com/carjavi/joystick-code-windows/master/img/developer.png" height="100" alt="www.instintodigital.net"></a>
</p>