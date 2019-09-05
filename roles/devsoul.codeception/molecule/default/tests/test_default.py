import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_codeception_is_installed(host):
    f = host.file('/usr/local/bin/codecept')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'