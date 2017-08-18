#!/bin/bash
#Define the Variables
dblocation="eastus"
dbresourcegroup="iotdbresourceg"
dbname="iotdb"
dbkind="MongoDB"
dbaccountname="iotdbaccount25"
dbcollection="iotdbcollection"

#Craete the Resource Group
az group create -l $dblocation -n $dbresourcegroup

#Create the CosmosDB Account
az cosmosdb create -n $dbaccountname -g $dbresourcegroup --kind $dbkind
az cosmosdb show -n $dbaccountname -g $dbresourcegroup | jq .writeLocations[0].documentEndpoint | awk -F '"' '{print $2}' > iotdb_endpoint.txt
az cosmosdb list-keys -n $dbaccountname -g $dbresourcegroup | jq .primaryMasterKey | awk -F '"' '{print $2}' > iotdbkey.txt

az cosmosdb database create --db-name $dbname --key $(cat iotdbkey.txt) --name $dbname -g $dbresourcegroup --url-connection $(cat iotdb_endpoint.txt)

az cosmosdb collection create --collection-name $dbcollection --db-name $dbname --key $(cat iotdbkey.txt) --name $dbname -g $dbresourcegroup --url-connection $(cat iotdb_endpoint.txt)