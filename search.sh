#!bin/bash

cd /home/jmr/scrapers/deal_cron

/home/jmr/scrapers/deal_cron/venv/bin/python3 /home/jmr/scrapers/deal_cron/make_file.py

sleep 4

source "/home/jmr/scrapers/deal_cron/$(find ./ -type f -cmin -2 | cut -d'/' -f 2)"
