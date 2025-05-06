from django.shortcuts import render
from app.clases.usuarios import Usuario

def home_view(request):
    return render(request, 'home.html')

def registro_usuario(request):
    mensaje = None
    if request.method == 'POST':
        if request.POST.get('contrasenia') != request.POST.get('confirmar_contrasenia'):
            mensaje = "Las contraseñas no coinciden"
        else:
            Usuario.objects.create(
                nombre=request.POST.get('nombre'),
                apellido=request.POST.get('apellido'),
                dni=request.POST.get('dni'),
                pais=request.POST.get('pais'),
                provincia=request.POST.get('provincia'),
                email=request.POST.get('mail'),
                telefono=request.POST.get('telefono'),
                contrasenia=request.POST.get('contrasenia'),
                fecha_nacimiento=request.POST.get('fecha_nacimiento'),
                sexo=request.POST.get('sexo'),
                numero_billetera="TEMP123"  # en el futuro podés generar uno
            )
            mensaje = "Usuario registrado con éxito"
    
    return render(request, 'registro.html', {'mensaje': mensaje})
