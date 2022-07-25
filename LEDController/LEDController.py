# Arduino LED Controller by Bryce W

# Python
import time
import serial


class LEDController:
    _VERSION_ = "1.0"

    def __init__(self):
        self.serial_connection = None
        pass

    def stream(self, stream_dict, serial_port=None, setup_blink=True):
        """
        Stream Dict format
        {
            "stream": [[<H/L>, <Timeout>, <PRE/POST>], ...]
                H/L: For led to be high or low
                PRE/POST: Determines if timeout will occur before or after the LED action is preformed.
                Timeout: Time either pre- / post-LED change that is waited.
            "repeat" : True/False
        }
        """
        if serial_port is None:
            raise Exception("No serial given!")

        try:
            self.serial_connection = serial.Serial('COM{}'.format(serial_port, 9600))
            if setup_blink:
                for i in range(0, 5):
                    self.serial_connection.write(b'H')
                    time.sleep(.2)
                time.sleep(.25)
            self.send_stream(stream_dict)

        except Exception as e:
            print(e)
            pass

    def send_stream(self, stream_dict):
        for stream_data in stream_dict['stream']:
            if stream_data[2] == "PRE":
                time.sleep(stream_data[1])
            self.serial_connection.writelines(b'%b' % bytes(stream_data[0].encode('utf-8')))

            if stream_data[2] == "POST":
                time.sleep(stream_data[1])

        if stream_dict['repeat']:
            self.send_stream(stream_dict)


if __name__ == "__main__":
    controller = LEDController()
    stream_dict = {
        "stream": [["H", 1, "POST"], ["H", .5, "PRE"]],
        "repeat": True
    }
    controller.stream(stream_dict=stream_dict, serial_port=3)
