#! /usr/bin/env python3

from influxdb import InfluxDBClient

class influxClass(object):
   def __init__(self, json_body, confdata):
      dbhost = confdata.db_host()
      dbport = confdata.db_port()
      dbuser = confdata.db_user()
      dbpass = confdata.db_pass()
      dbname = confdata.db_name()
      client = InfluxDBClient(dbhost, dbport, dbuser, dbpass, dbname)

def writeToDB(self)
   client.write_points(json_body)

