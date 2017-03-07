#! /usr/bin/env python3

import confparse
import accdata
import influxclass

confdata = confparse.confParse('/etc/lc/lc.data')
acctdata = accdata.accData(confdata.investorID(),confdata.authKey())
dbhost = confdata.db_host()
dbport = confdata.db_port()
dbuser = confdata.db_user()
dbpass = confdata.db_pass()
dbname = confdata.db_name()

json_body = [
   {
      "measurement": "availablecash",
      "fields":{
         "cashavailable": acctdata.availableCash(),
         "accounttotal": acctdata.accountTotal(),
         "outstandingPrincipal": acctdata.outstandingPrincipal(),
         "primaryNAR":acctdata.primaryNAR(),
         "receivedInterest":acctdata.receivedInterest(),
         "receivedPrincipal":acctdata.receivedPrincipal(),
         "receivedLateFees":acctdata.receivedLateFees()
      }
   }
]

influxclass.influxClass.writeToDB(json_body, confdata)
#client = InfluxDBClient(dbhost, dbport, dbuser, dbpass, dbname)
#client.write_points(json_body)

