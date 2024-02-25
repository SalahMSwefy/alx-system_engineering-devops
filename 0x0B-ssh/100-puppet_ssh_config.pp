#Client configuration file (w/ Puppet)

include stdlib

file_line { 'Client configuration file':
  ensure  => present,
  path    => '/etc/ssh/sshd_config',
  line    => 'PasswordAuthentication no
  IdentityFile ~/.ssh/school',
  replace => true,
}
