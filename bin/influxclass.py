#! /usr/bin/env python3

from influxdb import InfluxDBClient
import json

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

   def getInterest(self):
      interest_json=self.client.query('select last(receivedInterest) from availablecash;')
      #Generate a list from the datapoints of the returned result set and return the dictionatry item 'last'
      return list(interest_json.get_points())[0].get('last')
