import json

from os           import EX_TEMPFAIL
from django.views import View
from django.http  import JsonResponse

from .models import Owner, Dog

class OwnerAdd(View):
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(name=data["name"], email=data["email"], age=data["age"])
        return JsonResponse({"result": "CREATE SUCCESS"}, status=201)

class DogAdd(View):
    def post(self, request):
        data = json.loads(request.body)
        ownerName = Owner.objects.get(name=data["ownerName"])
        Dog.objects.create(name=data["name"], age=data["age"], owner=ownerName)
        return JsonResponse({"result": "CREATE SUCCESS"}, status=201)




class OwnerList(View):
    def get(self, request):
        owners = Owner.objects.all()
        ownerList = []
        for owner in owners:
            petList = []
            ownerList.append({'name': owner.name})
            ownerList.append({'email': owner.email})
            ownerList.append({'age': owner.age})
            dogs = Dog.objects.filter(owner__name=owner.name)
            for dog in dogs:
                if owner.name == dog.owner.name:
                    petList.append({'name': dog.name})
                    petList.append({'age': dog.age})
            ownerList.append({'petLIst': petList})
        

        return JsonResponse({'OwnerList': ownerList}, status=200)

class DogList(View):
    def get(self, request):
        dogs = Dog.objects.all()
        dogList = []
        for dog in dogs:
            dogList.append({'name': dog.name})
            dogList.append({'age': dog.age})
            dogList.append({'owner': dog.owner.name})
        return JsonResponse({'DogList': dogList}, status=200)



# 각 기능을 서로 다른 클래스로 구현해주세요.

# 1. 주인 리스트
#     - 이름, 이메일, 나이 포함
# 2. 강아지 리스트
#     - 이름, 나이, 주인 이름 포함
# 3. 주인 리스트 **(1번 코드에 추가)**
#     - 이름, 나이 포함, **키우는 강아지 리스트 (이름, 나이 포함)**



# name
# email
# ownerAge
# dogName
# dogAge
# ownerName

# http POST localhost:8000/owners/owner name="" email="" age= 
# http POST localhost:8000/owners/dog name="" age= ownerName=""