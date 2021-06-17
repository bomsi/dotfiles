# dotfiles

This repository contains my current dotfiles and scripts. Additionally, some random shell scripting notes can be found here as well.

## Installation

- navigate to your home directory
- clone this repo (`git clone git@github.com:bomsi/dotfiles.git`)
- set bash as default shell (`chsh -s /bin/bash`) and use it
- create `~/.local` if it does not exist
- add symlinks:
```sh
ln -s ~/dotfiles/.local/bin ~/.local/bin
ln -s ~/dotfiles/.gitconfig ~/.gitconfig
ln -s ~/dotfiles/.vimrc ~/.vimrc
ln -s ~/dotfiles/.bash_aliases ~/.bash_aliases
ln -s ~/dotfiles/.bashrc ~/.bashrc
ln -s ~/dotfiles/.bash_profile ~/.bash_profile
ln -s ~/dotfiles/.bash_logout ~/.bash_logout
```

## Unrelated Scripting Notes

### Extracting IMAP Logins

If we are interested in IMAP login analysis with SQLite, it is easy to prepare data with:
```sh
cd /root && mkdir ana
grep "dovecot: imap-login: Login:" /var/log/maillog|awk -v sq="'" -F'[,=<> ]' '{ print "INSERT INTO imaplogins(timestamp, session, user, ip) VALUES (" sq "2021-" $1 "-" $2 " " $3 sq ", " sq $29 sq ", " sq $10 sq ", " sq $17 sq ");"}'>/root/ana/data.sql
```
To extract from archived logs:
```sh
zgrep "dovecot: imap-login: Login:" /var/log/maillog*.gz|awk -v sq="'" -F'[,=<> ]' '{ print "INSERT INTO imaplogins(timestamp, session, user, ip) VALUES (" sq "2021-" $1 "-" $2 " " $3 sq ", " sq $29 sq ", " sq $10 sq ", " sq $17 sq ");"}'>>/root/ana/data.sql
```
Then:
```
sqlite3 /root/ana/ana.db
sqlite> CREATE TABLE IF NOT EXISTS imaplogins(timestamp TEXT NOT NULL, session TEXT NOT NULL, user TEXT NOT NULL, ip TEXT NOT NULL, UNIQUE(timestamp, session) ON CONFLICT IGNORE);
sqlite> .read /root/ana/data.sql
```

