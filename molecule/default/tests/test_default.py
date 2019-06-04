import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_unzip(host):
    unzip = host.package("unzip")

    assert unzip.is_installed


def test_jar(host):
    oracle_java_jce_path = "/usr/java/latest/jre/lib/security/"

    assert host.file(oracle_java_jce_path + "US_export_policy.jar").exists
    assert host.file(oracle_java_jce_path + "local_policy.jar").exists
