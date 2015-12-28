$ = require 'jquery'

toFix = [
  'wheel'
  'mousewheel'
  'DOMMouseScroll'
  'MozMousePixelScroll'
]
toBind = if 'onwheel' of document or document.documentMode >= 9 then [ 'wheel' ] else [
  'mousewheel'
  'DomMouseScroll'
  'MozMousePixelScroll'
]
slice = Array::slice
nullLowestDeltaTimeout = undefined
lowestDelta = undefined

handler = (event) ->
  orgEvent = event or window.event
  args = slice.call(arguments, 1)
  delta = 0
  deltaX = 0
  deltaY = 0
  absDelta = 0
  offsetX = 0
  offsetY = 0
  event = $.event.fix(orgEvent)
  event.type = 'mousewheel'
  # Old school scrollwheel delta
  if 'detail' of orgEvent
    deltaY = orgEvent.detail * -1
  if 'wheelDelta' of orgEvent
    deltaY = orgEvent.wheelDelta
  if 'wheelDeltaY' of orgEvent
    deltaY = orgEvent.wheelDeltaY
  if 'wheelDeltaX' of orgEvent
    deltaX = orgEvent.wheelDeltaX * -1
  # Firefox < 17 horizontal scrolling related to DOMMouseScroll event
  if 'axis' of orgEvent and orgEvent.axis == orgEvent.HORIZONTAL_AXIS
    deltaX = deltaY * -1
    deltaY = 0
  # Set delta to be deltaY or deltaX if deltaY is 0 for backwards compatabilitiy
  delta = if deltaY == 0 then deltaX else deltaY
  # New school wheel delta (wheel event)
  if 'deltaY' of orgEvent
    deltaY = orgEvent.deltaY * -1
    delta = deltaY
  if 'deltaX' of orgEvent
    deltaX = orgEvent.deltaX
    if deltaY == 0
      delta = deltaX * -1
  # No change actually happened, no reason to go any further
  if deltaY == 0 and deltaX == 0
    return
  # Need to convert lines and pages to pixels if we aren't already in pixels
  # There are three delta modes:
  #   * deltaMode 0 is by pixels, nothing to do
  #   * deltaMode 1 is by lines
  #   * deltaMode 2 is by pages
  if orgEvent.deltaMode == 1
    lineHeight = $.data(this, 'mousewheel-line-height')
    delta *= lineHeight
    deltaY *= lineHeight
    deltaX *= lineHeight
  else if orgEvent.deltaMode == 2
    pageHeight = $.data(this, 'mousewheel-page-height')
    delta *= pageHeight
    deltaY *= pageHeight
    deltaX *= pageHeight
  # Store lowest absolute delta to normalize the delta values
  absDelta = Math.max(Math.abs(deltaY), Math.abs(deltaX))
  if !lowestDelta or absDelta < lowestDelta
    lowestDelta = absDelta
    # Adjust older deltas if necessary
    if shouldAdjustOldDeltas(orgEvent, absDelta)
      lowestDelta /= 40
  # Adjust older deltas if necessary
  if shouldAdjustOldDeltas(orgEvent, absDelta)
    # Divide all the things by 40!
    delta /= 40
    deltaX /= 40
    deltaY /= 40
  # Get a whole, normalized value for the deltas
  delta = Math[if delta >= 1 then 'floor' else 'ceil'](delta / lowestDelta)
  deltaX = Math[if deltaX >= 1 then 'floor' else 'ceil'](deltaX / lowestDelta)
  deltaY = Math[if deltaY >= 1 then 'floor' else 'ceil'](deltaY / lowestDelta)
  # Normalise offsetX and offsetY properties
  if special.settings.normalizeOffset and @getBoundingClientRect
    boundingRect = @getBoundingClientRect()
    offsetX = event.clientX - (boundingRect.left)
    offsetY = event.clientY - (boundingRect.top)
  # Add information to the event object
  event.deltaX = deltaX
  event.deltaY = deltaY
  event.deltaFactor = lowestDelta
  event.offsetX = offsetX
  event.offsetY = offsetY
  # Go ahead and set deltaMode to 0 since we converted to pixels
  # Although this is a little odd since we overwrite the deltaX/Y
  # properties with normalized deltas.
  event.deltaMode = 0
  # Add event and delta to the front of the arguments
  args.unshift event, delta, deltaX, deltaY
  # Clearout lowestDelta after sometime to better
  # handle multiple device types that give different
  # a different lowestDelta
  # Ex: trackpad = 3 and mouse wheel = 120
  if nullLowestDeltaTimeout
    clearTimeout nullLowestDeltaTimeout
  nullLowestDeltaTimeout = setTimeout(nullLowestDelta, 200)
  ($.event.dispatch or $.event.handle).apply this, args

nullLowestDelta = ->
  lowestDelta = null
  return

shouldAdjustOldDeltas = (orgEvent, absDelta) ->
  # If this is an older event and the delta is divisable by 120,
  # then we are assuming that the browser is treating this as an
  # older mouse wheel event and that we should divide the deltas
  # by 40 to try and get a more usable deltaFactor.
  # Side note, this actually impacts the reported scroll distance
  # in older browsers and can cause scrolling to be slower than native.
  # Turn this off by setting $.event.special.mousewheel.settings.adjustOldDeltas to false.
  special.settings.adjustOldDeltas and orgEvent.type == 'mousewheel' and absDelta % 120 == 0

if $.event.fixHooks
  i = toFix.length
  while i
    $.event.fixHooks[toFix[--i]] = $.event.mouseHooks
special = $.event.special.mousewheel =
  version: '3.1.12'
  setup: ->
    `var i`
    if @addEventListener
      i = toBind.length
      while i
        @addEventListener toBind[--i], handler, false
    else
      @onmousewheel = handler
    # Store the line height and page height for this particular element
    $.data this, 'mousewheel-line-height', special.getLineHeight(this)
    $.data this, 'mousewheel-page-height', special.getPageHeight(this)
    return
  teardown: ->
    `var i`
    if @removeEventListener
      i = toBind.length
      while i
        @removeEventListener toBind[--i], handler, false
    else
      @onmousewheel = null
    # Clean up the data we added to the element
    $.removeData this, 'mousewheel-line-height'
    $.removeData this, 'mousewheel-page-height'
    return
  getLineHeight: (elem) ->
    $elem = $(elem)
    $parent = $elem[if 'offsetParent' of $.fn then 'offsetParent' else 'parent']()
    if !$parent.length
      $parent = $('body')
    parseInt($parent.css('fontSize'), 10) or parseInt($elem.css('fontSize'), 10) or 16
  getPageHeight: (elem) ->
    $(elem).height()
  settings:
    adjustOldDeltas: true
    normalizeOffset: true
$.fn.extend
  mousewheel: (fn) ->
    if fn then @bind('mousewheel', fn) else @trigger('mousewheel')
  unmousewheel: (fn) ->
    @unbind 'mousewheel', fn
