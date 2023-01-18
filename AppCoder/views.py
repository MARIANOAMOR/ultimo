from django.shortcuts import render,redirect
from AppCoder.models import Canal
# Create your views here.
def inicio(request):

      return render(request, "AppCoder/inicio.html")

# Create your views here.
from AppCoder.forms import canalFormulario
def formularioCargarCanal(request):
      if request.method == "POST":
            miFormulario = canalFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  canal = Canal(nombre=informacion['nombre'], descripcion=informacion['descripcion'],
                        campo1=informacion['campo1'], campo2=informacion['campo2'],
                        campo3=informacion['campo3'], campo4=informacion['campo4'],
                        campo5=informacion['campo6'], campo6=informacion['campo6'],
                        campo7=informacion['campo7'], campo8=informacion['campo8'])
                  canal.save()
                  return redirect("AgregarCanales") 
                  #return render(request, "AppCoder/canales.html") #Vuelvo al inicio o a donde quieran
      else:
            miFormulario = canalFormulario()
      return render(request, "AppCoder/AgregarCanales.html", {"miFormulario": miFormulario})


#def formularioMostrarCanal(request, canalblock_id=2):
    #canalBlock_name = Canal.objects.get(nombre=canalblock_id)
    #canals_description = list(Canal.objects.filter(canals_canalblock_id=canalblock_id))
    #context = {
    #    "nombre": canalBlock_name, 
    #    "descripcion":canals_description,
    #    "campo1": canalBlock_name1, 
    #    "campo2": canals_description2,
    #    "campo3": canalBlock_name, 
    #    "campo4": canals_description,
    #    "campo5": canalBlock_name, 
    #    "campo6": canals_description,
    #    "campo7": canalBlock_name, 
    #    "campo8": canals_description

    #}
    #return render_to_response('MostrarCanales.html', context)

#Para obtener todos los registros de la tabla Canal 
from django.views.generic import ListView
class ContactoListar(ListView): 
    model = Canal


def editarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre) # Recibe el nombre del profesor que vamos a modificar  
    if request.method == 'POST': # Si es metodo POST hago lo mismo que el agregar
        # aquí mellega toda la información del html
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            profesor.save()
            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido,
                                                   'email': profesor.email, 'profesion': profesor.profesion})
    # Voy al html que me permite editar
    return render(request, "AppCoder/editarProfesor.html", {"miFormulario": miFormulario, "profesor_nombre": profesor_nombre})

from django.views.generic import ListView
class CursoList(ListView):
    model = Canal
    template_name = "AppCoder/cursos_list.html"

from django.views.generic.detail import DetailView
class CursoDetalle(DetailView):
    model = Canal
    template_name = "AppCoder/curso_detalle.html"
    
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class CursoCreacion(CreateView):
    model = Canal
    success_url = "/AppCoder/curso_list.html"#/.html
    fields = ['nombre', 'descripcion','campo1','campo2','campo3','campo4','campo5','campo6','campo7','campo8']

from django.views.generic.edit import UpdateView
class CursoUpdate(UpdateView):
    model = Canal
    success_url = "AppCoder/cursos_list.html"#"/AppCoder/curso/list"
    fields = ['nombre', 'descripcion','campo1','campo2','campo3','campo4','campo5','campo6','campo7','campo8']

from django.views.generic.edit import DeleteView
class CursoDelete(DeleteView):
    model = Canal
    success_url = "AppCoder/cursos_list.html"#"/AppCoder/curso/list"