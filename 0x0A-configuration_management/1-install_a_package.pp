# This Puppet manifest installs flask

package { 'flask':
# Ensure the specific version is installed
  ensure   => '2.1.0',
# Use the pip3 package provider
  provider => 'pip3',
}
