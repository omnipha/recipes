# Home Assistant Satellite Recipe

Turns an Omnipha phone into an integrated Home Assistant sensor bridge and optional wall panel display.

## Capabilities

- **Telemetry**: Exposes built-in phone battery status, battery temperature, ambient light, accelerometer, and magnetometer over MQTT.
- **Camera stream**: Streams phone camera feed locally via RTSP or WebRTC for Frigate / go2rtc.
- **Kiosk display (optional)**: Launches a hardware-accelerated full-screen browser pointing to a Lovelace dashboard on VT7.

## Configuration options (`omnipha.yaml`)

```yaml
recipes:
  - id: homeassistant-satellite
    config:
      MQTT_BROKER: "192.168.1.50"
      MQTT_PORT: 1883
      MQTT_TOPIC_PREFIX: "omnipha/livingroom"
      DASHBOARD_URL: "http://192.168.1.50:8123/lovelace-wall"
      CAMERA_STREAM: true
```
