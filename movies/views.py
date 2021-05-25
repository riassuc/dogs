# import json

# from django.views import View
# from django.http  import JsonResponse

# from .models import Movie, Actor

# class ActorList(View):
#     def get(self, request):
#         data = json.loads(request.body)
#         actors = Actor.objects.all()
#         actorList = []
#         for actor in actors:
#             tempDict = {}
#             tempDict{'name'} = actor.first_name
#             actor.first_name
#             actor.last_name
#             movies = actor.movie.all()
#             movie = movies.title







# # 2. 등록된 배우 목록을 리턴해주는 GET 메소드를 구현해주세요.
# #     - 배우의 이름, 성, 그리고 출연한 영화 제목 목록
# # 3. 등록된 영화 목록을 리턴해주는 GET 메소드를 구현해주세요.
# #     - 영화의 제목, 상영시간, 출연한 배우 목록 (이름만)