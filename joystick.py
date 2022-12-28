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
            

     
