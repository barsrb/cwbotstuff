#!/bin/bash

screen -S cli1 -dm ./telegram-cli --json -p profile_1 -P 2001

screen -S cli2 -dm ./telegram-cli -p profile_1 --json -P 2002

screen -S cli3 -dm ./telegram-cli -p profile_1 --json -P 2003

screen -S cli4 -dm ./telegram-cli -p profile_1 --json -P 2004

screen -S cli5 -dm ./telegram-cli -p profile_1 --json -P 2005

screen -S cli6 -dm ./telegram-cli -p profile_1 --json -P 2006

screen -S cli7 -dm ./telegram-cli -p profile_1 --json -P 2007

screen -S cli8 -dm ./telegram-cli -p profile_1 --json -P 2008

screen -S cli9 -dm ./telegram-cli -p profile_1 --json -P 2009

screen -S cli10 -dm ./telegram-cli -p profile_1 --json -P 2010

screen -S bot1 -dm python3 ./main.py --admin RektSup --order RektSup --castle mint --gold 200 --buy 1 --lvlup lvl_def --group_name Botnet.io --port 2001

screen -S bot2 -dm python3 ./main.py --admin RektSup --order RektSup --castle twilight --gold 200 --buy 1 --lvlup lvl_def --group_name Botnet.io --port 2002

screen -S bot3 -dm python3 ./main.py --admin RektSup --order RektSup --castle yellow --gold 200 --buy 1 --lvlup lvl_def --group_name Botnet.io --port 2003

screen -S bot4 -dm python3 ./main.py --admin RektSup --order RektSup --castle white --gold 200 --buy 1 --lvlup lvl_def --group_name Botnet.io --port 2004

screen -S bot5 -dm python3 ./main.py --admin RektSup --order RektSup --castle white --gold 200 --buy 1 --lvlup lvl_def --group_name Botnet.io --port 2005

screen -S bot6 -dm python3 ./main.py --admin RektSup --order RektSup --castle red --gold 200 --buy 1 --lvlup lvl_def --group_name Botnet.io --port 2006

screen -S bot7 -dm python3 ./main.py --admin RektSup --order RektSup --castle blue --gold 200 --buy 1 --lvlup lvl_def --group_name Botnet.io --port 2007

screen -S bot8 -dm python3 ./main.py --admin RektSup --order RektSup --castle black --gold 200 --buy 1 --lvlup lvl_def --group_name Botnet.io --port 2008

screen -S bot9 -dm python3 ./main.py --admin RektSup --order RektSup --castle white --gold 200 --buy 1 --lvlup lvl_def --group_name Botnet.io --port 2009

screen -S bot10 -dm python3 ./main.py --admin RektSup --order RektSup --castle mint --gold 200 --buy 1 --lvlup lvl_def --group_name Botnet.io --port 2010