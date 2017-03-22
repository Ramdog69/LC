#! /usr/bin/env python3

import confparse
import accdata
import influxclass

confdata = confparse.confParse('/etc/lc/lc.data')
acctdata = accdata.accData(confdata.investorID(),confdata.authKey())
influxclass = influxclass.influxClass(confdata)
dbhost = confdata.db_host()
dbport = confdata.db_port()
dbuser = confdata.db_user()
dbpass = confdata.db_pass()
dbname = confdata.db_name()

diff_interest =  acctdata.receivedInterest() - influxclass.getInterest()
diff_principal = acctdata.receivedPrincipal() - influxclass.getPrincipal()

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
         "receivedLateFees":acctdata.receivedLateFees(),
         "lastInterest":diff_interest,
         "lastPrincipal":diff_principal
      }
   }
]

influxclass.writeToDB(json_body)

