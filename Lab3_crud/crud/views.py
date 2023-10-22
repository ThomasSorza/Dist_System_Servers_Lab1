from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Users
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# Query para buscar un usuario por documento y contraseña
def get_user(document, password):
    try:
        user = None
        if Users.objects.get(document=int(document), password=password) is not None:
            user = Users.objects.get(document=int(document), password=password)
        return user
    except Users.DoesNotExist:
        return None

@api_view(['POST'])
@csrf_exempt
def login(request):
    # Obtener el documento y la contraseña de los datos de la solicitud
    document = request.data.get('document')
    password = request.data.get('password')

    # Utilizar la función get_user para buscar al usuario
    user = get_user(document, password)

    if user is not None:

        # Generar un token de autorización (JSON Web Token)
        refresh = RefreshToken.for_user(user)

        # Obtener el token de acceso (JWT)
        access_token = str(refresh.access_token)

        # Construir una respuesta con el token JWT
        response_data = {
            'access_token': access_token,
        }
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        # Si no se encuentra un usuario, responder con un mensaje de error y código 401 (No autorizado)
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_401_UNAUTHORIZED)

'''
@api_view(['POST'])
def login(request):
    document = request.data.get('document')
    password = request.data.get('password')

    # Autenticar al usuario
    user = authenticate(request, document=document, password=password)

    if user is not None:
        # Si la autenticación es exitosa, obtenemos o creamos un token
        token, created = Token.objects.get_or_create(user=user)

        # Puedes personalizar la respuesta según tus necesidades
        response_data = {
            'message': 'Autenticación exitosa',
            'token': token.key,
            'user_id': user.id,  # O cualquier otro dato del usuario que desees incluir
        }

        return Response(response_data, status=status.HTTP_200_OK)
    else:
        # Si la autenticación falla, respondemos con un error
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_400_BAD_REQUEST)

'''    
@api_view(['GET'])
def test_token(request):
    return Response({})

'''
#For future sign_up
@api_view(['POST'])
def sign_up(request):
    return Response({})'''