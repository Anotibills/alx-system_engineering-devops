#This code will create file 'school' in /tmp directory
file {  '/tmp/school':
  ensure  => 'file',
  mode    => '0774',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
