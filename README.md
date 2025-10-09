# domoticz-ir-climate-controller
Python plugin for Domoticz to add Tasmota IR climate controller integration

# Prerequisites

- Domoticz 2022.1 or higher
- Make sure that your Domoticz supports Python plugins (https://www.domoticz.com/wiki/Using_Python_plugins)
- A Tasmota IR controller device is required.

  You can:
  - **Build your own IR sender** using an ESP device with an IR LED, following the official guide:  
    [https://tasmota.github.io/docs/IR-Remote/](https://tasmota.github.io/docs/IR-Remote/)
  
  - **Buy a ready-made device**, such as the [Athom Tasmota IR Controller](https://www.athom.tech/blank-1/tasmota-ir-controller)

## Installation

You can use [Plugins Manager](https://github.com/stas-demydiuk/domoticz-plugins-manager) for automatic installation or follow manual steps:

1. Clone repository into your domoticz plugins folder
```
cd domoticz/plugins
git clone https://github.com/szelessavalapitvany/domoticz-ir-climate-controller.git IR_climate_controller
```
2. Restart domoticz
3. Make sure that "Accept new Hardware Devices" is enabled in Domoticz settings
4. Go to "Hardware" page and add new item with type "Tasmota IR climate controller"
5. Set your Air conditioner type, Tasmota IR ip address

## Plugin update

1. Go to plugin folder and pull new version
```
cd domoticz/plugins/IR_climate_controller
git pull
```
2. Restart domoticz

Note: if you did any changes to plugin files and `git pull` command doesn't work for you anymore, you could stash all local changes using
```
git stash
```

## Plugin downgrade

1. Go to plugin folder and pull older version
```
cd domoticz/plugins/IR_climate_controller
git reset --hard 2550e9307d37755d192563638f615a6ab08f5a08
```
2. Restart domoticz or disable and re-enable plugin in 'Setup -> Hardware' (clearing browser cache might be necessary!)

