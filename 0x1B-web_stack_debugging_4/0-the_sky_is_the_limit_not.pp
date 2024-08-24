# A puppet manifest that configures Nginx to handle high traffic loads

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  source  => 'puppet:///modules/nginx/nginx.conf',
  notify  => Service['nginx'],
}

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
}
