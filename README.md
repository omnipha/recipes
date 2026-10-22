# Omnipha Recipes

Composable software recipes and application modules for Omnipha Linux phones.

## Concept

Omnipha splits phone bring-up from phone applications:

1. **Hardware / Base OS (`omnipha/ports`, `omnipha/images`)**:
   Kernel, hardware adaptation, firmware, minimal Alpine Linux, SSH key injection, container runtime.
2. **Recipes (`omnipha/recipes`)**:
   Modular software packages, services, and configs that turn the phone into a dedicated appliance (Home Assistant sensor unit, AI agent host, 3D printer controller, etc.).

Instead of building hundreds of monolithic images for every device-and-use-case combination, devices boot a clean base image. The desired recipes are applied at image build time or via `omnipha.yaml` during first boot.

## How a Recipe works

Every recipe is a self-contained directory under `recipes/<id>/`:
- `recipe.yaml`: metadata, hardware requirements, alpine packages, container definitions, ports, and environment variables.
- `docker-compose.yaml` (optional): containerized services.
- `setup.sh` (optional): post-install host configuration.
- `README.md`: description, required hardware, configuration options.

See [SPEC.md](SPEC.md) for the complete recipe specification.

## Available Recipes

| Recipe | Description | Display | Network | Status |
|---|---|---|---|---|
| [`homeassistant-satellite`](recipes/homeassistant-satellite/) | MQTT sensor bridge (battery, light, sensors), camera RTSP, optional dashboard kiosk | Optional | Wi-Fi / LAN | Draft / Skeleton |
| [`agent-host`](recipes/agent-host/) | AI coding agent environment (OpenClaw, Claude Code, Node, Python, tmux) | Headless | Wi-Fi / LAN | Draft / Skeleton |
| [`3dprint-klipper`](recipes/3dprint-klipper/) | Klipper, Moonraker, Mainsail web UI and camera streamer | Optional | Wi-Fi / LAN | Draft / Skeleton |
| [`security-lab`](recipes/security-lab/) | Pentest tools (Wi-Fi, Bluetooth, NFC inspection, USB gadget) | Console UI | Wi-Fi / USB | Draft / Skeleton |

## Configuration (`omnipha.yaml`)

Users and agents declare which recipes to activate via an `omnipha.yaml` file placed in the boot partition or data volume:

```yaml
version: 1
device: google-sargo
hostname: phone-ha-01

wifi:
  ssid: "MyNetwork"
  psk: "secret"

ssh_authorized_keys:
  - "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI..."

recipes:
  - id: homeassistant-satellite
    config:
      mqtt_broker: "192.168.1.50"
      dashboard_url: "http://192.168.1.50:8123"
  - id: agent-host
```

## Contributing

See [AGENTS.md](AGENTS.md). Anyone (human or AI agent) can add a recipe by creating a directory under `recipes/<id>/` and opening a pull request.
