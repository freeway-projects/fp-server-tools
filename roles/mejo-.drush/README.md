# Ansible role to install Drupal Drush on a webserver

[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-drush-blue.svg)](https://galaxy.ansible.com/mejo-/drush/) [![Build Status](https://travis-ci.org/mejo-/ansible-role-drush.svg?branch=master)](https://travis-ci.org/mejo-/ansible-role-drush)

A very simple role to install Drupal Drush globally.

Additionally, it installs a daily cronjob to update Drush.

# Preliminaries

PHP Composer needs to be available in order for this role to work.

# Defaults

```
# The location of the entire drush installation (includes all the supporting
# files, as well as the drush executable file.
drush_install_path: /usr/local/share/drush

# The path where drush will be installed and available to your system. Should be
# in your user's $PATH so you can run commands simply with `drush` instead of
# the full path.
drush_path: /usr/local/bin/drush

# The version of Drush to install (examples: "8.0.2", "7.x", "7.1.0", "master").
# This should be a string as it refers to a git branch, tag, or commit hash.
drush_version: 8.1.0

# Path to where Composer is installed.
drush_composer_path: /usr/local/bin/composer

# Whether to keep Drush up-to-date with the latest revision of the branch
# specified by drush_version.
drush_keep_updated: no
```

# License

This Ansible role is licensed under the GNU GPLv3 or later.

# Author

Copyright 2017 Jonas Meurer <jonas@freesources.org>
