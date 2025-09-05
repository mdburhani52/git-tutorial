## For windows setup, I ran following commands to work for me

## Open git bash and run the following commands
- ssh-keygen -t rsa -b 4096 -C "myemail@gmail.com"
- ssh-add ~/.ssh/id_rsa
- cat ~/.ssh/id_rsa.pub
  

## id_ed25519 is a more modern, stronger, and faster encryption algorithm for SSH keys.
- ssh-keygen -t ed25519 -C "myemail@gmail.com" 
- ssh-add ~/.ssh/id_ed25519 
- ssh-add "/c/Users/locationname/.ssh/id_ed25519"
- ssh-add -l
- cat ~/.ssh/id_ed25519.pub

  
### copy the string in git provider ssh

