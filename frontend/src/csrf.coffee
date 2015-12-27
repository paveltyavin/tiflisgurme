$ = require 'jquery'
require 'jquery.cookie'

csrftoken = $.cookie('csrftoken')

csrfSafeMethod = (method) ->
  # these HTTP methods do not require CSRF protection
  /^(GET|HEAD|OPTIONS|TRACE)$/.test method

$.ajaxSetup beforeSend: (xhr, settings) ->
  if !csrfSafeMethod(settings.type) and !@crossDomain
    xhr.setRequestHeader 'X-CSRFToken', csrftoken