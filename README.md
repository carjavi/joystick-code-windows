<p align="center"><img src="https://raw.githubusercontent.com/carjavi/joystick-code-windows/master/img/joystick.png" height="200" alt=" " /></p>
<h1 align="center">Joystick Code Windows</h1> 
<h4 align="right">Dic 22</h4>

<img src="https://img.shields.io/badge/OS-Windows%2011-blue">
<img src="https://img.shields.io/badge/Node%20-V18.7.0-green">
<img src="https://img.shields.io/badge/Python%20-V3.9.2-orange">

<br>


## Programming to Receive Joystick Input in Windows

## Displaying Physical Buttons
GameSir T4 Pro Joystick

<img src="https://raw.githubusercontent.com/carjavi/joystick-code-windows/master/img/GameSir-T4-Pro.png" height="100" alt="">
<img src="https://raw.githubusercontent.com/carjavi/joystick-code-windows/master/img/GameSir-T4-Pro2.png" height="100" alt="">

## RawInput Joystick Input Examples

## Python
```
import inputs

while True:
    events = inputs.get_gamepad()
    for event in events:
        print(event.ev_type, event.code, event.state)
        if event.code == 'BTN_SOUTH' and event.state == 1:
            print('Boton X')
```

## NodeJS 

---
Copyright &copy; 2022 [carjavi](https://github.com/carjavi). <br>
```www.instintodigital.net``` <br>
carjavi@hotmail.com <br>
<p align="center">
    <a href="https://instintodigital.net/" target="_blank"><img src="https://raw.githubusercontent.com/carjavi/joystick-code-windows/master/img/developer.png" height="100" alt="www.instintodigital.net"></a>
</p>