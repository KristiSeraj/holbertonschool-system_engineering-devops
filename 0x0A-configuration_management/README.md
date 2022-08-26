# Configuration Management

- [0-create_a_file.pp](https://github.com/KristiSeraj/holbertonschool-system_engineering-devops/blob/main/0x0A-configuration_management/0-create_a_file.pp) - Puppet file that creates a file in `/tmp`:
  - Requirements:
     - File path is `/tmp/school`
     - File permission is `0744`
     - File owner is `www-data`
     - File group is `www-data`
     - File contains `I love Puppet`

- [1-install_a_package.pp](https://github.com/KristiSeraj/holbertonschool-system_engineering-devops/blob/main/0x0A-configuration_management/1-install_a_package.pp) - Puppet file that install `flask` from `pip3`:
  - Requirements:
    - Install `flask`
    - Version must be `2.1.0`

- [2-execute_a_command.pp](https://github.com/KristiSeraj/holbertonschool-system_engineering-devops/blob/main/0x0A-configuration_management/2-execute_a_command.pp) - Puppet file that creates a manifest that kills a process named `killmenow`
  - Requirements:
    - Must use the `exec` Puppet resource
    - Must use `pkill`

- [killmenow](https://github.com/KristiSeraj/holbertonschool-system_engineering-devops/blob/main/0x0A-configuration_management/killmenow) - Process killed by *2-execute_a_command.pp*
