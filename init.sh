#!/bin/bash

wget http://raw.githubusercontent.com/bussas/cwbotstuff/master/config
cp -f config ~/.telegram-cli
./telegram-cli --json -p profile_1 -P 2000
wait
./telegram-cli --json -p profile_2 -P 2001
wait
./telegram-cli --json -p profile_3 -P 2002
wait
./telegram-cli --json -p profile_4 -P 2003
wait
./telegram-cli --json -p profile_5 -P 2004
wait
./telegram-cli --json -p profile_6 -P 2005
wait
./telegram-cli --json -p profile_7 -P 2006
wait
./telegram-cli --json -p profile_8 -P 2007
wait
./telegram-cli --json -p profile_9 -P 2008
wait
./telegram-cli --json -p profile_10 -P 2009
wait
