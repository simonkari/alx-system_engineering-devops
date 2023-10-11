# Puppet Manifest to Fix a Faulty WordPress Site
exec { 'fix-wordpress error':
  # Specify the shell command to be executed
  command => 'bash -c "sed -i s/class-wp-locale.phpp/class-wp-locale.php/ \
/var/www/html/wp-settings.php; service apache2 restart"',
  path    => '/usr/bin:/usr/sbin:/bin'
}
