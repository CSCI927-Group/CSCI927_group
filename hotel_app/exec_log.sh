#! /bin/sh
echo 'Timestamp, Case ID, User Name, Event' > info.csv
grep 'CUSTOMLOG' info.log | sed 's/, CUSTOMLOG$//'>> info.csv