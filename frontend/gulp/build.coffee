gulp = require 'gulp'
gulp.task 'build', ['copy', 'build:less', 'build:vendor', 'build:app']
gulp.task 'default', ['copy', 'less', 'build:vendor', 'watch']
