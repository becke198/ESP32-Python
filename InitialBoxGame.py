from machine import Pin, SoftI2C
import ssd1306
from time import sleep

# Initialize the OLED display
i2c = SoftI2C(scl=Pin(35), sda=Pin(34))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Configure PIN 2 as output for the LED
led = Pin(2, Pin.OUT)

# Configure PIN 5 as an input with an internal pull-up resistor
button = Pin(5, Pin.IN, Pin.PULL_UP)

# Initialize game variables
rect_x = 48
rect_y = oled_height - 32
goal_y = 10  # Position of the goal line
timer = 20  # Countdown timer (seconds)

# Function to check button press (non-blocking)
def is_button_pressed():
    if button.value() == 0:  # Button pressed (active low)
        sleep(0.2)  # Debounce delay
        return True
    return False

# Function to display the game screen
def update_screen():
    oled.fill(0)  # Clear the screen

    # Draw the goal line
    oled.hline(0, goal_y, oled_width, 1)

    # Draw the rectangle
    oled.fill_rect(rect_x, rect_y, 32, 32, 1)

    # Display the timer
    oled.text(f"Time: {timer}", 0, 0, 1)

    # Update the display
    oled.show()

# Main game loop
def game_loop():
    global rect_y, timer

    while timer > 0:
        if is_button_pressed():
            # Move the rectangle upward
            rect_y -= 10
            if rect_y < 0:
                rect_y = 0  # Prevent it from going off the screen

        # Check if the rectangle has reached the goal
        if rect_y <= goal_y:
            oled.fill(0)
            oled.text("YOU WIN!", 32, 24, 1)
            oled.show()
            return  # Exit the game loop

        # Update the screen
        update_screen()

        # Countdown timer
        sleep(1)
        timer -= 1

    # Game over if the timer runs out
    oled.fill(0)
    oled.text("GAME OVER", 24, 24, 1)
    oled.show()

# Start the game
game_loop()
