wreqr = require 'backbone.wreqr'

module.exports =
  vent: new wreqr.EventAggregator()
  reqres: new wreqr.RequestResponse()