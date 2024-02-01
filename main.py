import random
import os
import subprocess
import time

count = subprocess.Popen(["timeout", "--preserve-status", "5", "tcpdump", "-i", "bluetooth0"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
initial = count.stdout.read().decode("utf-8").split("\n")[4].split(" ")[0]
time.sleep(10)
count2 = subprocess.Popen(["timeout", "--preserve-status", "5", "tcpdump", "-i", "bluetooth0"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
final = count2.stdout.read().decode("utf-8").split("\n")[4].split(" ")[0]
print(int(final) - int(initial))

with open("devices.txt", "a") as f:
    f.write("{ \"Time\": " + str(time.time()) + ", \"Count\": " + str(int(final) - int(initial)) + "},\n")
    f.close()