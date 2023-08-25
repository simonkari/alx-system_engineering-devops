# The following Puppet code generates a file in the /tmp directory.

file { 'school':
# Ensure that the file exists
  ensure  => file,
  path    => '/tmp/school',
# Set file permission to 0744
  mode    => '0744',
# Set file owner to www-data
  owner   => 'www-data',
# Set file group to www-data
  group   => 'www-data',
# Set the content of the file
  content => "I love Puppet\n",
}
