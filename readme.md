## For windows setup, I ran following commands to work for me

## Open git bash and run the following commands
- ssh-keygen -t rsa -b 4096 -C "myemail@gmail.com"

- ls ~/.ssh (to check if 25519 files are generated or not if not then run below command)
- ssh-keygen -t ed25519 -C "myemail@gmail.com"

- ssh-add ~/.ssh/id_ed25519
- ssh-add "/c/Users/locationname/.ssh/id_ed25519"
- ssh-add -l
- cat ~/.ssh/id_ed25519.pub

## copy the string in git provider ssh

