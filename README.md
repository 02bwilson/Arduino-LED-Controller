# Arduino LED Controller

Arduino LED Controller is a simple LED Controller that works by sending serial signals to an Arduino. 

## Installation

Clone the repository, and copy the needed files to your project. 

## Usage

```python
from LEDController import LEDController

# Sends your LED Stream
controller = LEDController()
stream_dict = {
    "stream": [["H", 1, "POST"], ["H", .5, "PRE"]],
    "repeat": True
}
controller.stream(stream_dict=stream_dict, serial_port=3, setup_blink=True)
'''
Parameters:
    stream_dict: The dict of the stream to send to the arduino.
    serial_port: Address of the COM port the Arduino is connected to
    setup_blink: Enable/Disbale blinking when conntion is established to the Arduino
'''


```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[cc4.0](https://creativecommons.org/licenses/by/4.0/)
