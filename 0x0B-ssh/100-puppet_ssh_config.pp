#!/usr/bin/env bash
# Ensure SSH client configuration exists
file { '/home/ubuntu/.ssh/config':
  ensure => present,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
}

# Configure SSH client
file_line { 'Turn off passwd auth':
  path   => '/home/ubuntu/.ssh/config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

file_line { 'Declare Identity file':
  path   => '/home/ubuntu/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile',
}
