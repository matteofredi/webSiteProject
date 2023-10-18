document.addEventListener('DOMContentLoaded', () => {
    let logoutButton = document.querySelector('#logout')

    logoutButton.addEventListener('click', () => {
        let url = 'http://localhost:8000/logout'
        let options = {
            method: 'GET'
        }

        fetch(url, options)
            .then(res => res.json())
            .then(res => window.location.replace(res))
            .catch(e => {
                console.log(e);
                alert('something gone wrong')
            })
    })
})