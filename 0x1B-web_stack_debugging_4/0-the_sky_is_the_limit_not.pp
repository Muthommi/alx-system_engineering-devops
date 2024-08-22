# A puppet manifest that configures Nginx to handle high traffic loads

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Exec['reload-nginx'],
}

exec { 'reload-nginx':
  command     => 'service nginx reload',
  refreshonly => true,
}
