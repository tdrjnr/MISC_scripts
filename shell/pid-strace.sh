mkdir /tmp/strace
cd /tmp/strace
for i in `ps axuwf | grep command | awk '{ print $2 }'`; do (strace -p $i > command-$i.strace 2>&1)&  done