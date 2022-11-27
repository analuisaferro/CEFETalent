class AcceptDeclineModal {
    static remove() {
      document.querySelector(".modaladm").remove();
    }
  
    static dispatch(text) {
      const modalDiv = `<div class="modaladm" id='modal' tabindex="-1" role="dialog">
          <div class="message m-3">
            <h4>Atenção!</h2>
            <hr/>
            <p class="">${text}</p>
          </div>
        
          <div class="btn-modal d-flex flex-row-reverse mb-3">
              <button class="btn btn-primary mx-3" id='agree'>Excluir</button>
              <button class="btn btn-secondary" id='decline'>Cancelar</button>
          </div>
        </div>`;
  
      document.querySelector(".warnings").innerHTML = modalDiv;
      const agree = document.querySelector("#agree");
      const decline = document.querySelector("#decline");
  
      return new Promise((resolve, reject) => {
        decline.addEventListener("click", () => {
          AcceptDeclineModal.remove();
          resolve(false);
        });
        agree.addEventListener("click", () => {
          AcceptDeclineModal.remove();
          resolve(true);
        });
      });
    }
  }
  
  class Message {
    static alerts = [];
  
    static remove(e) {
      const index = Message.alerts.find((warning, index) => {
        if (`${index}-button` == e.id) return index;
      });
  
      Message.alerts.splice(index, 1);
      console.log(Message.alerts.length);
      const messageDiv = document.querySelector(".message");
  
      Message.alerts.length == 0 && messageDiv
        ? messageDiv.remove()
        : e.parentNode.remove();
    }
  
    static push(text, mode=null) {
      Message.alerts.push({ text, mode });
      console.log(text)
      Message.render();
    }
  
    static render() {
      const modalDiv = `
          <div class="modaladm message" id='modal' tabindex="-1" role="dialog">
          ${Message.alerts.map(
            (e, index) =>
              `<div class="message m-3 "><button id="${index}-button">X</button><p class="first-text">${e.text}</p></div>`
          )} 
        </div>
        `;
  
      const warnings = document.querySelector(".warnings");
      warnings.innerHTML = modalDiv;
  
      warnings.querySelectorAll("button").forEach((e) => {
        console.log(e)
        e.addEventListener("click", (e) => {
          Message.remove(e.target);
        });
      });
    }
  }