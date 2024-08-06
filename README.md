# TinkerBMS

BMS data stream reader, via RS485, CAN, and SMBus

## Why TinkerBMS?

There's already an excellent BMS reader - [dbus-serialbattery][dbus-serialbattery].
But it's runnable on SBCs like Raspberry Pi.
I'd like to do the same on any platform - PCs, microcontrollers, and SBCs.

* a reusable Python library
* [MicroPython](https://github.com/micropython/micropython) compatible for running on microcontrollers
* inherit the `Battery` abstract class of [dbus-serialbattery][dbus-serialbattery], making it easier to support more BMS protocols
* supporting more BMS protocols that [dbus-serialbattery][dbus-serialbattery] doesn't yet

## BMS Communication Protocols

| Battery  | Vendor                  | Protocol                                             |
| -------- | ----------------------- | ---------------------------------------------------- |
| 48NPFC50 | [MPINarada][mfr-narada] | [Shinwa BMS Protocol](./doc/protocol-shinwa-bms.pdf) |
| ZTT48100 | [Zhongtian][mfr-ztt]    | [Zhongtian BMS Protocol](./doc/protocol-ztt-bms.pdf) |

## Other Resources

* [dbus-serialbattery][dbus-serialbattery]
* [darkbyte-ru/shinwa-bms](https://github.com/darkbyte-ru/shinwa-bms)
* [ForrestFire0/GenericBMSArduino](https://github.com/ForrestFire0/GenericBMSArduino)

[dbus-serialbattery]: https://github.com/Louisvdw/dbus-serialbattery
[mfr-narada]: https://mpinarada.com/
[mfr-ztt]: https://www.zttgroup.com/
