from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class Accounts(APIView):

    def get(self, request, who):
        pass

    def post(self, request):
        print("asdasd")
        pass

    def put(self, request, who):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)
        pass

    def delete(self, request, who):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)
        pass

class Follow(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        pass