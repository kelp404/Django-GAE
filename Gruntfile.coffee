module.exports = (grunt) ->
    require('time-grunt') grunt

    grunt.config.init
        compass:
            source:
                options:
                    sassDir: 'application/static/scss'
                    cssDir: 'application/static/css'
                    outputStyle: 'compressed'
                    config: 'application/static/scss/config.rb'

        coffee:
            source:
                files:
                    './application/static/javascript/site.js': ['./application/static/coffeescript/*.coffee']

        watch:
            compass:
                files: ['./application/static/scss/*.scss']
                tasks: ['compass']
                options:
                    spawn: no
            coffee:
                files: ['./application/static/coffeescript/*.coffee']
                tasks: ['coffee']
                options:
                    spawn: no

        karma:
            source:
                configFile: './tests_coffee/karma.config.coffee'

    # -----------------------------------
    # register task
    # -----------------------------------
    grunt.registerTask 'dev', [
        'compass'
        'coffee'
        'watch'
    ]
    grunt.registerTask 'test', ['karma']

    # -----------------------------------
    # tasks
    # -----------------------------------
    grunt.loadNpmTasks 'grunt-contrib-compass'
    grunt.loadNpmTasks 'grunt-contrib-coffee'
    grunt.loadNpmTasks 'grunt-contrib-watch'
    grunt.loadNpmTasks 'grunt-karma'
