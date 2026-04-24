
import robot_hat
import time

try:
    from robot_hat import SunfounderPWM
    red_led = SunfounderPWM("P24")
    green_led = SunfounderPWM("P25")
except ImportError:
    from robot_hat import Pin
    red_led = Pin("P24")
    green_led = Pin("P25")

def run_smart_demo():
    print("--- Smart AI Irrigation System Active ---")
    # Red LED ON (Needs Water)
    red_led.value(1)
    time.sleep(2)
    red_led.value(0)
    
    # Green LED ON (Healthy)
    green_led.value(1)
    time.sleep(2)
    green_led.value(0)

if __name__ == "__main__":
    run_smart_demo()

