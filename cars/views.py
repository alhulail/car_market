from django.shortcuts import render, reverse
from .models import Car
from .forms import CarForm

def car_list(request):
	context = {
		"cars":Car.objects.all()
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	context = {
		"car": Car.objects.get(id=car_id)
	}
	return render(request, 'car_detail.html', context)


def car_create(request, car_id):
    form = CarForm()
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('car-list')
    context = {
        "form":form,
		"car_id": car_id,
    }
    return render(request, 'car_create.html', context)


def car_update(request, car_id):
    car_obj = car.objects.get(id=car_id)
    if not (request.user.is_staff or request.user == car_obj.owner):
        return redirect('no-access')
    form = CarForm(instance=car_obj)
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car_obj)
        if form.is_valid():
            form.save()
            return redirect('car-list')
    context = {
        "car_obj": car_obj,
        "form":form,
    }
    return render(request, 'car_update.html', context)


def car_delete(request, car_id):
	#Complete Me
	return render(...)
