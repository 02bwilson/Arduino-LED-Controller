# Arduino LED Controller by Bryce W

# Python
import time
import serial


class LEDController:
    _VERSION_ = "1.0"

    def __init__(self):
        self.serial_connection = None
        self.continue_flag = True

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

        except serial.serialutil.SerialException:
            raise Exception("Error connecting to serial port {}!".format(serial_port))

    def send_stream(self, stream_dict):
        for stream_data in stream_dict['stream']:
            if not self.continue_flag:
                return
            if stream_data[2] == "PRE":
                time.sleep(stream_data[1])

            self.serial_connection.writelines(b'%b' % bytes(stream_data[0].encode('utf-8')))

            if stream_data[2] == "POST":
                time.sleep(stream_data[1])

        if stream_dict['repeat'] and self.continue_flag:
            self.send_stream(stream_dict)
        else:
            return
    def stop_stream(self):
        self.continue_flag = False


if __name__ == "__main__":
    controller = LEDController()
    stream_dict = {
        "stream": [["H", .5, "POST"]],
        "repeat": True
    }
    controller.stream(stream_dict=stream_dict, serial_port=3, setup_blink=False)
