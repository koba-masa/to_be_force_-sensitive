import board
import digitalio
import time

class SampleKeyboard:
  SWITCH = board.GP16
  LED = board.GP25

  def execute(self):
    self.switch = digitalio.DigitalInOut(self.SWITCH)
    self.switch.switch_to_input(pull=digitalio.Pull.UP)
    self.led = digitalio.DigitalInOut(self.LED)
    self.led.direction = digitalio.Direction.OUTPUT

    while True:
      if self.switch.value == False:
        self.led.value = True
        time.sleep(0.1)
        self.led.value = False

      time.sleep(0.1)

SampleKeyboard().execute()
