function validarLogin(){
    const helpUser = document.getElementById('helpIdUser')
    const helpPass = document.getElementById('helpIdPass')
    const user = document.getElementById('usuario').value
    const pass = document.getElementById('contrasenia').value

    if(user==""){
        helpUser.innerHTML = "Debe ingresar un nombre de usuario"
        helpPass.innerHTML = ""
        return false
    }else if(pass==""){
        helpUser.innerHTML = ""
        helpPass.innerHTML = "Debe ingresar una contraseña"
        return false
    }else if(user!="User1" || pass!="Pass1"){
        helpUser.innerHTML = ""
        helpPass.innerHTML = "Usuario y contraseña invalidos"
        return false
    }else{
        return true
    }
}

function validarSignup(){
    const helpNombre = document.getElementById('helpIdNombre')
    const helpApellido = document.getElementById('helpIdApellido')
    const helpUsuario = document.getElementById('helpIdUsuario')
    const helpCorreo = document.getElementById('helpIdCorreo')
    const helpCont = document.getElementById('helpIdCont')
    const helpRepecont = document.getElementById('helpIdRepecont')
    const nombre = document.getElementById('nombre').value
    const apellido = document.getElementById('apellido').value
    const usuario = document.getElementById('usuario').value
    const correo = document.getElementById('correo').value
    const cont = document.getElementById('contrasenia').value
    const repecont = document.getElementById('repetir').value

    if(nombre==""){
        helpNombre.innerHTML = "Debe ingresar su nombre"
        helpApellido.innerHTML = ""
        helpUsuario.innerHTML = ""
        helpCorreo.innerHTML = ""
        helpCont.innerHTML = ""
        helpRepecont.innerHTML = ""
        return false
    }else if(apellido==""){
        helpNombre.innerHTML = ""
        helpApellido.innerHTML = "Debe ingresar su apellido"
        helpUsuario.innerHTML = ""
        helpCorreo.innerHTML = ""
        helpCont.innerHTML = ""
        helpRepecont.innerHTML = ""
        return false
    }else if(usuario==""){
        helpNombre.innerHTML = ""
        helpApellido.innerHTML = ""
        helpUsuario.innerHTML = "Debe ingresar un nombre de usuario"
        helpCorreo.innerHTML = ""
        helpCont.innerHTML = ""
        helpRepecont.innerHTML = ""
        return false
    }else if(correo==""){
        helpNombre.innerHTML = ""
        helpApellido.innerHTML = ""
        helpUsuario.innerHTML = ""
        helpCorreo.innerHTML = "Debe ingresar su correo electrónico"
        helpCont.innerHTML = ""
        helpRepecont.innerHTML = ""
        return false
    }else if(cont==""){
        helpNombre.innerHTML = ""
        helpApellido.innerHTML = ""
        helpUsuario.innerHTML = ""
        helpCorreo.innerHTML = ""
        helpCont.innerHTML = "Debe ingresar una contraseña"
        helpRepecont.innerHTML = ""
        return false
    }else if(repecont==""){
        helpNombre.innerHTML = ""
        helpApellido.innerHTML = ""
        helpUsuario.innerHTML = ""
        helpCorreo.innerHTML = ""
        helpCont.innerHTML = ""
        helpRepecont.innerHTML = "Debe confirmar la contraseña"
        return false
    }else if(cont!=repecont){
        helpNombre.innerHTML = ""
        helpApellido.innerHTML = ""
        helpUsuario.innerHTML = ""
        helpCorreo.innerHTML = ""
        helpCont.innerHTML = ""
        helpRepecont.innerHTML = "La contraseña no coincide"
        return false
    }else{
        return true
    }
}