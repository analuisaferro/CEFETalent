window.onload = function () {
  create_outro("tipos_atividade", true);
  create_outro("formato_atividade", false);
};

function create_outro(name, is_checkbox) {
  const wrapper_tipos = document.querySelector(`#id_${name}`);
  const div = document.createElement("div");
  div.className = "outro_wrapper";

  const checkbox = document.createElement("input");
  checkbox.type = is_checkbox ? "checkbox" : "radio";
  checkbox.id = `outro_${name}_checkbox`;
  checkbox.className = "form-check-input";
  checkbox.name = is_checkbox ? "" : name;
  div.appendChild(checkbox);

  const text_input = document.createElement("input");
  text_input.type = "text";
  text_input.name = `outro_${name}`;
  text_input.className = "form-control half";
  text_input.id = `outro_${name}_text_input`;
  text_input.placeholder = "Outro";
  text_input.disabled = true;
  div.appendChild(text_input);

  wrapper_tipos.appendChild(div);

  if (is_checkbox) {
    document
      .querySelector(`#outro_${name}_checkbox`)
      .addEventListener("change", (e) => {
        const text_input = document.querySelector(`#outro_${name}_text_input`);
        if (e.target.checked) {
          text_input.disabled = false;
          setRequired(text_input);
        } else {
          text_input.disabled = true;
          text_input.value = "";
          removeRequired(text_input);
        }
      });

    // document
    //   .querySelector(`#outro_${name}_text_input`)
    //   .addEventListener("input", (e) => {
    //     document.querySelector(`#outro_${name}_checkbox`).value =
    //       e.target.value;
    //   });
  } else {
    document.querySelector(`#id_${name}`).addEventListener("change", (e) => {
      const text_input = document.querySelector(`#outro_${name}_text_input`);
      if (e.target.id == `outro_${name}_checkbox`) {
        text_input.disabled = false;
        setRequired(text_input);
      } else {
        text_input.disabled = true;
        text_input.value = "";
        removeRequired(text_input);
      }
    });
    document
      .querySelector(`#outro_${name}_text_input`)
      .addEventListener("input", (e) => {
        document.querySelector(`#outro_${name}_checkbox`).value =
          e.target.value;
      });
  }
}
