# Recipe Specification (`SPEC.md`)

This document defines the structure, schema, and lifecycle of an Omnipha Recipe.

## Architecture

Omnipha separates device hardware enablement from application setups:

```
[ Device Layer ]   omnipha/ports   (kernel, firmware, drivers, minimal Alpine Linux)
         │
[ Base Image ]     omnipha/images  (boots headless with SSH key, container runtime)
         │
[ Recipe Layer ]   omnipha/recipes (modular services, docker-compose, configs, UI)
```

A recipe can be applied in two ways:
1. **Pre-baked**: Selected at image build time via `builder --recipe <id>`.
2. **First-boot**: Selected by user or agent via `omnipha.yaml` placed in the boot partition or data filesystem.

## Recipe directory layout

Every recipe lives in `recipes/<id>/`:

```
recipes/<id>/
├── recipe.yaml           # Metadata, requirements, environment, packages
├── README.md             # Usage documentation, hardware requirements, options
├── docker-compose.yaml   # (Optional) Container stack
├── setup.sh              # (Optional) Post-install host hook
└── config/               # (Optional) Template config files mounted into services
```

## `recipe.yaml` Schema

```yaml
id: homeassistant-satellite
name: "Home Assistant Satellite"
description: "Turns the phone into a wall-mounted sensor and camera satellite for Home Assistant."
version: "0.1.0"
maintainer: "omnipha"

# Hardware requirements and optional enhancements
requirements:
  min_ram_mb: 2048
  min_storage_mb: 4096
  display: optional     # required | optional | none
  touch: optional       # required | optional | none
  camera: optional      # required | optional | none
  battery: optional     # required | optional | none
  wifi: required        # required | optional | none
  bluetooth: optional   # required | optional | none

# Alpine packages installed directly on the host (if any)
packages:
  - mosquitto-clients
  - v4l-utils

# Environment variables with defaults that can be overridden in omnipha.yaml
config:
  MQTT_BROKER:
    type: string
    required: true
    description: "IP address or hostname of the Home Assistant / MQTT broker"
  MQTT_PORT:
    type: integer
    default: 1883
  DASHBOARD_URL:
    type: string
    required: false
    description: "URL loaded by the full-screen kiosk browser on the phone display"
  CAMERA_STREAM:
    type: boolean
    default: true
    description: "Expose phone camera as local RTSP or WebRTC stream"

# Services managed by the recipe
services:
  compose_file: "docker-compose.yaml"   # relative path if containers are used
  host_services: []                     # OpenRC services to enable, e.g. ["sshd"]

# First-boot hook (executed once during first boot provisioning)
hooks:
  first_boot: "setup.sh"
```

## The `omnipha.yaml` Configuration Contract

On first boot, the Omnipha first-boot engine looks for `/boot/omnipha.yaml` or `/etc/omnipha.yaml`:

```yaml
version: 1
hostname: "phone-ha-livingroom"
ssh_authorized_keys:
  - "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5..."

wifi:
  ssid: "MyHomeWiFi"
  psk: "supersecret"

recipes:
  - id: homeassistant-satellite
    config:
      MQTT_BROKER: "192.168.1.100"
      DASHBOARD_URL: "http://192.168.1.100:8123/lovelace-wall"
```

### First-boot Execution Flow:
1. Network bring-up (connects to Wi-Fi if specified).
2. SSH key injection into `/root/.ssh/authorized_keys` and default user.
3. For each recipe in `recipes`:
   - Checks hardware requirements against `/etc/omnipha/device.yaml`. Warns if optional parts are missing, halts recipe if required parts are missing.
   - Installs listed Alpine packages (`apk add`).
   - Renders environment variables into `/etc/omnipha/recipes/<id>.env`.
   - Runs `setup.sh` hook if present.
   - Starts container stack via `docker compose -f docker-compose.yaml up -d` if present.
4. Marks provisioning complete in `/var/lib/omnipha/provisioned`.
