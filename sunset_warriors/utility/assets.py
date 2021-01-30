"""Compile static assets."""

from flask_assets import Bundle

bundles = {

    'main_js': Bundle(
        'js/lib/jquery-3.5.1.min.js',
        'js/lib/popper.min.js',
        'js/lib/bootstrap.bundle.min.js',
        'js/maps.js',
        'js/custom.js',
        filters='jsmin',
        output='gen/main.%(version)s.js'),

    
    'main_css': Bundle(
        'sass/lib/bootstrap.min.css',
        'sass/main.scss',
        filters='libsass',
        depends=['sass/*.scss'],
        output='gen/main.%(version)s.css'),
}