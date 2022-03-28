import psycopg2
import json

DB_HOST="rogue.db.elephantsql.com"
DB_NAME="xlnjgqsy"
DB_USER="xlnjgqsy"
DB_PASS="M5DzWmNPNz74X67rY9wZ0KC0ywbAHsIc"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS device_interface")
cur.execute("CREATE TABLE device_interface "
            "(id SERIAL PRIMARY KEY, "
            "connection INTEGER, "
            "name VARCHAR(255) NOT NULL, "
            "description VARCHAR(255), "
            "config json, type VARCHAR(50), "
            "infra_type VARCHAR(50), "
            "port_channel_id INTEGER, "
            "max_frame_size INTEGER);")

conn.commit()

cur.close()
conn.close()

with open("configClear_v2.json") as access_json:
    read_content = json.load(access_json)
    frinx_access = read_content["frinx-uniconfig-topology:configuration"]
    cisco_access = frinx_access["Cisco-IOS-XE-native:native"]
    interface_access = cisco_access["interface"]
    port_access = interface_access["Port-channel"]


    #Port-channel
    def port_channel():
        print("Port-channel")
        for port in port_access:
            print("Name: {}".format(port["name"]))
            if port.get("description") is not None: # ten druhý port nemá description
                print("Description: {}".format(port["description"]))
            else:
                print("Description: null")
            print("Config: {}".format(port))
            print()


    #TenGigabitEthernet
    def ten_gigabit_ethernet():
        print("TenGigabitEthernet")
        TenGigabitEthernet = interface_access["TenGigabitEthernet"]
        for item in TenGigabitEthernet:
            print("Name: TenGigabitEthernet{}".format(item["name"]))
            print("Description: {}".format(item["description"]))
            if item.get("mtu") is not None:
                print("Max_frame_size: {}".format(item["mtu"]))
            else:
                print("Max_frame_size: null")
            print("Config: {}".format(item))
            print()


    #GigabitEthernet
    def gigabit_ethernet():
        print("GigabitEthernet")
        GigabitEthernet = interface_access["GigabitEthernet"]
        for item in GigabitEthernet:
            print("Name: GigabitEthernet{}".format(item["name"]))
            if item.get("description") is not None:
                print("Description: {}".format(item["description"]))
            else:
                print("Description: null")
            if item.get("mtu") is not None:
                print("Max_frame_size: {}".format(item["mtu"]))
            else:
                print("Max_frame_size: null")
            print("Config: {}".format(item))
            print()

    port_channel()
    ten_gigabit_ethernet()
    gigabit_ethernet()