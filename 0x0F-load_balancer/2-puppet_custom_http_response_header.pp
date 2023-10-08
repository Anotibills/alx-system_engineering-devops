# Script for custom header using puppet

# updating ubuntu server
exec { 'update server':
  command     => 'apt-get update',
  user        => 'root',
  provider    => 'shell',
  refreshonly => true,
}

# installing nginx web server on server
package { 'nginx':
  ensure   => present,
  provider => 'apt',
  require  => Exec['update server'],
}

# custom nginx response header (X-Served-By: hostname)
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

# restarting nginx service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

