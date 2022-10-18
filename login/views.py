from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from login.serializers import UserSerializer
from login.models import User


class userViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer    
    queryset = None
    model = User
    
    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.all()
        return self.queryset

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)
#lista
    def list(self, request):
        queryset = self.model.objects.all()
        serializer = self.serializer_class(queryset, many=True) 
        return Response(serializer.data)

    def create(self, request):
        user_serializer = self.serializer_class(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"mensaje": "Se ha registrado exitosamente el usuario!"},status= status.HTTP_201_CREATED)
        return Response({"error":user_serializer.errors},status= status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None): 
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)   
        
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user = self.get_object(pk)

        user_serializer = self.serializer_class(user,data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"message":"Usuario actualizado correctamente!"}, status= status.HTTP_200_OK)
        return Response({"error":"hay errores en la actualizacion ", "error": user_serializer.errors}, status= status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk = None):
        user_destroy = self.model.objects.filter(id=pk).update(is_active= False)
        if user_destroy == 1:
            return Response({"message":"Usuario eliminado correctamente"},status=status.HTTP_200_OK)
        return Response({"error":"No existe un usuario con estos datos"},status=status.HTTP_404_NOT_FOUND)
# Create your views here.
