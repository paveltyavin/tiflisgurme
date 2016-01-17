$ = require 'jquery'
_ = require 'underscore'
require './csrf'
require './config'
require 'bootstrap'

router =
  'home/': require './home'
  'shipping/': require './shipping'
  'menu/': require './menu'
  'news/': require './news'
  '': require './common'


window.addEventListener 'load', ->
  for key in _.keys(router)
    do (key) ->
      r = new RegExp(key, 'i')
      if r.test(window.location.pathname)
        router[key]()