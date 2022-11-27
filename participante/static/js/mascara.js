function leech(v) {
  v = v.replace(/o/gi, "0");
  v = v.replace(/i/gi, "1");
  v = v.replace(/z/gi, "2");
  v = v.replace(/e/gi, "3");
  v = v.replace(/a/gi, "4");
  v = v.replace(/s/gi, "5");
  v = v.replace(/t/gi, "7");
  return v;
}

function data(v) {
  v = v.replace(/\D/g, ""); //Remove tudo o que nao e digito
  v = v.replace(/(\d{2})(\d)/, "$1/$2"); //Coloca um ponto entre o terceiro e o quarto digitos
  v = v.replace(/(\d{2})(\d)/, "$1/$2"); //Coloca um ponto entre o terceiro e o quarto digitos
  //de novo (para o segundo bloco de numeros)
  return v;
}

function icpf(v) {
  v = v.replace(/\D/g, ""); //Remove tudo o que nao e digito
  v = v.replace(/(\d{3})(\d)/, "$1.$2"); //Coloca um ponto entre o terceiro e o quarto digitos
  v = v.replace(/(\d{3})(\d)/, "$1.$2"); //Coloca um ponto entre o terceiro e o quarto digitos
  //de novo (para o segundo bloco de numeros)
  v = v.replace(/(\d{3})(\d{1,2})$/, "$1-$2"); //Coloca um hifen entre o terceiro e o quarto digitos
  return v;
}

function itelefone(v) {
  v = v.replace(/\D/g, ""); //Remove tudo o que nao e digito
  v = v.replace(/^(\d\d)(\d)/g, "($1) $2"); //Coloca parenteses em volta dos dois primeiros digitos
  v = v.replace(/(\d{4})(\d)/, "$1-$2"); //Coloca hifen entre o quarto e o quinto digitos
  return v;
}

function icep(v) {
  v = v.replace(/\D/g, ""); //Remove tudo o que nao e digito
  v = v.replace(/(\d{2})(\d)/, "$1.$2"); //Coloca hifen entre o quarto e o quinto digitos
  v = v.replace(/(\d{3})(\d)/, "$1-$2"); //Coloca hifen entre o quarto e o quinto digitos
  return v;
}

function icelular(v) {
  v = v.replace(/\D/g, ""); //Remove tudo o que nao e digito
  v = v.replace(/^(\d\d)(\d)/g, "($1) $2"); //Coloca parenteses em volta dos dois primeiros digitos
  v = v.replace(/(\d{5})(\d)/, "$1-$2"); //Coloca hifen entre o quarto e o quinto digitos
  return v;
}

function iuppercase(v){
  return v.toUpperCase()
}

function icapitalize(v){
  return v.charAt(0).toUpperCase() + v.slice(1)
}

function mascara(o, f) {
  v_obj = o;
  v_fun = f;
  setTimeout(execmascara, 1);
}

function execmascara() {
  v_obj.value = v_fun(v_obj.value);
}

function hide(...elements) {
  elements.forEach((e) => {
    e.style.display = "none";
    e.querySelector("input").value = "";
  });
}

function show(...elements) {
  elements.forEach((e) => {
    e.style.display = "block";
  });
}

function setRequired(...elements) {
  elements.forEach((e) => {
    e.querySelector("input").setAttribute("required", "");
  });
}

function removeRequired(...elements) {
  elements.forEach((e) => {
    e.querySelector("input").removeAttribute("required");
  });
}
