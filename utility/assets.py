from flask_assets import Bundle

bundles = {

    'home_js': Bundle(
        'js/vendor/bootstrap.bundle.min.js',
        'js/vendor/jquery-3.5.1.min.js',
        'js/vendor/popper.min.js',
        'js/maps.js',
        filters='jsmin',
        output='gen/home.%(version)s.js'),

    
    'home_css': Bundle(
        'css/vendor/bootstrap.min.css',
        'css/main.scss',
        depends='**/*.scss',
        filters='libsass',
        output='gen/home.%(version)s.css'),
}