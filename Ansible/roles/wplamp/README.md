# Wordpress Playbook




Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      become: yes
      roles:
        - {role: wplamp/php_config, tags: ['php_config']}
        - {role: wplamp/apache_install, tags: ['apache_install']}
        - {role: wplamp/mysql_install, tags: ['mysql_install']}
        - {role: wplamp/wordpress, tags: ['wordpress']}

Author Information
------------------

This role was created in 2020 by Nguyen Viet Hung. 
