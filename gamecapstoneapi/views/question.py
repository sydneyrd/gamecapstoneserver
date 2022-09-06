import base64
from datetime import datetime
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from gamecapstoneapi.models import Question
from gamecapstoneapi.models import SlotUser
from django.db.models import Q




class QuestionView(ViewSet):
    """ Question Views """

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type"""
        try:
            question = Question.objects.get(pk=pk)
            serializer = QuestionSerializer(question)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Question.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    # def list(self, request):
    #     """Handle GET requests to get all game types
    #     Returns:
    #         Response -- JSON serialized list of game types
    #     """
    #     posts = Post.objects.all()
    #     subscriptions = self.request.query_params.get('subscriptions', None)
    #     if subscriptions is not None:
    #         currentuser = RareUser.objects.get(user=request.auth.user)
    #         subs = currentuser.follower.all()
    #         subbed_posts = []
    #         for sub in subs:
    #             for post in posts:
    #                 if post.user == sub.author:
    #                     subbed_posts.append(post)

    #         posts = set(subbed_posts)
    #         # only posts whose authorId matches the authors subscribed to

    #     search_text = self.request.query_params.get('title', None)
    #     if search_text is not None:
    #         posts = Post.objects.filter(
    #             Q(title__contains=search_text) |
    #             Q(content__contains=search_text))
    #     user = request.query_params.get('user', None)
    #     if user is not None:
    #         posts = Post.objects.filter(user=user)
    #     category = request.query_params.get('category', None)
    #     if category is not None:
    #         posts = Post.objects.filter(category=category)
    #     tag = request.query_params.get('tag_id', None)
    #     if tag is not None:
    #         posts = Post.objects.filter(tags=tag)
    #     serializer = PostSerializer(posts, many=True)
    #     return Response(serializer.data)

    # def create(self, request):
    #     """Handle POST operations"""
    #     user = RareUser.objects.get(user=request.auth.user)
    #     cat = Category.objects.get(pk=request.data["category_id"])

    #     format, imgstr = request.data["image_url"].split(';base64,')
    #     ext = format.split('/')[-1]
    #     data = ContentFile(base64.b64decode(
    #         imgstr), name=f'{request.data["title"]}-{uuid.uuid4()}.{ext}')

    #     if user.user.is_staff == True:
    #         post = Post.objects.create(
    #             title=request.data["title"],
    #             user=user,
    #             category=cat,
    #             publication_date=datetime.date.today(),
    #             image_url=data,
    #             content=request.data["content"],
    #             approved=True
    #         )

    #     else:
    #         post = Post.objects.create(
    #             title=request.data["title"],
    #             user=user,
    #             category=cat,
    #             publication_date=datetime.date.today(),
    #             image_url=data,
    #             content=request.data["content"],
    #             approved=False
    #         )
    #     post.tags.add(*request.data['tags'])
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def update(self, request, pk):
    #     """handle put"""
    #     post = Post.objects.get(pk=pk)
    #     cat = Category.objects.get(pk=request.data["category_id"])
    #     post.title = request.data["title"]
    #     post.publication_date = request.data["publication_date"]
    #     post.image_url = request.data["image_url"]
    #     post.category = cat
    #     post.content = request.data["content"]
    #     post.approved = request.data["approved"]
    #     post.save()
    #     post.tags.clear()
    #     post.tags.add(*request.data['tags'])
    #     return Response(None, status=status.HTTP_204_NO_CONTENT)

    # def destroy(self, request, pk):
    #     post = Post.objects.get(pk=pk)
    #     post.delete()
    #     return Response(None, status=status.HTTP_204_NO_CONTENT)

    # @action(methods=['post'], detail=True)
    # def add(self, request, pk):

    #     post = Post.objects.get(pk=pk)
    #     PostReaction.objects.create(post=post, reaction_id=request.data['reaction_id'])

    #     return Response({'message': 'Reaction Added'}, status=status.HTTP_201_CREATED)


class QuestionSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Question
        fields = ('id', 'label', 'difficulty', 'solution')
        depth = 2