module.exports = ->
  $('#homeCarousel').carousel interval: false
  $('.multi-item-carousel .item').each ->
    next = $(@).next()
    if !next.length
      next = $(@).siblings(':first')
    next.children(':first-child').clone().appendTo $(@)
    if next.next().length > 0
      next.next().children(':first-child').clone().appendTo $(@)
    else
      $(@).siblings(':first').children(':first-child').clone().appendTo $(@)

  height = $(window).height()
  $('.container_welcome').css 'height', height

  $('.arrow_bottom').on 'click', (event)=>
    event.preventDefault()
    target = $('.navbar')
    $('html, body').animate
      scrollTop: target.offset().top
    , 1000
