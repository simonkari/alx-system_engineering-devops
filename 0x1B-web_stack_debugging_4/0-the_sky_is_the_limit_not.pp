# Corrects an issue with an nginx site that
# struggles with handling multiple simultaneous requests
exec { 'fix-for-nginx':
  command => "bash -c \"sed -iE 's/^ULIMIT=.*/ULIMIT=\\\"-n 8192\\\"/'
  /etc/default/nginx; service nginx restart\"",
  path    => '/usr/bin:/usr/sbin:/bin'
}
