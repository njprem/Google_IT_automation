import subprocess


process = subprocess.Popen(['sleep', '5'])

message_1 = "The process is running in the background..."

import time
time.sleep(2)

if process.poll() is None:
    message_2 = "The process is still running."
else:
    message_2 = "The process has finished."

print(message_1, message_2)