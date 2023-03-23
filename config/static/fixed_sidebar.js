setTimeout(() => {
    const navLinkActive = document.querySelectorAll('.sidebar .nav-item .nav-link')
    const sidebar = document.querySelector('.main-sidebar .sidebar')
    navLinkActive.forEach(n => {
        if (window.location.href.includes(n.href)) {
            sidebar.scrollTo({
                top: n.getBoundingClientRect().y - 200,
            })
        }
    })

}, 10)
