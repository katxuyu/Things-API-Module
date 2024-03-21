from things import EndDeviceRegistryService as api

app_name = 'packetworx-test-devices'
app_name2 = 'things-module-test-app'
app_domain = ''
app_key = ''

ed = api(app_domain, app_name, app_key)

#print(ed.ListEndDevices())
print(ed.GetEndDevice('op-0000000000007319'))