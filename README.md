# fp-server-tools
Set of useful server admin tools to be installed on servers.

# Installation
## Prerequisites
### Digital Ocean - Debian 10

#### Script to run when server is being built

These are the commands to include in the user data script:

    apt --quiet update
    apt --assume-yes --quiet dist-upgrade

    # Ansible and git are needed to use fp-server-tools
    apt --assume-yes --quiet install ansible git python-apt apt-transport-https

    # This is needed by Ansible to be able to run with the --check option.
    apt --assume-yes --quiet install ansible git python-apt apt-transport-https

    # This is needed to be able to install apt packages from alternative sources.
    apt --assume-yes --quiet install ansible git apt-transport-https

    git clone https://github.com/freeway-projects/fp-server-tools.git /opt/fp-server-tools

#### Updating fp-server-tools

NB - This is only relevant if you have write access to the fp-server-tools repo.  If you do not have write access and wish to submit changes then fork the repo and submit pull requests.

If it is required to be able to push changes to this repo back up then create an ssh key and upload the public key to your account at GitHub:

    # ssh-keygen -b 4096
    # cat ~/.ssh/id_rsa.pub
    
Then paste the public key into https://github.com/settings/keys 

Also, on the server change the remote URL to use SSH so that git push works with:

    # cd /opt/fp-server-tools
    # git remote set-url origin git@github.com:freeway-projects/fp-server-tools.git
