# This manifest kills a process named killmenow.
exec { 'kill_killmenow':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
  onlyif  => 'pgrep killmenow',
}
