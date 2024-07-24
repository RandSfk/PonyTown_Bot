(function() {
  var script = document.createElement('script');
  script.textContent = `
    // Your JavaScript code goes here
    var activeTab = 'local';
    var botName = '';

    const socket = new WebSocket('ws://localhost:5000');
    socket.addEventListener('open', (event) => {
        console.log('WebSocket connection established.');
    });
    socket.addEventListener('message', (event) => {
        const data = JSON.parse(event.data);
        if (data.move === false) {
            sendText(data.message);
        }
    });
    socket.addEventListener('error', (event) => {
        console.error('WebSocket error:', event);
    });
    socket.addEventListener('close', (event) => {
        console.log('WebSocket connection closed:', event);
    });

    var formContainer = document.createElement('div');
    formContainer.classList.add('form-container');
    document.body.appendChild(formContainer);
    var formTitle = document.createElement('h2');
    formTitle.textContent = 'PonyTown Bot';
    formContainer.appendChild(formTitle);

    var botForm = document.createElement('form');
    botForm.id = 'botForm';
    formContainer.appendChild(botForm);

    var botNameInput = document.createElement('input');
    botNameInput.type = 'text';
    botNameInput.id = 'botName';
    botNameInput.name = 'botName';
    botNameInput.placeholder = 'Masukkan nama bot';
    botNameInput.required = true;
    botForm.appendChild(botNameInput);
    botForm.appendChild(document.createElement('br'));

    var ownerInput = document.createElement('input');
    ownerInput.type = 'text';
    ownerInput.id = 'owner';
    ownerInput.name = 'owner';
    ownerInput.placeholder = 'Masukkan nama owner';
    ownerInput.required = true;
    botForm.appendChild(ownerInput);
    botForm.appendChild(document.createElement('br'));

    var submitButton = document.createElement('button');
    submitButton.type = 'submit';
    submitButton.textContent = 'Simpan';
    botForm.appendChild(submitButton);

    var closeButton = document.createElement('button');
    closeButton.type = 'button';
    closeButton.textContent = 'Tutup';
    botForm.appendChild(closeButton);

    formContainer.style.position = 'fixed';
    formContainer.style.top = '50%';
    formContainer.style.left = '50%';
    formContainer.style.transform = 'translate(-50%, -50%)';
    formContainer.style.maxWidth = '600px';
    formContainer.style.padding = '20px';
    formContainer.style.border = '1px solid #ccc';
    formContainer.style.backgroundColor = '#3b3b3b';
    formContainer.style.borderRadius = '5px';
    formContainer.style.zIndex = '9999';

    formTitle.style.textAlign = 'center';
    formTitle.style.marginBottom = '20px';
    formTitle.style.color = 'white';

    botForm.style.display = 'flex';
    botForm.style.flexDirection = 'column';

    var formElements = botForm.querySelectorAll('label, input, button');
    formElements.forEach(function(element) {
        element.style.marginBottom = '10px';
        if (element.tagName === 'INPUT' || element.tagName === 'BUTTON') {
            element.style.padding = '10px';
            element.style.fontSize = '16px';
            element.style.border = '1px solid #ccc';
            element.style.borderRadius = '4px';
            element.style.boxSizing = 'border-box';
            if (element.tagName === 'INPUT') {
                element.style.width = '100%';
            }
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

    var formGroupTextCenter = document.querySelector('.form-group.text-center');
    var rulesContainer = document.querySelector('.mx-auto.text-start.text-large');

    formGroupTextCenter.style.display = 'none';
    rulesContainer.style.display = 'none';

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
              formGroupTextCenter.style.display = 'block';
              rulesContainer.style.display = 'block';
              formContainer.style.display = 'none';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    closeButton.addEventListener('click', function() {
        formGroupTextCenter.style.display = 'block';
        rulesContainer.style.display = 'block';
        formContainer.style.display = 'none';
    });

    function sendText(text) {
      var textarea = document.querySelector('.chat-textarea');
      var uiButton = document.querySelector('ui-button[title="Send message (hold Shift to send without closing input)"]');
      if (textarea && uiButton) {
        textarea.value = text;
        var button = uiButton.querySelector('button');

        if (button) {
          button.click();
        }
      }
    }

    function sendTextApi(text) {
      if (socket.readyState === WebSocket.OPEN) {
          const data = { chatText: text };
          socket.send(JSON.stringify(data));
      } else {
          console.error('WebSocket connection is not open.');
      }
    }

    function sendKeyEvent(key, type) {
      var eventObj = document.createEventObject ?
        document.createEventObject() : document.createEvent("Events");

      if (eventObj.initEvent) {
        eventObj.initEvent(type, true, true);
      }

      eventObj.keyCode = key;
      eventObj.which = key;
      document.dispatchEvent ? document.dispatchEvent(eventObj) : document.fireEvent("on" + type, eventObj);
    }

    function moveUp() {
      sendKeyEvent(87, 'keydown');
      setTimeout(function () {
        sendKeyEvent(87, 'keyup');
      }, 100);
    }

    function moveDown() {
      sendKeyEvent(83, 'keydown');
      setTimeout(function () {
        sendKeyEvent(83, 'keyup');
      }, 100);
    }

    function moveLeft() {
      sendKeyEvent(65, 'keydown');
      setTimeout(function () {
        sendKeyEvent(65, 'keyup');
      }, 100);
    }

    function moveRight() {
      sendKeyEvent(68, 'keydown');
      setTimeout(function () {
        sendKeyEvent(68, 'keyup');
      }, 100);
    }

    function move(direction) {
      if (direction === 'w' || direction === 'up') {
        moveUp();
      } else if (direction === 's' || direction === 'down') {
        moveDown();
      } else if (direction === 'a' || direction === 'left') {
        moveLeft();
      } else if (direction === 'd' || direction === 'right') {
        moveRight();
      } else {
        console.error('Invalid direction:', direction);
      }
    }

    function getUsernameAndMessage(chatText) {
      var regex = /^\d{2}:\d{2}\[(.*?)\] (.*)$/;
      var match = chatText.match(regex);
      
      if (match) {
          var username = match[1]; 
          var message = match[2];
          
          return {
              username: username,
              message: message
          };
      } else {
          return null;
      }
    } 

    function ChatLog() {
      var alertInfo = document.querySelector('.alert.alert-info');
      if (alertInfo) {
        alertInfo.remove();
        return;
      }

      var chatLines = document.querySelectorAll('.chat-line');
      if (chatLines.length === 0) {
        let buttons = document.querySelectorAll('button[aria-haspopup="true"]');
        buttons.forEach(button => button.click());

        var dropdowns = document.querySelectorAll('div[role="menu"]');
        dropdowns.forEach(dropdown => {
            var closeButton = dropdown.querySelector('button[aria-label="Close"]');
            if (closeButton) {
                closeButton.click();
            }
        });
        return;
      }

      chatLines.forEach(line => {
        var chatText = line.innerText;
        var data = getUsernameAndMessage(chatText);
        
        if (data) {
          sendTextApi(data.message);
        }
      });
    }
  `;
  document.body.appendChild(script);
})();
