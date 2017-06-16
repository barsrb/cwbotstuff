import configparser
import os
import sys
import sqlite3


pathname = os.path.dirname(sys.argv[0])
fullpath = os.path.abspath(pathname)
baseconfig = configparser.SafeConfigParser()

baseconfig.read(fullpath + '/bmconfig.cfg')
if baseconfig.has_section('base'):
    castle_name=baseconfig.get('base','castle_name')
    admin_username=baseconfig.get('base','admin_username')
    order_username=baseconfig.get('base','order_username')
    group_name=baseconfig.get('base','group_name')
    port = baseconfig.get('base','port')
    tg_cli_bin = baseconfig.get('base','tg_cli_bin')
    tg_cli_config = baseconfig.get('base','tg_cli_config')
    tg_bots_dir = baseconfig.get('base','tg_bots_dir')
    tg_start = baseconfig.get('base','tg_start')
    cw_script = baseconfig.get('base','cw_script')
    cw_start = baseconfig.get('base','cw_start')

else:
    print("Vybery zamok po-umolchaniyu:")
    print("1) Blue castle")
    print("2) Yellow castle")
    print("3) Red castle")
    print("4) Mint castle")
    print("5) Twilight castle")
    print("6) Black castle")
    print("7) While castle")
    castle=int(input('Input:'))
    castle_name = {1:"blue", 2:"yellow", 3:"red", 4:"mint", 5:"twilight", 6:"black", 7:"white"}[castle]
    print("Castle -  "+castle_name)
    admin_username = input("Vvedi username admina (bez @):")
    order_username = input("Vvedi username komandira (bez @):") or ""
    group_name = input("Vvedi nazvaniye obshey gruppi:") or ""
    port = input("Vvedi nachalniy nomer porta (1400):") or "1400"
    tg_cli_bin = input("Vvedi put' do tg-cli bin (/root/tg-cli/bin/telegram-cli):") or "/root/tg-cli/bin/telegram-cli"
    tg_cli_config = input("Vvedi put' do configa tg-cli (/root/.telegram-cli/config):") or "/root/.telegram-cli/config"
    tg_bots_dir = input("Vvedi put' do papki s profilyami botov v tg (/root/bots/tg-cli):") or "/root/bots/tg-cli"
    tg_start = input("Vvedi put' dlya scripta zapuska tg-cli (/root/tg_start.sh):") or "/root/tg_start.sh"
    cw_script = input("Vvedite put' dlya scripta cw (/root/main.py):") or "/root/main.py"
    cw_start = input("Vvedi put' dlya zapuska botov cw (/root/cw_start.sh):") or "/root/cw_start.sh"
    if baseconfig.has_section('base'):
        baseconfig.remove_section('base')
    baseconfig.add_section('base')
    baseconfig.set('base','castle_name',str(castle_name))
    baseconfig.set('base','admin_username',str(admin_username))
    baseconfig.set('base','order_username',str(order_username))
    baseconfig.set('base','group_name',str(group_name))
    baseconfig.set('base','port',str(port))
    baseconfig.set('base','tg_cli_bin',str(tg_cli_bin))
    baseconfig.set('base','tg_cli_config',str(tg_cli_config))
    baseconfig.set('base','tg_bots_dir',str(tg_bots_dir))
    baseconfig.set('base','tg_start',str(tg_start))
    baseconfig.set('base','cw_script',str(cw_script))
    baseconfig.set('base','cw_start',str(cw_start))

    with open(fullpath + '/bmconfig.cfg','w+') as cfgfile:
        baseconfig.write(cfgfile)

conn = sqlite3.connect('botmanager.db')
c = conn.cursor()
c.execute("SELECT * FROM sqlite_master WHERE name ='bots' and type='table'; ")
if(len(c.fetchall())<1):
    c.execute("CREATE TABLE bots (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(16), castle VARCHAR (16), admin  VARCHAR (64), orders VARCHAR (64), groups VARCHAR (64), port INTEGER);")

c.execute("SELECT * FROM sqlite_master WHERE type='table'; ")
print (len(c.fetchall()))
conn.close()


def add_bot():
    global port, castle_name, admin_username, order_username, group_name
    conn = sqlite3.connect('botmanager.db')
    c = conn.cursor()
    c.execute("SELECT MAX(port) FROM bots WHERE 1; ")
    for row in c:
        bot_port = row[0]
    if bot_port == None:
        bot_port = port
    else:
        bot_port = int(row[0])+1
    bot_name = input("Vvedite imya bota (bot1, bot2, botred... etc):") or "bot"+str(bot_port)
    print("Vybery zamok (ili Enter, esli "+castle_name+"):")
    print("1) Blue castle")
    print("2) Yellow castle")
    print("3) Red castle")
    print("4) Mint castle")
    print("5) Twilight castle")
    print("6) Black castle")
    print("7) While castle")
    castle=input('Input:') or "0"
    castle = int(castle)
    castle_name = {0:castle_name, 1:"blue", 2:"yellow", 3:"red", 4:"mint", 5:"twilight", 6:"black", 7:"white"}[castle]
    print("Castle -  "+castle_name)
    admin_username = input("Vvedi username admina (bez @)(ili Enter, esli "+admin_username+"):") or admin_username
    order_username = input("Vvedi username komandira (bez @)(ili Enter, esli "+order_username+"):") or order_username
    group_name = input("Vvedi nazvaniye obshey gruppi(ili Enter, esli "+group_name+"):") or group_name
    bot_port = input("Vvedi port (ili Enter, esli "+str(bot_port)+"):") or str(bot_port)
    c.execute("INSERT INTO 'bots' (name,castle, admin, orders, groups, port) VALUES ('"+bot_name+"', '"+castle_name+"', '"+admin_username+"', '"+order_username+"', '"+group_name+"', '"+bot_port+"')")
    conn.commit()
    print("Bot dobavlen!")

def update_cfg_files():
    global tg_cli_config, tg_bots_dir, tg_start, tg_cli_bin, cw_start, cw_script

    conn = sqlite3.connect('botmanager.db')
    c = conn.cursor()

    tg_cli_config_f = open(tg_cli_config, 'w')
    tg_start_f = open (tg_start, 'w')
    cw_start_f = open (cw_start, 'w')

    c.execute("SELECT name, castle, admin, orders, groups, port FROM bots WHERE 1;")
    for row in c:
        bot_name = row[0]
        bot_castle = row[1]
        bot_admin = row[2]
        bot_orders = row[3]
        bot_groups = row[4]
        bot_port = row[5]

        tg_cli_config_f.write(bot_name+" = {\n")
        tg_cli_config_f.write("config_directory = \""+tg_bots_dir+"/"+bot_name+"\";\n")
        tg_cli_config_f.write("msg_num = true;\n};\n\n")
        if not os.path.exists(tg_bots_dir+"/"+bot_name):
            os.makedirs(tg_bots_dir+"/"+bot_name)

        tg_start_f.write("screen -S "+bot_name+"tg -dm bash -c \""+tg_cli_bin+" -p "+bot_name+" --json -P "+str(bot_port)+"\"\n")
        cw_comand = "screen -S "+bot_name+"cw -dm bash -c \"python3 "+cw_script+" --admin "+bot_admin+" --castle "+bot_castle+" --port "+str(bot_port)+" "
        if len(bot_orders)>0:
            cw_comand = cw_comand + " --order "+bot_orders
        if len(bot_groups)>0:
            cw_comand = cw_comand + " --group_name "+bot_groups

        cw_comand = cw_comand+"\"\n"
        cw_start_f.write(cw_comand)

    tg_cli_config_f.close()
    tg_start_f.close()
    cw_start_f.close()
    os.chmod(tg_start, 0o755)
    os.chmod(cw_start, 0o755)
    conn.close()
    pass

if __name__ == '__main__':
    print("1) Dobavit' bota")
    print("2) Izmenit' bota")
    print("3) Obnovit' fayli zapuska")
    op = input()
    if(op=="1"):
        add_bot()
    if(op=="3"):
        update_cfg_files()
