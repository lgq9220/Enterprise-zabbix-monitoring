#/bin/bash
mysql -uroot vmware -e "SELECT * from esxi_alarm where  alartime >= DATE_ADD(NOW(),INTERVAL -10 MINUTE ) order  BY alartime  desc limit 10;"
