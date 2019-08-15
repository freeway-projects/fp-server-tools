# fp-server-tools
Set of useful server admin tools to be installed on servers.

# Installation
## Prerequisites
### Digital Ocean - Debian 10

These are the commands to include in the user data script.

    apt --assume-yes --quiet dist-upgrade
    apt --quiet update
    apt --assume-yes --quiet install ansible git
