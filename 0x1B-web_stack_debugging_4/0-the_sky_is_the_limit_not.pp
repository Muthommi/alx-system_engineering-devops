# A puppet manifest that configures Nginx to handle high traffic loads

exec { 'fix-for-nginx':
  command =>  'sed -i "s/[0-9]\+\s\+[0-9]\+/4096 4096/" /etc/default/nginx && service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'test -f /etc/default/nginx',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/nginx.conf'],
}
