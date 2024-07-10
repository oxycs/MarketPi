# MarketPi

## A program to plot the current capacity of the marketplace, inspired by [this post](https://matthew.science/posts/occupancy/).

To use, simply place these files onto a Raspberry Pi with Bluetooth. Before starting the service, the Pi needs to be configured to start listening to nearby devices, which can be done with the command `bluetoothctl scan on &`.

Make sure to install the `mysql-connector-python` package with `python3 -m pip install mysql-connector-python`.

Then add the following to your crontab:

```
* * * * * /usr/bin/flock -n /tmp/fcjmain.lockfile /usr/bin/python3 ~/main.py
```
You will also need to install `tcpdump`.

You can then plot the data with Grafana, or any other plotting software.

![Grafana Graph](image-2.png)

See the current installation at https://dining.csc.oxy.edu for the dining hall capacity at Occidental College.