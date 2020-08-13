import pendulum
from time import sleep
import keyboard

now = pendulum.now(tz="local")
START = pendulum.today(tz="local").add(hours=22) # 10 PM
END = pendulum.tomorrow(tz="local").add(hours=7) # 7 AM (can be changed according to your preferences)

# Test cases
# START = pendulum.now(tz="local").subtract(seconds=5)
# START = pendulum.now(tz="local").add(seconds=5)
# END = pendulum.now(tz="local").add(seconds=10)

wdPeriod = pendulum.period(START, END)

while(True):
    if now == START or now in wdPeriod:
        keyboard.press_and_release('ctrl+win+c')
        sleep(wdPeriod.remaining_seconds)
        keyboard.press_and_release('ctrl+win+c')
        now = pendulum.now(tz="local")
        pass
    sleep(1)
    now = pendulum.now(tz="local")
    # print(now.to_time_string(), end="\r") # Shows current time