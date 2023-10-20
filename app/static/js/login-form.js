async function login(url, requestOptions) {
    let errorDiv = document.querySelector('#error-message')
    let loginDiv = document.querySelector('form')

    try {
        const response = await fetch(url, requestOptions);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        window.location.replace('http://localhost:8000/home');
    } catch (error) {
        loginDiv.style.display = 'none';
        errorDiv.style.display = 'flex'
    }
}


document.addEventListener('DOMContentLoaded', () => {
        let form = document.querySelector('form')
        let retryButton = document.querySelector('#retry-button')
        let errorDiv = document.querySelector('#error-message')

        form.addEventListener('submit', (event) => {
                event.preventDefault();
                let form = document.querySelector('form')
                let formData = new FormData(form);

                // const URL = 'http://localhost:8000/secure-data'
                // const requestOptions = {
                //     method: 'POST',
                //     body: (new URLSearchParams(formData)).toString(),
                //     headers: {"Content-type": "application/x-www-form-urlencoded"}
                // }

                const URL = 'http://localhost:8000/secure-data'
                let tokenB64 = btoa(formData.get('username') + ":" + formData.get('password'))

                const requestOptions = {
                    method: 'GET',
                    headers: {"Authorization": "Basic " + tokenB64}
                }

                login(URL, requestOptions);
            }
        )

        retryButton.addEventListener('click', () => {
                form.style.display = 'flex';
                errorDiv.style.display = 'none';
            }
        )

    }
)

