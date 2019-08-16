# fp-server-tools
Set of useful server admin tools to be installed on servers.

# Installation
## Prerequisites
### Digital Ocean - Debian 10

These are the commands to include in the user data script:

    apt --quiet update
    apt --assume-yes --quiet dist-upgrade
    apt --assume-yes --quiet install ansible git python-apt apt-transport-https
    git clone https://github.com/freeway-projects/fp-server-tools.git /opt/fp-server-tools

If it is required to be able to push changes to this repo back up then create an ssh key and upload the public key to your account at GitHub:

    # ssh-keygen -b 4096
    # cat ~/.ssh/id_rsa.pub
    
Then paste the public key into https://github.com/settings/keys 

Also, on the server change the remote URL to use SSH so that git push works with:

    # cd /opt/fp-server-tools
    # git remote set-url origin git@github.com:freeway-projects/fp-server-tools.git
