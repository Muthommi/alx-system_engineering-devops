# This puppet manifest creates a file with certain requirements.
file { '/tmp/school':
  ensure  => 'file',
  content => 'I love puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
