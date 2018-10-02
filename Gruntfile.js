module.exports = function(grunt) {
    
    // Project configuration
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        sass: {
            dist: {
                files: [{
                    expand: true,
                    cwd: 'sass',
                    src: ['*.sass'],
                    dest: 'static/css',
                    ext: '.css'
                }]
            }
        },
        cssmin: {
            target: {
                files: [{
                    expand: true,
                    cwd: 'static/css',
                    src: ['*.css', '!*.min.css'],
                    dest: 'static/css',
                    ext: '.min.css'
                }]
            }
        },
        watch: {
            sass: {
                tasks: ['sass', 'cssmin'],
                files: ['sass/**/*.sass'],
                options: {
                    spawn: true,
                    reload: true
                }
            },
            css: {
                files: ['static/css/*.min.css'],
                options: {
                    livereload: 35729
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-cssmin');

    grunt.registerTask('default', ['watch']);
};
