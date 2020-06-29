from django.shortcuts import (
    get_object_or_404,
    render,
    redirect,
    HttpResponseRedirect,
    reverse
)
from .models import BlogModel
from .forms import BlogForm




def index(request):
    return render(request, 'CRUD_app/index.html')

def create_view(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Data saved successfully."
            return render(request, "CRUD_app/success.html", {'message': message})
        else:
            print(form.errors)
            message = "Something Went Wrong."
            return render(request, "CRUD_app/error.html", {'message': message})
    else:
        form = BlogForm()
        return render(request, "CRUD_app/form.html", {'form': form})

def list_view(request):
    Blogs = BlogModel.objects.all()
    return render(request, 'CRUD_app/list_view.html', {'dataset':Blogs})

def detail_view(request, id):
    data = BlogModel.objects.get(id=id)
    return render(request, 'CRUD_app/detail_view.html', {'data': data})

def update_view(request, id):
    # fetch the object related to passed id 
    obj = get_object_or_404(BlogModel, id = id) 
    
    if request.method == "POST":
    
        # pass the object as instance in form 
        form = BlogForm(request.POST, instance = obj) 
    
        # save the data from the form and 
        # redirect to detail_view 
        if form.is_valid(): 
            form.save() 
            #return redirect("/detail_view/"+id) # absolute path
            return HttpResponseRedirect(reverse('detail_view', args=(id,))) # Calling via url name
        else:
            print(form.errors)
            message = "Something Went Wrong."
            return render(request, "CRUD_app/error.html", {'message': message})
    else:
        form = BlogForm(instance=obj)
        return render(request, "CRUD_app/update_view.html", {'form':form})


def delete_view(request, id):
    obj = get_object_or_404(BlogModel, id = id)
    obj.delete()
    return HttpResponseRedirect(reverse('list_view'))