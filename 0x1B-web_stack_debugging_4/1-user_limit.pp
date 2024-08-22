# A puppet manifest to increase the open file limit for holberton user

exec { 'increase-file-limit':
  command => 'echo "holberton soft nofile 1024" >> /etc/security/limits.conf && echo "holberton hard nofile 2048" >> /etc/security/limits.conf',
  unless  => 'grep -q "holberton soft nofile 1024" /etc/security/limits.conf && grep -q "holberton hard nofile 2048" /etc/security/limits.conf',
}
