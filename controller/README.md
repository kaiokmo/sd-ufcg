# Running Monitor

Update controller.cfg, each section is an address to prometheus server.

Example:

```
[rivendell]
address: <ip>:<port>

[gondor]
address: <ip>:<port>
```

The redis address to update metrics goes as sdtin:

```
python controller.py <redis-ip> <redis-port>
```