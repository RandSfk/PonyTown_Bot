// Buat elemen container form
var formContainer = document.createElement('div');
formContainer.classList.add('form-container');
document.body.appendChild(formContainer);

// Judul Form
var formTitle = document.createElement('h2');
formTitle.textContent = 'PonyTown Bot';
formContainer.appendChild(formTitle);

// Formulir
var botForm = document.createElement('form');
botForm.id = 'botForm';
formContainer.appendChild(botForm);

// Input Bot Name
var botNameInput = document.createElement('input');
botNameInput.type = 'text';
botNameInput.id = 'botName';
botNameInput.name = 'botName';
botNameInput.placeholder = 'Masukkan nama bot';
botNameInput.required = true;
botForm.appendChild(botNameInput);
botForm.appendChild(document.createElement('br'));

// Input Owner
var ownerInput = document.createElement('input');
ownerInput.type = 'text';
ownerInput.id = 'owner';
ownerInput.name = 'owner';
ownerInput.placeholder = 'Masukkan nama owner';
ownerInput.required = true;
botForm.appendChild(ownerInput);
botForm.appendChild(document.createElement('br'));

// Tombol Submit
var submitButton = document.createElement('button');
submitButton.type = 'submit';
submitButton.textContent = 'Simpan';
botForm.appendChild(submitButton);

// Tombol Close
var closeButton = document.createElement('button');
closeButton.type = 'button';
closeButton.textContent = 'Tutup';
botForm.appendChild(closeButton);

// Styling dengan JavaScript
formContainer.style.position = 'fixed';
formContainer.style.top = '50%';
formContainer.style.left = '50%';
formContainer.style.transform = 'translate(-50%, -50%)';
formContainer.style.maxWidth = '600px';  // Menyesuaikan lebar form
formContainer.style.padding = '20px';
formContainer.style.border = '1px solid #ccc';
formContainer.style.backgroundColor = '#3b3b3b';
formContainer.style.borderRadius = '5px';
formContainer.style.zIndex = '9999';

formTitle.style.textAlign = 'center';
formTitle.style.marginBottom = '20px';
formTitle.style.color = 'white';  // Warna teks judul menjadi putih

botForm.style.display = 'flex';
botForm.style.flexDirection = 'column';

var formElements = botForm.querySelectorAll('input, button');
formElements.forEach(function(element) {
    element.style.marginBottom = '10px';
    element.style.padding = '10px';
    element.style.fontSize = '16px';
    element.style.border = '1px solid #ccc';
    element.style.borderRadius = '4px';
    element.style.boxSizing = 'border-box';
    if (element.tagName === 'INPUT') {
        element.style.width = '100%';  // Memastikan input memenuhi lebar form
    }
});

submitButton.style.backgroundColor = '#007bff';
submitButton.style.color = 'white';
submitButton.style.border = 'none';
submitButton.style.cursor = 'pointer';

closeButton.style.backgroundColor = '#dc3545';
closeButton.style.color = 'white';
closeButton.style.border = 'none';
closeButton.style.cursor = 'pointer';
closeButton.style.marginTop = '10px';

// Menyembunyikan elemen saat form muncul
var formGroupTextCenter = document.querySelector('.form-group.text-center');
var rulesContainer = document.querySelector('.mx-auto.text-start.text-large');

if (formGroupTextCenter) formGroupTextCenter.style.display = 'none';
if (rulesContainer) rulesContainer.style.display = 'none';

// Event Listener Form
botForm.addEventListener('submit', function(event) {
    event.preventDefault();
    var botName = document.getElementById('botName').value;
    var owner = document.getElementById('owner').value;

    fetch('http://localhost:5000/api/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ botName: botName, owner: owner })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        if (data.success) {
            if (formGroupTextCenter) formGroupTextCenter.style.display = 'block';
            if (rulesContainer) rulesContainer.style.display = 'block';
            formContainer.style.display = 'none';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Event Listener Close Button
closeButton.addEventListener('click', function() {
    if (formGroupTextCenter) formGroupTextCenter.style.display = 'block';
    if (rulesContainer) rulesContainer.style.display = 'block';
    formContainer.style.display = 'none';
});
