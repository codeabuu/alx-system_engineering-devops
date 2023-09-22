exec { 'kill':
    command => 'pkill -f killmenow',
    path    => ['/bin', '/usr/bin'],
}
