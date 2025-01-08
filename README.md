# ESP32-Python
This respository compiles all of my coding designs on the ESP 32 MicroPython Device.

# OLED-Based Interactive Game -- INITIAL BOX GAME

This project is an interactive game built using a microcontroller, an OLED display, and a push button. The game involves moving a rectangle upward by pressing a button, with the goal of reaching a goal line before the timer runs out.

---

## Components Used
1. **Microcontroller**: Compatible with MicroPython (e.g., ESP32, ESP8266).
2. **OLED Display**: 128x64 pixels, connected via I2C.
3. **Push Button**: Configured with an internal pull-up resistor.
4. **LED**: (Optional) connected to pin 2 for additional functionality.

---

## How It Works
- **Objective**: Move the rectangle to the goal line (`goal_y`) within the countdown timer's duration.
- **Button Input**: Pressing the button moves the rectangle upward.
- **Timer**: The game runs for 20 seconds or until the goal is reached.
- **Feedback**:
  - **"YOU WIN!"**: Displayed if the rectangle reaches the goal line.
  - **"GAME OVER"**: Displayed if the timer runs out before reaching the goal.

---

## Features
1. **Real-Time Interaction**: Button press moves the rectangle in real time.
2. **Visual Feedback**: Flashing the screen confirms button presses.
3. **Clear Game States**: Displays "YOU WIN!" or "GAME OVER" based on the result.
4. **Debouncing**: Prevents multiple detections from a single button press.

---

## Code Description

### Modules and Initialization
- **`machine`**: Manages hardware interactions like pins and I2C.
- **`ssd1306`**: Driver for the OLED display.
- **`time`**: Provides delay functionality.

### OLED Initialization
```python
i2c = SoftI2C(scl=Pin(35), sda=Pin(34))
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)



