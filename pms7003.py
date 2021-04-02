#!/usr/bin/env python3

from serial import Serial


class PMS7003:
    def __init__(self, port):
        self._frame_header = b'BM\x00\x1c'
        self._connection = Serial(port, timeout=0.1)  # open serial port at "9600,8,N,1", no timeout
        self._connection.reset_input_buffer()
        self._connection.reset_output_buffer()
        self.set_passive_mode()
        self._processed_data = {"pm010_std": None, "pm025_std": None, "pm100_std": None,
                                "pm010_atm": None, "pm025_atm": None, "pm100_atm": None,
                                "part003": None, "part005": None, "part010": None,
                                "part025": None, "part050": None, "part100": None}

    def __del__(self):
        self._connection.close()

    def _validate_frame(self):
        if sum(self._frame_header) + sum(self._raw_data) == self._checksum[0] * 256 + self._checksum[1]:
            return 1
        return 0

    def _read_frame_passive(self):
        cmd = b'\x42\x4d\xe2\x00\x00\x01\x71'
        self._connection.write(cmd)
        tmp_data = self._connection.read(32)
        self._raw_data = tmp_data[4:30]
        self._checksum = tmp_data[-2:]
        try:
            if self._validate_frame():
                return True
            else:
                return False
        except IndexError:
                return False

    def set_passive_mode(self):
        cmd = b'\x42\x4d\xe1\x00\x00\x01\x70'
        self._connection.write(cmd)
        x = self._connection.read(32)
        if x != b'\x42\x4d\x00\x04\xe1\x00\x01\x74':  # retry if answer frame is not correct
            self.set_passive_mode()

    def set_active_mode(self):
        pass

    def set_sleep_mode(self):
        pass

    def set_wakeup_mode(self):
        pass

    def read(self):
        if self._read_frame_passive():
            self._processed_data["pm010_std"] = self._raw_data[0] * 16 + self._raw_data[1]
            self._processed_data["pm025_std"] = self._raw_data[2] * 16 + self._raw_data[3]
            self._processed_data["pm100_std"] = self._raw_data[4] * 16 + self._raw_data[5]
            self._processed_data["pm010_atm"] = self._raw_data[6] * 16 + self._raw_data[7]
            self._processed_data["pm025_atm"] = self._raw_data[8] * 16 + self._raw_data[9]
            self._processed_data["pm100_atm"] = self._raw_data[10] * 16 + self._raw_data[11]
            self._processed_data["part003"] = self._raw_data[12] * 16 + self._raw_data[13]
            self._processed_data["part005"] = self._raw_data[14] * 16 + self._raw_data[15]
            self._processed_data["part010"] = self._raw_data[16] * 16 + self._raw_data[17]
            self._processed_data["part025"] = self._raw_data[18] * 16 + self._raw_data[19]
            self._processed_data["part050"] = self._raw_data[20] * 16 + self._raw_data[21]
            self._processed_data["part100"] = self._raw_data[22] * 16 + self._raw_data[23]
            return self._processed_data
        else:
            return None


if __name__ == "__main__":
    sensor = PMS7003('/dev/ttyUSB0')
    output = sensor.read()
    if output:
        print(output)
    else:
        print("Read error!")
