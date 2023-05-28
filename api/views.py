from django.shortcuts import render
from rest_framework.decorators import api_view
from .forms import UserRegistrationForm, LoginForm, RequestFriendForm, AcceptForm, UserFriendsForm, DiffForm, PolyForm, LalgForm
from .models import Friend_Request, DiffExpression, Polynomial, LinearAlgebra
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .diff import diff
from .poly import eval_polys, Poly, Addition, Subtraction
from .lalg import evaluate, Vec, Vector, Matrix, M, Number
from .serializers import DiffSerializer, LalgSerializer, PolySerializer
User = get_user_model()

@api_view(['POST']) 
def register(request):
    form = UserRegistrationForm(request.POST)   
    if form.is_valid():
        new_user = form.save(commit=False)
        cd = form.cleaned_data    
        new_user.set_password(cd['password'])

        new_user.save()

        return Response({'account': 'created'}) 

    return Response({'form': 'invalid'})

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return Response({'login': 'Succesful'})
                else:
                    return Response({'login': 'Disabled'})
            else:
                return Response({'Invalid': 'login'})
    else:
        form = LoginForm()

    return Response({'test': 'hello'})

@api_view(['POST'])
@login_required(login_url='/api/login/')
@csrf_exempt
def request_friend(request):
    form = RequestFriendForm(request.POST)
    if form.is_valid():
        #new_user = form.save(commit=False)
        cd = form.cleaned_data  
        from_user = request.user
        to_user = User.objects.get(id=cd['id'])
        friend_request, created = Friend_Request.objects.get_or_create(from_user=from_user, to_user=to_user)

        if created:
            return Response({'request': 'sent'})
        else:
            return Response({'request': 'was sent already'})


@api_view(['POST'])
@login_required(login_url='/api/login/')
@csrf_exempt
def accept_friend_request(request):
    form = AcceptForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        friend_request = Friend_Request.objects.get(id=cd['id'])
        if friend_request.to_user == request.user:
            friend_request.to_user.friends.add(friend_request.from_user)
            friend_request.from_user.friends.add(friend_request.to_user)
            friend_request.delete()

            return Response({"accept": "request"})
        else:
            return Response({"request":"not accepted"})

@api_view(['POST'])
def list_friends_of_user(request):
    form = UserFriendsForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        user = User.objects.get(id=cd['id'])
        user_friends = user.friends.all()
        return serializers.serialize('json', user_friends)

@api_view(['POST'])
@login_required(login_url='/api/login/')
@csrf_exempt
def compute_diff_expression(request):
    form = DiffForm(request.POST)
    if form.is_valid():
        new_expr = form.save(commit=False)
        data_expr = form.cleaned_data
        data_expr = data_expr['exp']
        eval_data_expr = tuple(data_expr)
        eval_data = diff(eval_data_expr)
        expr_model = DiffExpression(exp=eval_data, user_name=request.user)
        expr_model.save()
        serializer = DiffSerializer(expr_model)

        return Response(serializer.data)

@api_view(['POST'])
@login_required(login_url='/api/login/')
@csrf_exempt
def compute_lalg_expression(request):
    form = LalgForm(request.POST)
    if form.is_valid():
        new_expr = form.save(commit=False)
        data_expr = form.cleaned_data
        data_expr = data_expr['exp']
        eval_data_expr = eval(data_expr)
        eval_data = evaluate(eval_data_expr)
        expr_model = LinearAlgebra(exp=eval_data, user_name=request.user)
        expr_model.save()
        serializer = LalgSerializer(expr_model)

        return Response(serializer.data)


@api_view(['POST'])
def compute_poly_expression(request):
    form = PolyForm(request.POST)
    if form.is_valid():
        new_expr = form.save(commit=False)
        data_expr = form.cleaned_data
        data_expr = data_expr['exp']
        eval_data_expr = eval(data_expr)
        eval_data = eval_polys(eval_data_expr)
        expr_model = Polynomial(exp=eval_data, user_name=request.user)
        expr_model.save()
        serializer = PolySerializer(expr_model)

        return Response(serializer.data)