module.exports = ->
  $('#homeCarousel').carousel interval: false
  $('.multi-item-carousel .item').each ->
    next = $(this).next()
    if !next.length
      next = $(this).siblings(':first')
    next.children(':first-child').clone().appendTo $(this)
    if next.next().length > 0
      next.next().children(':first-child').clone().appendTo $(this)
    else
      $(this).siblings(':first').children(':first-child').clone().appendTo $(this)

  height = $(window).height()
  $('.container_welcome').css 'height', height

  $('.arrow_bottom').on 'click', (event)=>
    event.preventDefault()
    target = $('.navbar')
    $('html, body').animate
      scrollTop: target.offset().top
    , 1000
