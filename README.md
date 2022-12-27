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
GameSir T4 Pro Joystick

<img src="https://raw.githubusercontent.com/carjavi/joystick-code-windows/master/img/GameSir-T4-Pro.png" height="250" alt="">
<img src="https://raw.githubusercontent.com/carjavi/joystick-code-windows/master/img/GameSir-T4-Pro2.png" height="300" alt="">

<br>

## Buttons
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
### LB & RB (TL & TR)
```Key BTN_Tx 1``` KeyPress<br>
```Key BTN_Tx 0``` Key-Release
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
###  LT & RT (0-255)
```Absolute ABS_Z 0``` Key-Release<br>
```Absolute ABS_RZ 0``` Key-Release<br>
```Absolute ABS_Z 255``` KeyPress (left)<br>
```Absolute ABS_RZ 255``` KeyPress (rigth)<br>
 
<br>

## RawInput Joystick Input Examples
## Python
event.ev_type --> Absolute o Sync / event.code --> ABS_xxx
```
pip install inputs
```
file joystick.py 
```
import inputs

while True:
    events = inputs.get_gamepad()
    for event in events:
        # print(event.ev_type, event.code, event.state)

        # Buttons
        if event.code == 'BTN_SOUTH' and event.state == 1:
            print('A Button Press')
        if event.code == 'BTN_SOUTH' and event.state == 0:
            print('A Button Release')
        if event.code == 'BTN_NORTH' and event.state == 1:
            print('Y Button Press')
        if event.code == 'BTN_NORTH' and event.state == 0:
            print('Y Button Release')
        if event.code == 'BTN_WEST' and event.state == 1:
            print('X Button Press')
        if event.code == 'BTN_WEST' and event.state == 0:
            print('X Button Release')
        if event.code == 'BTN_EAST' and event.state == 1:
            print('B Button Press')
        if event.code == 'BTN_EAST' and event.state == 0:
            print('B Button Release')
        if event.code == 'BTN_TR' and event.state == 1:
            print('TR Press')
        if event.code == 'BTN_TR' and event.state == 0:
            print('TR Release')
        if event.code == 'BTN_TL' and event.state == 1:
            print('TL Press')
        if event.code == 'BTN_TL' and event.state == 0:
            print('TL Release')
        if event.code == 'BTN_START' and event.state == 1:
            print('SELECT Press')
        if event.code == 'BTN_START' and event.state == 0:
            print('SELECT Release')
        if event.code == 'BTN_SELECT' and event.state == 1:
            print('START Press')
        if event.code == 'BTN_SELECT' and event.state == 0:
            print('START Release')

        # Direction Button
   
```
<img  align="middle" width="32" height="32" src="https://raw.githubusercontent.com/carjavi/markdown-guide/master/img/python.svg"> [joystick.py](https://url.com)


<br>

more inf: <br>
https://pypi.org/project/inputs/ <br>
https://pypi.org/project/inputs/

<br>

## NodeJS 
```
Trabajando en esto!
```


<br>

---
Copyright &copy; 2022 [carjavi](https://github.com/carjavi). <br>
```www.instintodigital.net``` <br>
carjavi@hotmail.com <br>
<p align="center">
    <a href="https://instintodigital.net/" target="_blank"><img src="https://raw.githubusercontent.com/carjavi/joystick-code-windows/master/img/developer.png" height="100" alt="www.instintodigital.net"></a>
</p>