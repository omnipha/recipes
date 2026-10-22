# 3D Printer Host (Klipper) Recipe

Controls a 3D printer over USB OTG using Klipper, Moonraker, and Mainsail, with webcam streaming.

## Features

- **Klipper & Moonraker**: Low-latency G-code execution over USB serial (`/dev/ttyACM0` or `/dev/ttyUSB0`).
- **Mainsail Web UI**: Accessible on the local network on port 80.
- **Webcam Stream**: Phone camera exposed as an MJPEG or H.264 stream for live print monitoring.
- **Display Status (optional)**: Direct touchscreen control or KlipperScreen on the phone display.

## Configuration options (`omnipha.yaml`)

```yaml
recipes:
  - id: 3dprint-klipper
    config:
      PRINTER_PORT: "/dev/ttyACM0"
      WEB_PORT: 80
      STREAM_FRAMERATE: 15
```
