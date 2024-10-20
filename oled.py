from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime

# Initialize I2C on pins GP8 (sda=Pin(16)) and GP9 (scl=Pin(17)) with a frequency of 200,000 Hz
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)

# Create an SSD1306 OLED object
oled = SSD1306_I2C(96, 96, i2c)  # Adjust the display width and height based on your OLED specifications

# Clear the display
oled.fill(0)
oled.show()

# Display a diagonal line
oled.line(0, 0, 127, 63, 1)
oled.show()
utime.sleep(2)

# Display a rectangle
oled.rect(10, 10, 50, 30, 1)
oled.show()
utime.sleep(2)

# Display a filled rectangle
oled.fill_rect(70, 10, 50, 30, 1)
oled.show()
utime.sleep(2)

# Display a circle
oled.circle(80, 40, 20, 1)
oled.show()
utime.sleep(2)

# Display a filled circle
oled.fill_circle(40, 40, 20, 1)
oled.show()
utime.sleep(2)

# Clear the display
oled.fill(0)
oled.show()
