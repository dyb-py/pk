from car import Car

def show_car(request):
    #Car对象要存到SESSION里面
    if request.SESSION.get('car') is None:
        car = Car()
    else:
        car = request.SESSION.get('car')
    car.add_car(1)
    request.SESSION['car'] = car
    return render('car.html',{'car':car})

def show_car2(request):
    car = request.SESSION.get('car')