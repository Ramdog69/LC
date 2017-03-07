#! /usr/bin/env python3

from influxdb import InfluxDBClient

class influxClass(object):
   def __init__(self, confdata):
      self.dbhost = confdata.db_host()
      self.dbport = confdata.db_port()
      self.dbuser = confdata.db_user()
      self.dbpass = confdata.db_pass()
      self.dbname = confdata.db_name()
      self.client = InfluxDBClient(self.dbhost, self.dbport, self.dbuser, self.dbpass, self.dbname)

   def writeToDB(self, json_body):
      self.client.write_points(json_body)

