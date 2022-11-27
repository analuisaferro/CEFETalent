window.onload = function(){
    const wrapper_tipos = document.querySelector('#id_tipos_atividade')
    const div = document.createElement('div')
    div.className = 'form-check outro'
    const label = document.createElement('label')
    label.className = 'form-check-label'
    label.htmlFor = 'outro_tipo_atividade'
    
    const checkbox = document.createElement('input')
    checkbox.type = 'checkbox'
    checkbox.id = 'outro_tipo_atividade_checkbox'
    label.appendChild(checkbox)
    label.appendChild()

    div.append(label)
    wrapper_tipos.appendChild(div)

    wrapper_formatos = document.querySelector('#id_formatos_atividade')

}