"""
Tasmota IR climate controller python plugin for Domoticz
Author: szelessavmuhely.hu,
Version: 1.1.0 (september 10, 2025) 

<plugin key="ICC_IKV" name="IR climate controller _ Tasmota IR klima vezérlő" author="szelessavmuhely.hu" version="1.0.0">
	<description>
		<h2>IR climate controller _ Tasmota IR klima vezérlő</h2><br/>
		<br/>
		IR-eszközzel vezérelhető plugin, amely lehetővé teszi Wi-Fi nélküli, IR-es klímák távoli vezérlését Domoticz-ból. / Tasmota IR device control plugin that allows remote control of Wi-Fi-free, IR air conditioners from Domoticz.
		<br/>
		<br/>
	</description>
	<params>
		<param field="Address" label="Domoticz IP Address" width="200px" required="true" default="127.0.0.1"/>
		<param field="Port" label="Port" width="40px" required="true" default="8080"/>
		<param field="Username" label="Username" width="200px" required="false" default=""/>
		<param field="Password" label="Password" width="200px" required="false" default=""/>
		<param field="Mode1" label="Air conditioner type / Klíma típusa" width="200px">
			<options>
				<option label="Egyéb / Auto" value="AUTO" default="true" />
				<option label="AIRTON" value="AIRTON" />
				<option label="AIRWELL" value="AIRWELL" />
				<option label="AIWA" value="AIWA_RC_T501" />
				<option label="AMCOR" value="AMCOR" />
				<option label="ARGO" value="ARGO" />
				<option label="ARRIS" value="ARRIS" />
				<option label="BOSCH144" value="BOSCH144" />
				<option label="BOSE" value="BOSE" />
				<option label="CARRIER" value="CARRIER_AC" />
				<option label="CARRIER 128" value="CARRIER_AC128" />
				<option label="CARRIER 40" value="CARRIER_AC40" />
				<option label="CARRIER 64" value="CARRIER_AC64" />
				<option label="CARRIER 84" value="CARRIER_AC84" />
				<option label="CLIMABUTLER" value="CLIMABUTLER" />
				<option label="COOLIX" value="COOLIX" />
				<option label="COOLIX 48" value="COOLIX48" />
				<option label="CORONA" value="CORONA_AC" />
				<option label="DAIKIN" value="DAIKIN" />
				<option label="DAIKIN 128" value="DAIKIN128" />
				<option label="DAIKIN 152" value="DAIKIN152" />
				<option label="DAIKIN 160" value="DAIKIN160" />
				<option label="DAIKIN 176" value="DAIKIN176" />
				<option label="DAIKIN 2" value="DAIKIN2" />
				<option label="DAIKIN 200" value="DAIKIN200" />
				<option label="DAIKIN 216" value="DAIKIN216" />
				<option label="DAIKIN 312" value="DAIKIN312" />
				<option label="DAIKIN 64" value="DAIKIN64" />
				<option label="DELONGHI" value="DELONGHI_AC" />
				<option label="DENON" value="DENON" />
				<option label="DISH" value="DISH" />
				<option label="DOSHISHA" value="DOSHISHA" />
				<option label="ECOCLIM" value="ECOCLIM" />
				<option label="ELECTRA" value="ELECTRA_AC" />
				<option label="ELITESCREENS" value="ELITESCREENS" />
				<option label="EPSON" value="EPSON" />
				<option label="FUJITSU" value="FUJITSU_AC" />
				<option label="GICABLE" value="GICABLE" />
				<option label="GOODWEATHER" value="GOODWEATHER" />
				<option label="GORENJE" value="GORENJE" />
				<option label="GREE" value="GREE" />
				<option label="HAIER" value="HAIER_AC" />
				<option label="HAIER 160" value="HAIER_AC160" />
				<option label="HAIER 176" value="HAIER_AC176" />
				<option label="HAIER YRW02" value="HAIER_AC_YRW02" />
				<option label="HITACHI" value="HITACHI_AC" />
				<option label="HITACHI 1" value="HITACHI_AC1" />
				<option label="HITACHI 2" value="HITACHI_AC2" />
				<option label="HITACHI 264" value="HITACHI_AC264" />
				<option label="HITACHI 296" value="HITACHI_AC296" />
				<option label="HITACHI 3" value="HITACHI_AC3" />
				<option label="HITACHI 344" value="HITACHI_AC344" />
				<option label="HITACHI 424" value="HITACHI_AC424" />
				<option label="INAX" value="INAX" />
				<option label="JVC" value="JVC" />
				<option label="KELON" value="KELON" />
				<option label="KELON 168" value="KELON168" />
				<option label="KELVINATOR" value="KELVINATOR" />
				<option label="LASERTAG" value="LASERTAG" />
				<option label="LEGOPF" value="LEGOPF" />
				<option label="LG" value="LG" />
				<option label="LG 2" value="LG2" />
				<option label="LUTRON" value="LUTRON" />
				<option label="MAGIQUEST" value="MAGIQUEST" />
				<option label="METZ" value="METZ" />
				<option label="MIDEA" value="MIDEA" />
				<option label="MIDEA 24" value="MIDEA24" />
				<option label="MILESTAG2" value="MILESTAG2" />
				<option label="MIRAGE" value="MIRAGE" />
				<option label="MITSUBISHI" value="MITSUBISHI" />
				<option label="MITSUBISHI 112" value="MITSUBISHI112" />
				<option label="MITSUBISHI 136" value="MITSUBISHI136" />
				<option label="MITSUBISHI 2" value="MITSUBISHI2" />
				<option label="MITSUBISHI AC" value="MITSUBISHI_AC" />
				<option label="MITSUBISHI HEAVY 152" value="MITSUBISHI_HEAVY_152" />
				<option label="MITSUBISHI HEAVY 88" value="MITSUBISHI_HEAVY_88" />
				<option label="MULTIBRACKETS" value="MULTIBRACKETS" />
				<option label="MWM" value="MWM" />
				<option label="NEC" value="NEC" />
				<option label="NEC LIKE" value="NEC_LIKE" />
				<option label="NEOCLIMA" value="NEOCLIMA" />
				<option label="NIKAI" value="NIKAI" />
				<option label="PANASONIC" value="PANASONIC" />
				<option label="PANASONIC AC" value="PANASONIC_AC" />
				<option label="PANASONIC AC 32" value="PANASONIC_AC32" />
				<option label="PIONEER" value="PIONEER" />
				<option label="RC5" value="RC5" />
				<option label="RC5X" value="RC5X" />
				<option label="RC6" value="RC6" />
				<option label="RCMM" value="RCMM" />
				<option label="RHOSS" value="RHOSS" />
				<option label="SAMSUNG" value="SAMSUNG" />
				<option label="SAMSUNG 36" value="SAMSUNG36" />
				<option label="SAMSUNG AC" value="SAMSUNG_AC" />
				<option label="SANYO" value="SANYO" />
				<option label="SANYO AC" value="SANYO_AC" />
				<option label="SANYO AC 152" value="SANYO_AC152" />
				<option label="SANYO AC 88" value="SANYO_AC88" />
				<option label="SANYO LC7461" value="SANYO_LC7461" />
				<option label="SHARP" value="SHARP" />
				<option label="SHARP AC" value="SHARP_AC" />
				<option label="SONY" value="SONY" />
				<option label="SYMPHONY" value="SYMPHONY" />
				<option label="TCL 112AC" value="TCL112AC" />
				<option label="TCL 96AC" value="TCL96AC" />
				<option label="TECHNIBEL AC" value="TECHNIBEL_AC" />
				<option label="TECO" value="TECO" />
				<option label="TEKNOPOINT" value="TEKNOPOINT" />
				<option label="TOSHIBA AC" value="TOSHIBA_AC" />
				<option label="TOTO" value="TOTO" />
				<option label="TRANSCOLD" value="TRANSCOLD" />
				<option label="TROTEC" value="TROTEC" />
				<option label="TROTEC 3550" value="TROTEC_3550" />
				<option label="TRUMA" value="TRUMA" />
				<option label="VESTEL AC" value="VESTEL_AC" />
				<option label="VOLTAS" value="VOLTAS" />
				<option label="WHIRLPOOL AC" value="WHIRLPOOL_AC" />
				<option label="WHYNTER" value="WHYNTER" />
				<option label="WOWWEE" value="WOWWEE" />
				<option label="XMP" value="XMP" />
				<option label="YORK" value="YORK" />
				<option label="ZEPEAL" value="ZEPEAL" />
			</options>
		</param>
		<param field="Mode2" label="Tasmota IR ip address /  Tasmota IR ip címe" width="100px" required="false" default=""/>
		<param field="Mode3" label="Logging Level" width="200px">
			<options>
				<option label="Normal" value="Normal"  default="true"/>
				<option label="Verbose" value="Verbose"/>
				<option label="Debug - Python Only" value="2"/>
				<option label="Debug - Basic" value="62"/>
				<option label="Debug - Basic+Messages" value="126"/>
				<option label="Debug - Connections Only" value="16"/>
				<option label="Debug - Connections+Queue" value="144"/>
				<option label="Debug - All" value="-1"/>
			</options>
		</param>
	</params>
</plugin>
"""
import Domoticz
import json
from urllib import parse, request
from datetime import datetime, timedelta
import time
import math
import base64
import itertools
import re
import os
import heapq

class deviceparam:

	def __init__(self, unit, nvalue, svalue):
		self.unit = unit
		self.nvalue = nvalue
		self.svalue = svalue

class switchparam:

	def __init__(self, idx, command):
		self.idx = idx
		self.command = command

class TranslationLoader:

	def __init__(self, language="en"):
		self.translations = self.load_translations(language)
		if not self.translations:
			Domoticz.Debug("An error occurred while loading the translations!")
			self.translations = self.load_translations("en") 

	def load_translations(self, language):
		file_path = os.path.join(Parameters["HomeFolder"], f'icc_translate_{language}.json')
		try:
			with open(file_path, 'r', encoding='utf-8') as file:
				return json.load(file)
		except (FileNotFoundError, json.JSONDecodeError) as e:
			Domoticz.Debug(f"Error loading the file '{file_path}': {e}")
			return {} 

	def t(self, text):
		return self.translations.get(text, text)  # If there is no translation, it returns with the original text

class BasePlugin:

	def __init__(self):

		self.debug = True
		self.AC_command = []
		self.AC_last_command_time = None
		self.AC_vendor = []
		self.AC_ipaddress = []
		self.AC_power = False
		self.AC_temp = 22.0
		self.AC_mode = None
		self.AC_fan_rate = None
		self.AC_vertical_air = None
		self.AC_horizontal_air = None
		self.AC_silent_mode = None
		self.AC_turbo_mode = None
		self.AC_economy_mode = None
		self.AC_filter = None
		self.AC_cleaning = None
		self.AC_sound_signal = None
		self.AC_status_mode = None
		self.AC_ir_resend = None
		self.encoded_json = None
		return


	def onStart(self):

		self.location = Settings["Location"].split(";")
		
		tl = TranslationLoader(Parameters["Language"])
		
		# állítsa be a megfelelő naplózási szintet
		try:
			debuglevel = int(Parameters["Mode3"])
		except ValueError:
			debuglevel = 0
			self.loglevel = Parameters["Mode3"]
		if debuglevel != 0:
			self.debug = True
			Domoticz.Debugging(debuglevel)
			DumpConfigToLog()
			self.loglevel = "Verbose"
		else:
			self.debug = False
			Domoticz.Debugging(0)

		devicecreated = []
		if 1 not in Devices:
			Options = {"LevelActions": "||",
				"LevelNames": tl.t("Off|On"),
				"LevelOffHidden": "false",
				"SelectorStyle": "0"}
			Domoticz.Device(Name=tl.t("Power"), Unit=1, TypeName="Selector Switch", Image=9, Options=Options, Used=1).Create()
			devicecreated.append(deviceparam(1, 0, "0"))
			self.addfavorite(Devices[1].ID)
		if 2 not in Devices:
			Domoticz.Device(Name= tl.t("Target temperature"), Unit=2, Type=242, Subtype=1, Used=1).Create()
			devicecreated.append(deviceparam(2, 0, "24"))
			self.addfavorite(Devices[2].ID)
		if 3 not in Devices:
			Options = {"LevelActions": "||",
				"LevelNames": tl.t("Off|Auto|Cool|Heat|Fan|Dry"),
				"LevelOffHidden": "true",
				"SelectorStyle": "1"}
			Domoticz.Device(Name=tl.t("Mode"), Unit=3, TypeName="Selector Switch", Image=7, Options=Options, Used=1).Create()
			devicecreated.append(deviceparam(3, 0, "10"))
			self.addfavorite(Devices[3].ID)
		if 4 not in Devices:
			Options = {"LevelActions": "||",
				"LevelNames": tl.t("Off|Auto|Low|Medium|High|Max"),
				"LevelOffHidden": "true",
				"SelectorStyle": "1"}
			Domoticz.Device(Name=tl.t("Fan Rate"), Unit=4, TypeName="Selector Switch", Image=7, Options=Options, Used=1).Create()
			devicecreated.append(deviceparam(4, 0, "10"))
		if 5 not in Devices:
			Options = {"LevelActions": "||",
				"LevelNames": tl.t("Off|On"),
				"LevelOffHidden": "false",
				"SelectorStyle": "0"}
			Domoticz.Device(Name=tl.t("Vertical air flow"), Unit=5, TypeName="Selector Switch", Image=7, Options=Options, Used=1).Create()
			devicecreated.append(deviceparam(5, 0, "0"))
		if 6 not in Devices:
			Options = {"LevelActions": "||",
				"LevelNames": tl.t("Off|On"),
				"LevelOffHidden": "false",
				"SelectorStyle": "0"}
			Domoticz.Device(Name=tl.t("Horizontal air flow"), Unit=6, TypeName="Selector Switch", Image=7, Options=Options, Used=1).Create()
			devicecreated.append(deviceparam(6, 0, "0"))
		if 7 not in Devices:
			Options = {"LevelActions": "||",
				"LevelNames": tl.t("Off|On"),
				"LevelOffHidden": "false",
				"SelectorStyle": "0"}
			Domoticz.Device(Name=tl.t("Silent mode"), Unit=7, TypeName="Selector Switch", Image=7, Options=Options, Used=1).Create()
			devicecreated.append(deviceparam(7, 0, "0"))
		if 8 not in Devices:
			Options = {"LevelActions": "||",
				"LevelNames": tl.t("Off|On"),
				"LevelOffHidden": "false",
				"SelectorStyle": "0"}
			Domoticz.Device(Name=tl.t("Turbo mode"), Unit=8, TypeName="Selector Switch", Image=7, Options=Options, Used=1).Create()
			devicecreated.append(deviceparam(8, 0, "0"))
		if 9 not in Devices:
			Options = {"LevelActions": "||",
				"LevelNames": tl.t("Off|On"),
				"LevelOffHidden": "false",
				"SelectorStyle": "0"}
			Domoticz.Device(Name=tl.t("Economy mode"), Unit=9, TypeName="Selector Switch", Image=7, Options=Options, Used=1).Create()
			devicecreated.append(deviceparam(9, 0, "0"))
		if 10 not in Devices:
			Options = {"LevelActions": "||",
				"LevelNames": tl.t("Off|On"),
				"LevelOffHidden": "false",
				"SelectorStyle": "0"}
			Domoticz.Device(Name=tl.t("Filter"), Unit=10, TypeName="Selector Switch", Image=7, Options=Options, Used=1).Create()
			devicecreated.append(deviceparam(10, 0, "0"))
		if 11 not in Devices:
			Options = {"LevelActions": "||",
				"LevelNames": tl.t("Off|On"),
				"LevelOffHidden": "false",
				"SelectorStyle": "0"}
			Domoticz.Device(Name=tl.t("Cleaning"), Unit=11, TypeName="Selector Switch", Image=7, Options=Options, Used=1).Create()
			devicecreated.append(deviceparam(11, 0, "0"))
		if 12 not in Devices:
			Options = {"LevelActions": "||",
				"LevelNames": tl.t("Off|On"),
				"LevelOffHidden": "false",
				"SelectorStyle": "0"}
			Domoticz.Device(Name=tl.t("Sound signal"), Unit=12, TypeName="Selector Switch", Image=8, Options=Options, Used=1).Create()
			devicecreated.append(deviceparam(12, 0, "0"))
		if 13 not in Devices:
			Options = {"LevelActions": "||",
				"LevelNames": tl.t("Off|Send only|Store only|Send and store"),
				"LevelOffHidden": "true",
				"SelectorStyle": "1"}
			Domoticz.Device(Name=tl.t("Status mode"), Unit=13, TypeName="Selector Switch", Image=3, Options=Options, Used=1).Create()
			devicecreated.append(deviceparam(13, 0, "30"))
		if 14 not in Devices:
			Options = {"LevelActions": "||",
					   "LevelNames": tl.t("Off|1 min|5 min|15 min|30 min|60 min|120 min|240 min|480 min"),
					   "LevelOffHidden": "false",
					   "SelectorStyle": "1"}
			Domoticz.Device(Name= tl.t("Automatic IR retransmission"), Unit=14, TypeName="Selector Switch", Image=21, Options=Options, Used=1).Create()
			devicecreated.append(deviceparam(14, 0, "0"))
		if 15 not in Devices:
			Domoticz.Device(Name= tl.t("IR command resend"), Unit=15, Type=244, Subtype=73, Switchtype=9, Image=9, Used=1).Create()
			devicecreated.append(deviceparam(15, 0, "0"))
			self.addfavorite(Devices[15].ID)
		

		for device in devicecreated:
			Devices[device.unit].Update(nValue=device.nvalue, sValue=device.svalue)

		self.AC_vendor = Parameters["Mode1"]

		self.AC_ipaddress = Parameters["Mode2"]

		self.parameter_change()

	
	def parameter_change(self):

		self.AC_temp = float(Devices[2].sValue)
		
		if Devices[1].sValue == "0" :
			self.AC_power = False
		elif Devices[1].sValue == "10" :
			self.AC_power = True

		if Devices[3].sValue == "10" :
			self.AC_mode = "Auto"
		elif Devices[3].sValue == "20" :
			self.AC_mode = "Cool"
		elif Devices[3].sValue == "30" :
			self.AC_mode = "Heat"
		elif Devices[3].sValue == "40" :
			self.AC_mode = "Fan"
		elif Devices[3].sValue == "50" :
			self.AC_mode = "Dry"

		if Devices[4].sValue == "10" :
			self.AC_fan_rate = "Auto"
		elif Devices[4].sValue == "20" :
			self.AC_fan_rate = "Low"
		elif Devices[4].sValue == "30" :
			self.AC_fan_rate = "Medium"
		elif Devices[4].sValue == "40" :
			self.AC_fan_rate = "High"
		elif Devices[4].sValue == "50" :
			self.AC_fan_rate = "Max"

		if Devices[5].sValue == "0" :
			self.AC_vertical_air = "Off"
		elif Devices[5].sValue == "10" :
			self.AC_vertical_air = "Auto"

		if Devices[6].sValue == "0" :
			self.AC_horizontal_air = "Off"
		elif Devices[6].sValue == "10" :
			self.AC_horizontal_air = "Auto"

		if Devices[7].sValue == "0" :
			self.AC_silent_mode = "Off"
		elif Devices[7].sValue == "10" :
			self.AC_silent_mode = "On"

		if Devices[8].sValue == "0" :
			self.AC_turbo_mode = "Off"
		elif Devices[8].sValue == "10" :
			self.AC_turbo_mode = "On"
		
		if Devices[9].sValue == "0" :
			self.AC_economy_mode = "Off"
		elif Devices[9].sValue == "10" :
			self.AC_economy_mode = "On"

		if Devices[10].sValue == "0" :
			self.AC_filter = "Off"
		elif Devices[10].sValue == "10" :
			self.AC_filter = "On"

		if Devices[11].sValue == "0" :
			self.AC_cleaning = "Off"
		elif Devices[11].sValue == "10" :
			self.AC_cleaning = "On"
		
		if Devices[12].sValue == "0" :
			self.AC_sound_signal = "Off"
		elif Devices[12].sValue == "10" :
			self.AC_sound_signal = "On"

		if Devices[13].sValue == "10" :
			self.AC_status_mode = "Send only"
		elif Devices[13].sValue == "20" :
			self.AC_status_mode = "Store only"
		elif Devices[13].sValue == "30" :
			self.AC_status_mode = "Send and store"

		if Devices[14].sValue == "0" :
			self.AC_ir_resend = None
		elif Devices[14].sValue == "10" :
			self.AC_ir_resend = 1
		elif Devices[14].sValue == "20" :
			self.AC_ir_resend = 5
		elif Devices[14].sValue == "30" :
			self.AC_ir_resend = 15
		elif Devices[14].sValue == "40" :
			self.AC_ir_resend = 30
		elif Devices[14].sValue == "50" :
			self.AC_ir_resend = 60
		elif Devices[14].sValue == "60" :
			self.AC_ir_resend = 120
		elif Devices[14].sValue == "70" :
			self.AC_ir_resend = 240
		elif Devices[14].sValue == "80" :
			self.AC_ir_resend = 480

		self.AC_command = {
			"Vendor": self.AC_vendor,
			"Power": self.AC_power,
			"Mode": self.AC_mode,
			"FanSpeed": self.AC_fan_rate,
			"Temp": self.AC_temp,
			"SwingV": self.AC_vertical_air,
			"SwingH": self.AC_horizontal_air,
			"Silent": self.AC_silent_mode,
			"Turbo": self.AC_turbo_mode,
			"Econo": self.AC_economy_mode,
			"Filter": self.AC_filter,
			"Clean": self.AC_cleaning,
			"BEEP": self.AC_sound_signal,
			"Sleep": self.AC_status_mode
		}

		json_command = json.dumps(self.AC_command)
		encoded_json = parse.quote(json_command, safe="")
		self.url = f"http://{self.AC_ipaddress}/cm?cmnd=IRHVAC%20{encoded_json}"

	def onStop(self):
		Domoticz.Debugging(0)


	def onCommand(self, Unit, Command, Level, Color):

		Domoticz.Debug("onCommand called for Unit {}: Command '{}', Level: {}".format(Unit, Command, Level))

		nvalue = 1 if Level > 0 else 0
		svalue = str(Level)

		Devices[Unit].Update(nValue=nvalue, sValue=svalue)

		if Unit in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15):
			self.AC_last_command_time = None
			self.parameter_change()
			self.onHeartbeat()


	def onHeartbeat(self):

		if self.AC_last_command_time is None :

			request.urlopen(self.url)
			Domoticz.Debug(f"IRHVAC küldés: {self.url}")
			self.AC_last_command_time = datetime.now()

			
		elif self.AC_ir_resend is not None:
			
			if datetime.now() - self.AC_last_command_time >= timedelta(minutes=self.AC_ir_resend):
				request.urlopen(self.url)
				Domoticz.Debug(f"IRHVAC küldés: {self.url}")
				self.AC_last_command_time = datetime.now()


	def WriteLog(self, message, level="Normal"):

		if (self.loglevel == "Verbose" and level == "Verbose") or level == "Status":
			if self.statussupported:
				Domoticz.Status(message)
			else:
				Domoticz.Log(message)
		elif level == "Normal":
			Domoticz.Log(message)

	def addfavorite(self, deviceidx):

		idx = deviceidx
		DomoticzAPI("idx={}&isfavorite=1&param=makefavorite&type=command".format(idx))

	def removefavorite(self, deviceidx):

		idx = deviceidx
		DomoticzAPI("idx={}&isfavorite=0&param=makefavorite&type=command".format(idx))



global _plugin
_plugin = BasePlugin()


def onStart():
	global _plugin
	_plugin.onStart()


def onStop():
	global _plugin
	_plugin.onStop()


def onCommand(Unit, Command, Level, Color):
	global _plugin
	_plugin.onCommand(Unit, Command, Level, Color)


def onHeartbeat():
	global _plugin
	_plugin.onHeartbeat()


# Plugin utility functions ---------------------------------------------------

def DomoticzAPI(APICall):

	resultJson = None
	url = "http://{}:{}/json.htm?{}".format(Parameters["Address"], Parameters["Port"], parse.quote(APICall, safe="&="))
	Domoticz.Debug("Calling domoticz API: {}".format(url))
	try:
		req = request.Request(url)
		if Parameters["Username"] != "":
			Domoticz.Debug("Add authentification for user {}".format(Parameters["Username"]))
			credentials = ('%s:%s' % (Parameters["Username"], Parameters["Password"]))
			encoded_credentials = base64.b64encode(credentials.encode('ascii'))
			req.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))

		response = request.urlopen(req)
		if response.status == 200:
			resultJson = json.loads(response.read().decode('utf-8'))
			if resultJson["status"] != "OK":
				Domoticz.Error("Domoticz API returned an error: status = {}".format(resultJson["status"]))
				resultJson = None
		else:
			Domoticz.Error("Domoticz API: http error = {}".format(response.status))
	except:
		Domoticz.Error("Error calling '{}'".format(url))
	return resultJson


# Generic helper functions
def DumpConfigToLog():
	for x in Parameters:
		if Parameters[x] != "":
			Domoticz.Debug("'" + x + "':'" + str(Parameters[x]) + "'")
	Domoticz.Debug("Device count: " + str(len(Devices)))
	for x in Devices:
		Domoticz.Debug("Device: " + str(x) + " - " + str(Devices[x]))
		Domoticz.Debug("Device ID: '" + str(Devices[x].ID) + "'")
		Domoticz.Debug("Device Name: '" + Devices[x].Name + "'")
		Domoticz.Debug("Device nValue: " + str(Devices[x].nValue))
		Domoticz.Debug("Device sValue: '" + Devices[x].sValue + "'")
		Domoticz.Debug("Device LastLevel: " + str(Devices[x].LastLevel))
	return
