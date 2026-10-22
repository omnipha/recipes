# Security Lab & Pentest Toolkit Recipe

A mobile pentest toolkit for wireless audits, Bluetooth/NFC inspection, and USB gadget experiments.

## Features

- **Wireless tools**: `tcpdump`, `nmap`, `tshark`, `aircrack-ng`, `wireless-tools`.
- **Bluetooth & NFC**: BlueZ utilities and NFC reading tools where supported by hardware.
- **Console UI**: Runs a direct terminal UI on the phone display or over SSH.

## Caveats

- Many phone Wi-Fi chips do not support monitor mode or packet injection on stock drivers. External USB OTG wireless adapters are recommended for advanced audits.

## Configuration options (`omnipha.yaml`)

```yaml
recipes:
  - id: security-lab
    config:
      UI_MODE: "console"
      WIFI_INTERFACE: "wlan0"
```
