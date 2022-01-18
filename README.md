# Home Assistant Thermal Comfort Icons
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)

Custom icon pack designed for [Thermal Comfort](https://github.com/dolezsa/thermal_comfort).

## Temperatures

### Heat Index
![Preview](./svg/thermometer-heat.svg) thermometer-heat<br />
![Preview](./svg/thermometer-fire.svg) thermometer-fire<br />

### Dew Point
![Preview](./svg/thermometer-water.svg) thermometer-water<br />
![Preview](./svg/thermometer-water-opacity.svg) thermometer-water-opacity<br />

### Frost Point
![Preview](./svg/thermometer-snow.svg) thermometer-snow<br />

### Simmer Index
![Preview](./svg/thermometer-sleep.svg) thermometer-sleep<br />
![Preview](./svg/thermometer-power-sleep.svg) thermometer-power-sleep<br />

## Perception

### Thermal Perception
![Preview](./svg/hand-thermometer.svg) hand-thermometer<br />
![Preview](./svg/home-thermometer-eye.svg) home-thermometer-eye<br />

### Simmer Zone
![Preview](./svg/hand-thermometer-power-sleep.svg) hand-thermometer-power-sleep<br />
![Preview](./svg/home-thermometer-eye-power-sleep.svg) home-thermometer-eye-power-sleep<br />

## Install

### HACS
Add this repo via HACS as a [custom repository](https://hacs.xyz/docs/faq/custom_repositories) and install.

### Manual
Copy the `hass-tc-icons.js` file into `<config>/www/` where `<config>` is your home-assistant config directory (the directory where your `configuration.yaml` resides).

Add the folowing to the `frontend` section of your `configuration.yaml`

```yaml
frontend:
  extra_module_url:
    - /local/hass-tc-icons.js
```

Or add the following to your lovelace configuration using the Raw Config editor under Configure UI or ui-lovelace.yaml if using YAML mode.

```yaml
resources:
  - type: js
    url: /local/hass-tc-icons.js
```

Restart home-assistant.

## Using
The icons uses the prefix `tc:`.

For thermal_comfort add a unique_id in the yaml config and set the icon per sensor through the frontend.

```yaml
sensor:
  - platform: thermal_comfort
    sensors:
      livingroom:
        friendly_name: Living Room
        temperature_sensor: sensor.temperature_livingroom
        humidity_sensor: sensor.humidity_livingroom
        unique_id: 8126740e-8e91-4e66-b902-58e13a9939a7
```

## FAQ
Q: The icon ain't showing, it's just white space where it should be. What's up with that?

A: Probably related to cache. Try opening your instance in a incognito/private Window and see if your icon shows then. If yes, it's cache related. If not, spellcheck.

## Thanks
Based on [hass-bha-icons](https://github.com/hulkhaugen/hass-bha-icons) from @hulkhaugen
