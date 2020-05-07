#/bin/bash

mysql -uroot vmware -e "SELECT * from vm_alarm where vmname  alartime >= DATE_ADD(NOW(),INTERVAL -10 MINUTE ) order  BY alartime  desc limit 10;"
