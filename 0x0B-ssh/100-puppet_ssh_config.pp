#Client configuration file (w/ Puppet)

lines = 'Host 485447-web-01
    HostName 18.235.243.86
    User ubuntu
    IdentifyFile ~/.ssh/school
    PasswordAuthentication no'

file {'/etc/ssh/ssh_config':
    ensure => file,
    content => $lines,
}
