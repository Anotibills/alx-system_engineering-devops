#!/usr/bin/env bash
# Puppet script for ssh configuration

file { '/etc/ssh/ssh_config':
        ensure  => present,
        content => "
                    #Script for SSH Configuration
                    Host *
                         PasswordAuthentication no
                         IdentityFile ~/.ssh/school
                   ",
}
