#This script executes a command killmenow with puppet
exec{ 'killmenow':
  command => '/usr/bin/pkill killmenow',
}
