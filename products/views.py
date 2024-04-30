from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class Products(APIView):

    def get(self, request, what=None):
        pass

    def post(self, request):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

    def put(self, request, what):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

    def delete(self, request, what):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

class Comments(APIView):

    def get(self, request, what):
        pass

    def post(self, request, what):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

    def put(self, request, what, comment_id):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

    def delete(self, request, what, comment_id):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

class Likes(APIView):

    def post(self, request):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)