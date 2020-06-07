# Test for an interactive shell.  There is no need to set anything
# past this point for scp and rcp, and it's important to refrain from
# outputting anything in those cases.
if [[ $- != *i* ]] ; then
	# Shell is non-interactive. Bye! 
	return
fi

# Load aliases.
if [[ -f ~/.bash_aliases ]] ; then
	. ~/.bash_aliases
fi

# Add ~/.local/bin to path.
export PATH="$HOME/.local/bin:$PATH"

