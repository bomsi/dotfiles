alias ll='ls -alh'
alias mountdislocker='mkdir -p /mnt/dislocker; mkdir -p /mnt/dislockerm; dislocker -v -r -u /dev/sdb1 -- /mnt/dislocker && mount -o loop,ro /mnt/dislocker/dislocker-file /mnt/dislockerm'
alias mountdislockerrw='mkdir -p /mnt/dislocker; mkdir -p /mnt/dislockerm; dislocker -v -u /dev/sdb1 -- /mnt/dislocker && mount -o loop /mnt/dislocker/dislocker-file /mnt/dislockerm'
alias umountdislocker='umount /mnt/dislocker/dislocker-file && umount dislocker'

