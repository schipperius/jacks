document.querySelectorAll('.offcanvas a').forEach(link => {
  link.addEventListener('click', () => {
    const offcanvas = bootstrap.Offcanvas.getInstance(
      document.getElementById('offcanvasNavbar')
    )
    offcanvas?.hide()
  })
})
