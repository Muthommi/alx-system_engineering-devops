# This puppet manifest ensures that Apache is properly configured and running

# Ensure Apache is installed
package { 'apache2':
  ensure => installed,
}

# Ensure Apache service is running and enabled
service { 'apache2':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  hasstatus  => true,
}

# Ensure the Apache configuration file is correct
file { '/etc/apache2/apache2.conf':
  ensure  => file,
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => 'template('apache/apache2.conf.erb'),
  notify  => Service['apache2'],
}

# Ensure necessary Apache modules are enabled
exec { 'enable_apache_modules':
  command => '/usr/sbin/a2enmod rewrite headers',
  unless  => '/usr/sbin/a2query -m rewrite && /usr/sbin/a2query -m headers',
  notify  => Service['apache2'],
  require => Package['apache2'],
}

# Ensure Apache's document root exists and has proper permissions
file { '/var/www/html':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  require => Package['apache2'],
}
