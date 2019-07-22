Oracle Java JCE
=========

[![Build Status](https://travis-ci.com/triviadata/ansible-oracle-java-jce.svg?branch=master)](https://travis-ci.com/triviadata/ansible-oracle-java-jce)

Install Oracle Java JCE into existing `JAVA_HOME` on Linux host.

Requirements
--------------
None.

Role Variables
--------------
Variables are listed in `defaults/main.yml` and desribed below:

* **java_home_directory**: Java home directory, default is `/usr/java/latest`
* **oracle_java_jce_version**: Oracle Java JCE version, possible values are `6`, `7` and `8`, default is `8`
* **oracle_java_jce_home_directory**: default location of JCE extension, default is `JAVA_HOME/jre/lib/security`
* **oracle_java_jce_download_dir**: directory where to store downloaded archive, default is `/tmp`
* **oracle_java_jce_download_link**: Oracle Java JCE download URL, change if are you using your own repository
* **oracle_java_jce_download_checksum**: Oracle Java JCE checksum, change if your SHA differs from official one

Dependencies
----------------
None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: triviadata.oracle-java-jce

License
-------

BSD

Author Information
-------
This role was created in June 2019 by Matus Cuper
