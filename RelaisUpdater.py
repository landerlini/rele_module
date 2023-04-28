"""
Software interface to the 8CH RELE MODULE developed at INFN Firenze.
(c) 2023 - INFN Firenze

Authors: Roberto Ciaranfi, Giovanni Passaleva, Lucio Anderlini
"""
import contextlib
from threading import Thread
import time

import ftd2xx as ftd


@contextlib.contextmanager
def ftd_connect(address: int = 0, mode: int = 0xff, enable: int = 0x01):
    driver = ftd.open(address)
    driver.setBitMode(mode, enable)
    try:
        yield driver
    finally:
        driver.close()


class RelaisUpdater (Thread):
    def __init__(self, refresh_period_seconds: float = 0.1, address: int = 0, mode: int = 0xff, enable: int = 0x01):
        self._conn_args = dict(address=address, mode=mode, enable=enable)
        self._current_status = None
        self._new_status = 0x0
        self.refresh_period_seconds = refresh_period_seconds
        self._running = True
        Thread.__init__(self)

    def kill(self):
        self._running = False
        self.join()

    def __getitem__(self, relais: int):
        return bool((self.status >> relais) & 0x01)

    def __setitem__(self, relais: int, value: bool):
        status = self._new_status
        if status is None:
            status = self._current_status

        if value:
            status |= 1 << relais
        else:
            status &= 0xff - (1 << relais)

        self._new_status = status

    def __str__ (self):
        return (
                f"Relais board #{self._conn_args['address']}: " +
                " ".join(["✅" if self[i] else "◼️" for i in range(8)])
        )

    @property
    def status(self):
        return self._current_status

    @status.setter
    def status(self, new_value: int):
        if self._new_status is not None:
            print ("WARNING! Updates are too frequent to be properly taken into account.")
        self._new_status = new_value

    def run(self):
        while self._running:
            time.sleep(self.refresh_period_seconds)
            if self._new_status is not None and self._new_status != self._current_status:
                with ftd_connect(**self._conn_args) as d:
                    d.write(chr(self._new_status))
                    self._current_status = self._new_status
                self._new_status = None





