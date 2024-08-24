# A puppet manifest that configures Nginx to handle high traffic loads

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => epp('nginx/nginx.conf,epp'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
}
