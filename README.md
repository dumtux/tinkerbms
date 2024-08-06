# tinkerBMS

BMS data stream reader, via RS485, CAN, and SMBus

## BMS Communication Protocols

| Battery  | Vendor                  | Protocol                                             |
| -------- | ----------------------- | ---------------------------------------------------- |
| 48NPFC50 | [MPINarada](mfr-narada) | [Shinwa BMS Protocol](./doc/protocol-shinwa-bms.pdf) |
| ZTT48100 | [Zhongtian](mfr-ztt)    | [Zhongtian BMS Protocol](./doc/protocol-ztt-bms.pdf) |

## Other Resources

* [dbus-serialbattery](dbus-serialbattery)
* [darkbyte-ru/shinwa-bms](https://github.com/darkbyte-ru/shinwa-bms)
* [ForrestFire0/GenericBMSArduino](https://github.com/ForrestFire0/GenericBMSArduino)

[dbus-serialbattery]: https://github.com/Louisvdw/dbus-serialbattery
[mfr-narada]: https://mpinarada.com/
[mfr-ztt]: https://www.zttgroup.com/
