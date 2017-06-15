#!/bin/bash

wget http://raw.githubusercontent.com/bussas/cwbotstuff/master/config
cp -f config ~/.telegram-cli
./telegram-cli -p profile_1 
wait
./telegram-cli -p profile_2
wait
./telegram-cli -p profile_3 
wait
./telegram-cli -p profile_4
wait
./telegram-cli -p profile_5
wait
./telegram-cli -p profile_6
wait
./telegram-cli -p profile_7
wait
./telegram-cli -p profile_8
wait
./telegram-cli -p profile_9
wait
./telegram-cli -p profile_10
wait
