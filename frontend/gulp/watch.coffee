gulp = require 'gulp'
watch_bundle = require './browserify'
livereload = require 'gulp-livereload'

gulp.task 'watch', ->
  livereload.listen
    start: true
  gulp.watch ['./less/**'], ['less']
  gulp.watch ['./copy/**'], ['copy']
  watch_bundle()