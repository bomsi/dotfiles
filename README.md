# dotfiles

This repository contains my current dotfiles and scripts.

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
