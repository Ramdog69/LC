#! /usr/bin/env python3

import requests
import json

class accData(object):
   def __init__(self, investor_id, authkey):
      self.apiVersion = 'v1'
      self.investor_id = investor_id
      self.authkey = authkey
      self.header = {'Authorization' : str(self.authkey), 'Content-Type': 'application/json', 'Accept': 'application/json', "X-LC-LISTING-VERSION":"1.1"}
      self.acctSummary = 'https://api.lendingclub.com/api/investor/' + self.apiVersion + '/accounts/' + str(self.investor_id) + '/summary'
      self.summary = requests.get(self.acctSummary, headers= self.header, params = {'showAll':'true'})
      self.summary_data = json.loads(self.summary.text)

   def availableCash(self):
      return self.summary_data['availableCash']

   def accountTotal(self):
      return self.summary_data['accountTotal']

   def outstandingPrincipal(self):
      return self.summary_data['outstandingPrincipal']

   def totalNotes(self):
      return self.summary_data['totalNotes']

