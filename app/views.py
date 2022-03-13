from rest_framework.views import APIView
from rest_framework import permissions, viewsets
from tokenize import Token
from rest_framework.response import Response
from app.serializers import MemberSerializer, ArticleSerializer
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from app.models import Article
from django_filters.rest_framework import DjangoFilterBackend

class GetMemberView(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = MemberSerializer()

    def get(self, request, format=None):
        user = self.request.user
        serializer = MemberSerializer(user)
        return Response(serializer.data)


class ArticleViewSet(viewsets.ModelViewSet):
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly, TokenHasReadWriteScope]
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']
    ordering_fields = ['created_at']