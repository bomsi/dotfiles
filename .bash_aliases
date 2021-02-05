alias ll='ls -alh'
alias mountdislocker='mkdir -p /mnt/dislocker; mkdir -p /mnt/dislockerm; dislocker -v -r -u /dev/sdb1 -- /mnt/dislocker && mount -o loop,ro /mnt/dislocker/dislocker-file /mnt/dislockerm'
alias mountdislockerrw='mkdir -p /mnt/dislocker; mkdir -p /mnt/dislockerm; dislocker -v -u /dev/sdb1 -- /mnt/dislocker && mount -o loop /mnt/dislocker/dislocker-file /mnt/dislockerm'
alias umountdislocker='umount /mnt/dislocker/dislocker-file && umount dislocker'
alias del='srm -i -vv -E'
alias torssh="ssh -o ProxyCommand='nc -x 127.0.0.1:9050 %h %p'"
alias findservletinjar="find . -name '*.jar' -exec unzip -l {} \; | grep -E 'Archive:|[Ss]ervlet'"
alias revportforward='ssh -R 2222:127.0.0.1:8080 user@proxymachine'
alias zd='grep -Iirn --colour'
