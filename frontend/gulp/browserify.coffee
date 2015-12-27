browserify = require 'browserify'
gulp = require 'gulp'
gutil = require 'gulp-util'
uglify = require 'gulp-uglify'
buffer = require 'vinyl-buffer'
source = require 'vinyl-source-stream'
_ = require 'underscore'
livereload = require 'gulp-livereload'
watchify = require 'watchify'

vendor_list = ->
  packageManifest = require('../package.json')
  result = _.keys(packageManifest.dependencies) or []
  result.push 'buffer'
  return result

b = browserify
  entries: './src/app.coffee'
  extensions: ['.coffee', '.hbs']
  cache: {}
  packageCache: {}
#  debug: true
  fullPaths: true
  insertGlobals: true

w = watchify b, {
  poll: true
}

w.external id for id in vendor_list()

watch_bundle = ->
  w.bundle()
  .on "error", (error) ->
    gutil.log error.message
    gutil.beep()
    @emit 'end'
  .pipe source 'app.js'
  .pipe buffer()
  .pipe gulp.dest './dist/'
  .pipe livereload()

w.on 'update', watch_bundle
w.on 'time', (time) ->
  gutil.log "browserify", time, 'ms'


gulp.task 'build:vendor', ->
  b = browserify()
  for id in vendor_list()
    b.require id, expose: id
  b.bundle()
  .pipe source('vendor.js')
  .pipe gulp.dest('./dist/')


gulp.task 'build:app', ->
  b = browserify
    entries: './src/app.coffee'
    extensions: ['.coffee', '.hbs']
    insertGlobals: true
  b.external id for id in vendor_list()

  b.bundle()
  .pipe source('app.js')
  .pipe buffer()
  .pipe gulp.dest './dist/'


module.exports = watch_bundle
