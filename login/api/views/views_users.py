from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from login.api.serializers.serializers_users import UserSerializer
from login.models import User
from django.contrib.auth.models import Group
import uuid

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
        """
            Developer: Johan Esteban Sabogal <canoas430@gmail.com>.
            Todos los Derechos reservador a: Johan Esteban Sabogal Canoas, Leyder Ramirez, Alan Tobar. 
            Funcion "CREATE" del modelo (User), Crea al usuario y le asigna el grupo "Usuario" por defecto.

            JSON:

                {
                    "password": "1234",
                    "username": "johan12@gmail.com",
                    "name": "johan",
                    "last_name": "sabogal",
                    "document": 10058375422,
                    "number_phone": 3146446590
                }
        """
        data = {}
        data["status"] = status.HTTP_400_BAD_REQUEST
        try:
            user_serializer = self.serializer_class(data = request.data)
            if user_serializer.is_valid():
                user_serializer.token = uuid.uuid4()
                user_serializer.save()
                user = User.objects.get(document = request.data["document"])
                user.groups.add(Group.objects.get(name='Usuario'))
                data["msg"] = "Se ha registrado exitosamente el usuario!" ; data["status"] = status.HTTP_201_CREATED; data["type"] = "success";
            data["msg"] = user_serializer.errors
            
        except Exception as e:
            if data.get("msg") is None: data["msg"] = str(e)
            data["type"] = "error"
        return Response(data, status = data["status"])
    

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

