from django.shortcuts import render
from django.http import JsonResponse
from zoodb.models import Animals, caretaker, donated_by


def get_animals(request):
    data = list(Animals.objects.all().values())
    return render(request,"zoo_animal.html",context={'animals':list(data)})
    

def get_caretakers(request):
    data = caretaker.objects.all()
    return render(request, "caretakers.html", {"caretakers": data})

def get_donors(request):
    data = donated_by.objects.all()
    return render(request, "donors.html", {"donors": data})


def add_animal(request):
    name = request.GET.get("name")
    species = request.GET.get("species")
    gender = request.GET.get("gender")
    age = request.GET.get("age")
    habitat = request.GET.get("habitat")
    Animals.objects.create(
        name=name,
        species=species,
        gender=gender,
        age=age,
        habitat=habitat
    )

    return JsonResponse({"message": "Animal Added Successfully"})

def update_animal(request):
    name_value=request.GET.get('name')
    species_value=request.GET.get('species')
    gender_value=request.GET.get('gender')
    age_value=request.GET.get('age')
    habitat_value=request.GET.get('habitat')
    
    animal=Animals.objects.get(name=name_value)
    animal.species=species_value
    animal.gender=gender_value
    animal.age=age_value
    animal.habitat=habitat_value
    
    animal.save()
    return JsonResponse({'message':'Event Updated','updated':{
        "name":animal.name,
        "species":animal.species,
        "gender":animal.gender,
        "age":animal.age,
        "habitat":animal.habitat
    }})

def delete_animal(request):
    name_value=request.GET.get('name')
    event=Animals.objects.get(name=name_value)
    event.delete()
    return JsonResponse({'message':'Animal Deleted'})




def display_landing(request):
    return render(request,"zoo.html")
tiger={
    'breed':'Tiger',
    'name':'ROYAL BENGAL TIGER',
    'title':'Bengal Tiger',
    'image':'https://cdn.britannica.com/62/104262-050-A5246CC2/Siberian-tiger.jpg',
    'age':20,
    'caretaker':"Ramesh",
    'Donated_by':'kolkata international zoo',
    'Food':'meat',
    'place':'Bengal',
     'donate':False,
    'description':'The Bengal Tiger is known for its rich orange coat with dark black stripes. It is the national animal of India and is powerful, agile, and graceful'
}
def display_tiger(request):
    return render(request,"animal.html",context=tiger)
lion={
    'breed':'Lion',
    'name':'AFRICAN LION',
    'title':'African Lion',
    'image':'https://cdn.wallpapersafari.com/70/54/TWAh5x.jpg',
    'age': '10 years',
    'caretaker':"Ramesh",
    'Donated_by':'kolkata international zoo',
    'Food':'meat',
    'place':'Bengal',
     'donate':True,
    'description':'The African lion is known for its rich orange coat with dark black stripes. It is the national animal of India and is powerful, agile, and graceful'
}
def display_lion(request):
    return render(request,"animal.html",context=lion)
elephant={
    'breed':'Elephant',
    'name':'Asian Elephant',
    'title':'Asian Elephant',
    'image':'https://images7.alphacoders.com/681/681042.jpg',
    'age':'60-70 years',
    'caretaker':"Samuel Dlamini",
    'Donated_by':'Kruger National Park',
    'Food':'Grasses,leaves',
    'place':'Tanzania',
    'donate': False,
    'description':'Slightly smaller than the African species, with smaller ears and a single “finger” on its trunk. Known for intelligence and loyalty. Commonly used in cultural festivals and logging work in Asia.'
}
def display_elephant(request):
    return render(request,"animal.html",context=elephant)
bear={
    'breed':'Bear',
    'name':'Polar Bear',
    'title':'Polar Bear',
    'image':'https://tse4.mm.bing.net/th/id/OIP.TqCGas7eubea27anuGNisgHaE8?cb=ucfimgc2&rs=1&pid=ImgDetMain&o=7&rm=3',
    'age':'20-25 years',
    'caretaker':"Robert",
    'Donated_by':'Alaska wildlife Conservation',
    'Food':'Seals,fish,birds',
    'place':'Greenland',
    'donate':False,
    'description':'The Polar Bear is the largest carnivorous land mammal, found in Arctic regions. It has thick white fur and a layer of fat to survive freezing temperatures. An excellent swimmer, it hunts seals on sea ice.'
}
def display_bear(request):
    return render(request,"animal.html",context=bear)
dolphin={
    'breed':'Dolphin',
    'name':'Bottlenose Dolphin',
    'title':'Bottlenose Dolphin',
    'image':'https://www.australiangeographic.com.au/wp-content/uploads/2023/01/shutterstock_1373689742-1800x1192.jpg',
    'age':'40-60 years',
    'caretaker':"sarah",
    'Donated_by':'Miami Seaquarium',
    'Food':'Seals,fish,birds',
    'place':'Greenland',
    'donate':True,
    'description':'The Polar Bear is the largest carnivorous land mammal, found in Arctic regions. It has thick white fur and a layer of fat to survive freezing temperatures. An excellent swimmer, it hunts seals on sea ice.'
}
def display_dolphin(request):
    return render(request,"animal.html",context=dolphin)
def animal_data(request):
    animals=[
        {
            'breed':'Tiger',
            'name':'ROYAL BENGAL TIGER',
            'title':'Bengal Tiger',
            'image':'https://cdn.britannica.com/62/104262-050-A5246CC2/Siberian-tiger.jpg',
            'age':20,
            'caretaker':"Ramesh",
            'Donated_by':'kolkata international zoo',
            'Food':'meat',
            'place':'Bengal',
            'donate':False,
            'description':'The Bengal Tiger is known for its rich orange coat with dark black stripes. It is the national animal of India and is powerful, agile, and graceful'

        },
        {
            'breed':'Lion',
            'name':'AFRICAN LION',
            'title':'African Lion',
            'image':'https://cdn.wallpapersafari.com/70/54/TWAh5x.jpg',
            'age': '10 years',
            'caretaker':"Ramesh",
            'Donated_by':'kolkata international zoo',
            'Food':'meat',
            'place':'Bengal',
            'donate':True,
            'description':'The African lion is known for its rich orange coat with dark black stripes. It is the national animal of India and is powerful, agile, and graceful',

        },
        {
    'breed':'Elephant',
    'name':'Asian Elephant',
    'title':'Asian Elephant',
    'image':'https://images7.alphacoders.com/681/681042.jpg',
    'age':'60-70 years',
    'caretaker':"Samuel Dlamini",
    'Donated_by':'Kruger National Park',
    'Food':'Grasses,leaves',
    'place':'Tanzania',
    'donate': False,
    'description':'Slightly smaller than the African species, with smaller ears and a single “finger” on its trunk. Known for intelligence and loyalty. Commonly used in cultural festivals and logging work in Asia.'
},
  {
    'breed':'Bear',
    'name':'Polar Bear',
    'title':'Polar Bear',
    'image':'https://tse4.mm.bing.net/th/id/OIP.TqCGas7eubea27anuGNisgHaE8?cb=ucfimgc2&rs=1&pid=ImgDetMain&o=7&rm=3',
    'age':'20-25 years',
    'caretaker':"Robert",
    'Donated_by':'Alaska wildlife Conservation',
    'Food':'Seals,fish,birds',
    'place':'Greenland',
    'donate':False,
    'description':'The Polar Bear is the largest carnivorous land mammal, found in Arctic regions. It has thick white fur and a layer of fat to survive freezing temperatures. An excellent swimmer, it hunts seals on sea ice.'
},
  {
    'breed':'Dolphin',
    'name':'Bottlenose Dolphin',
    'title':'Bottlenose Dolphin',
    'image':'https://www.australiangeographic.com.au/wp-content/uploads/2023/01/shutterstock_1373689742-1800x1192.jpg',
    'age':'40-60 years',
    'caretaker':"sarah",
    'Donated_by':'Miami Seaquarium',
    'Food':'Seals,fish,birds',
    'place':'Greenland',
    'donate':True,
    'description':'The Polar Bear is the largest carnivorous land mammal, found in Arctic regions. It has thick white fur and a layer of fat to survive freezing temperatures. An excellent swimmer, it hunts seals on sea ice.'
},
  {
    'breed':'Monkey',
    'name':'Monkey',
    'title':'Monkey',
    'image':'https://www.pixelstalk.net/wp-content/uploads/2016/05/Free-Monkey-Imgae-Download.jpg',
    'age':'40-60 years',
    'caretaker':"sarah",
    'Donated_by':'Miami Seaquarium',
    'Food':'Seals,fish,birds',
    'place':'Greenland',
    'donate':True,
    'description':'The Polar Bear is the largest carnivorous land mammal, found in Arctic regions. It has thick white fur and a layer of fat to survive freezing temperatures. An excellent swimmer, it hunts seals on sea ice.'
},
  
   {
    'breed':'Zebra',
    'name':'plain zebra',
    'title':'zebra',
    'image':'https://tse4.mm.bing.net/th/id/OIP.3D6CLMH8PUxG8y-gNv9jAAHaE8?cb=ucfimgc2&rs=1&pid=ImgDetMain&o=7&rm=3',
    'age':'40-60 years',
    'caretaker':"sarah",
    'Donated_by':'Miami Seaquarium',
    'Food':'Seals,fish,birds',
    'place':'Greenland',
    'donate':True,
    'description':'The Polar Bear is the largest carnivorous land mammal, found in Arctic regions. It has thick white fur and a layer of fat to survive freezing temperatures. An excellent swimmer, it hunts seals on sea ice.'
},
  
   {
    'breed':'ostrich',
    'name':'Dessert ostrich',
    'title':'ostrich',
    'image':'https://www.pixelstalk.net/wp-content/uploads/2016/05/Free-Monkey-Imgae-Download.jpg',
    'age':'40-60 years',
    'caretaker':"sarah",
    'Donated_by':'Miami Seaquarium',
    'Food':'Seals,fish,birds',
    'place':'Greenland',
    'donate':True,
    'description':'The Polar Bear is the largest carnivorous land mammal, found in Arctic regions. It has thick white fur and a layer of fat to survive freezing temperatures. An excellent swimmer, it hunts seals on sea ice.'
},
  {
    'breed':'Camel',
    'name':'Dessert camel',
    'title':'camel',
    'image':'https://www.pixelstalk.net/wp-content/uploads/2016/05/Free-Monkey-Imgae-Download.jpg',
    'age':'40-60 years',
    'caretaker':"sarah",
    'Donated_by':'Miami Seaquarium',
    'Food':'Seals,fish,birds',
    'place':'Greenland',
    'donate':True,
    'description':'The Polar Bear is the largest carnivorous land mammal, found in Arctic regions. It has thick white fur and a layer of fat to survive freezing temperatures. An excellent swimmer, it hunts seals on sea ice.'
},
  
  {
    'breed':'lepord',
    'name':'Indian leapord',
    'title':'leopard',
    'image':'https://www.pixelstalk.net/wp-content/uploads/2016/05/Free-Monkey-Imgae-Download.jpg',
    'age':'40-60 years',
    'caretaker':"sarah",
    'Donated_by':'Miami Seaquarium',
    'Food':'Seals,fish,birds',
    'place':'Greenland',
    'donate':True,
    'description':'The Polar Bear is the largest carnivorous land mammal, found in Arctic regions. It has thick white fur and a layer of fat to survive freezing temperatures. An excellent swimmer, it hunts seals on sea ice.'
},
]
    return JsonResponse({'status':200,'data':animals})  
def zoo_data(request):
    zoos=[
        {
            'name':'karnataka zoo',
            'location':'karnataka',
        },
        {
            'name':'maharastra zoo',
            'location':'maharastra',
        },
        {
            'name':'Bengal zoo',
            'location':'bengal',
        },
        {
            'name':'Bihar zoo',
            'location':'Bihar',
        },
        {
            'name':'Hydrerabad zoo',
            'location':'Hyderabad',
        },
        {
            'name':'kolkata zoo',
            'location':'Kolkata',
        },
        {
            'name':'Tamil Nadu zoo',
            'location':'Tamil Nadu',
        },
        {
            'name':'Delhi zoo',
            'location':'Delhi',
        },
        {
            'name':'odissa zoo',
            'location':'odissa',
        },
        {
            'name':'maharastra zoo',
            'location':'maharastra',
        },
    ]
    return JsonResponse({'status':200,'data':zoos})  
    
def login(request):
        email_value=request.GET.get('email')
        password_value=request.GET.get('password')
        
        print(email_value)
        print(password_value)
        if email_value=="admin@gmail.com" and password_value=="admin@123" :
            return JsonResponse({'message':'Login successful'})
        else:
            return JsonResponse({'message':'Invalid Login'})
bookings=[]        
def book_ticket(request):
    name = request.GET.get('name')
    persons = request.GET.get('number_of_persons')
    email = request.GET.get('email')

    if not name or not persons or not email:
        return JsonResponse({'error': 'Missing one or more fields'})
    booking = {
        'name': name,
        'number_of_persons': persons,
        'email': email
    }
    bookings.append(booking)

    return JsonResponse({
        'status': 200,
        'message': 'Ticket booked successfully and added to array',
        'total_bookings': len(bookings),
        'bookings': bookings
    })        
    
    
