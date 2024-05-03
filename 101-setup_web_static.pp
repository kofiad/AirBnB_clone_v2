# 0-setup_web_static.pp

# Install Apache
package { 'apache2':
    ensure => installed,
}

# Create the web_static directory
file { '/var/www/html/web_static':
    ensure => directory,
    owner  => 'root',
    group  => 'root',
    mode   => '0755',
}

# Create the index.html file
file { '/var/www/html/index.html':
    ensure  => file,
    content => '<html><body>Web Static Content</body></html>',
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
}

# Create a symbolic link to the web_static directory
file { '/var/www/html/static':
    ensure => link,
    target => '/var/www/html/web_static',
}
