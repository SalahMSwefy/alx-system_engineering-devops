#Client configuration file (w/ Puppet)

file_line { 'PasswordAuthentication':
  ensure  => 'present',
  path    => '/etc/ssh/sshd_config',
  line    => '  PasswordAuthentication no',
  replace => true,
}

file_line { 'IdentityFile':
  ensure  => 'present',
  path    => '/etc/ssh/sshd_config',
  line    => '  IdentityFile ~/.ssh/school',
  replace => true,
}
