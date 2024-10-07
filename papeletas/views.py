from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Conductor, Infraccion, Papeleta
from .serializers import ConductorSerializer, InfraccionSerializer, PapeletaSerializer

def inicio(request):
    return render(request, 'papeletas/inicio.html')
class CRUDView(View):
    model = None
    template_name = ''
    redirect_url = ''
    
    def get(self, request):
        objects = self.model.objects.all()
        return render(request, self.template_name + '_list.html', {self.model.__name__.lower() + 's': objects})

    def post(self, request):
        obj = self.model(**self.get_data(request))
        obj.save()
        return redirect(self.redirect_url)

    def get_data(self, request):
        return {field.name: request.POST[field.name] for field in self.model._meta.fields}

    def get_object(self, id):
        return get_object_or_404(self.model, id=id)

class ConductorView(CRUDView):
    model = Conductor
    template_name = 'papeletas/conductor'
    redirect_url = 'listar_conductores'

class InfraccionView(CRUDView):
    model = Infraccion
    template_name = 'papeletas/infraccion'
    redirect_url = 'listar_infracciones'

class PapeletaView(CRUDView):
    model = Papeleta
    template_name = 'papeletas/papeleta'
    redirect_url = 'listar_papeletas'

# Vista para eliminar un objeto
def eliminar(request, model, id):
    obj = get_object_or_404(model, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect(f'listar_{model.__name__.lower()}s')
    return render(request, f'papeletas/{model.__name__.lower()}_confirm_delete.html', {'object': obj})

# Vistas específicas para las operaciones
def listar_conductores(request):
    conductores = Conductor.objects.all()  # Recuperar todos los conductores
    return render(request, 'papeletas/conductor_list.html', {'conductores': conductores})

def crear_conductor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        licencia = request.POST.get('licencia')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        imagen = request.FILES.get('imagen')  # Manejar la imagen
        
        # Asegúrate de que los campos no son None o vacíos si eso es necesario
        if nombre and licencia and direccion and telefono:  # Verifica que los campos no estén vacíos
            conductor = Conductor(nombre=nombre, licencia=licencia, direccion=direccion, telefono=telefono, imagen=imagen)
            conductor.save()
            return redirect('listar_conductores')
    return render(request, 'papeletas/conductor_form.html')

def editar_conductor(request, id):
    conductor = get_object_or_404(Conductor, id=id)
    if request.method == 'POST':
        conductor.nombre = request.POST.get('nombre', conductor.nombre)
        conductor.licencia = request.POST.get('licencia', conductor.licencia)
        conductor.direccion = request.POST.get('direccion', conductor.direccion)
        conductor.telefono = request.POST.get('telefono', conductor.telefono)

        # Actualiza la imagen solo si se ha proporcionado una nueva
        if 'imagen' in request.FILES:
            conductor.imagen = request.FILES['imagen']
        
        conductor.save()
        return redirect('listar_conductores')
    return render(request, 'papeletas/conductor_form.html', {'conductor': conductor})

def eliminar_conductor(request, id):
    return eliminar(request, Conductor, id)

def listar_infracciones(request):
    return InfraccionView.as_view()(request)

def crear_infraccion(request):
    if request.method == 'POST':
        return InfraccionView.as_view()(request)
    return render(request, 'papeletas/infraccion_form.html')

def editar_infraccion(request, id):
    infraccion = get_object_or_404(Infraccion, id=id)
    if request.method == 'POST':
        infraccion.descripcion = request.POST.get('descripcion', infraccion.descripcion)
        infraccion.save()
        return redirect('listar_infracciones')
    return render(request, 'papeletas/infraccion_form.html', {'infraccion': infraccion})

def eliminar_infraccion(request, id):
    return eliminar(request, Infraccion, id)

def listar_papeletas(request):
    return PapeletaView.as_view()(request)

def crear_papeleta(request):
    if request.method == 'POST':
        return PapeletaView.as_view()(request)
    return render(request, 'papeletas/papeleta_form.html')

def editar_papeleta(request, id):
    papeleta = get_object_or_404(Papeleta, id=id)
    if request.method == 'POST':
        papeleta.conductor_id = request.POST.get('conductor_id', papeleta.conductor_id)
        papeleta.infraccion_id = request.POST.get('infraccion_id', papeleta.infraccion_id)
        papeleta.fecha = request.POST.get('fecha', papeleta.fecha)
        papeleta.save()
        return redirect('listar_papeletas')
    return render(request, 'papeletas/papeleta_form.html', {'papeleta': papeleta})

def eliminar_papeleta(request, id):
    return eliminar(request, Papeleta, id)
