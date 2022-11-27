window.onload = function () {
  const wrapper_tipos = document.querySelector("#id_tipos_atividade");
  const div = document.createElement("div");
  div.className = "outro_wrapper"

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.id = "outro_tipo_atividade_checkbox";
  checkbox.className = "form-check-input";

  div.appendChild(checkbox);

  const text_input = document.createElement("input");
  text_input.type = "text";
  text_input.name = "outro_tipo_atividade";
  text_input.className = "form-control";
  text_input.id = "outro_tipo_atividade_checkbox";

  div.appendChild(text_input);

  wrapper_tipos.appendChild(div);

  wrapper_formatos = document.querySelector("#id_formatos_atividade");

  document
    .querySelector("#outro_tipo_atividade_checkbox")
    .addEventListener("change", (e) => {
      console.log(e.target.checked);
      if (e.target.checked) {
      }
    });
};
