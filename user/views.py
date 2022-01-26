from django.shortcuts import render,redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model #사용자가 데이터베이스 안에 있는지 없는지 확인하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up_view(request):
    if request.method == 'GET': #장고서버로 url요청을 한다.
         user = request.user.is_authenticated
         if user:
             return redirect('/')
         else:
             return render(request, 'user/signup.html')#sign.html에 화면을 띄어준다.
    elif request.method =='POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        password2 = request.POST.get('password2','')
        bio = request.POST.get('bio','')

        if password != password2:
            #패스워드가 같지 않음
            return render(request, 'user/signup.html',{'error':'패스워드를 확인해주세요'}) #일치하지 않는다면 저장되지 않고 회원가입페이지로 다시 간다.
        else:
            if username == '' or password == '':
                return render(request, 'user/signup.html', {'error': '이름과 패스워드를 입력해주세요'})
            exist_user = get_user_model().objects.filter(username=username)#username을 UserModel안에 있는지 찾아낸다.
            if exist_user:
                #이름 아이디가 중복이 될 경우
                return render(request, 'user/signup.html',{'error': '사용자가 이미 존재합니다.'})
            else:
                # new_user = UserModel()
                # new_user.username = username
                # new_user.password = password
                # new_user.bio = bio
                # new_user.save()
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in') #회원가입이 성공시 로그인 페이지로 이동한다.

def sign_in_view(request):
    if request.method =='POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        me = auth.authenticate(request, username=username, password=password)
        #입력한 username과 암호를 저장된 username,암호가 일치하는지 한번에 비교하는 기능을 하고있다.
        if me is not None:
            auth.login(request, me)
            # request.session['user'] = me.username #동일하면 세션안에 me.username을 추가
            return redirect('/')
        else:
            return render(request,'user/signin.html',{'error':'유저 이름 혹은 패스워드를 확인해주세여'})

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request,'user/signin.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')




@login_required
def user_view(request):
    if request.method == 'GET':
        # 사용자를 불러오기, exclude와 request.user.username 를 사용해서 '로그인 한 사용자'를 제외하기
        # 친구 리스트를 보는데 굳이 내가 나를 보고 팔로우 할 이유가 없어서 제외한다.
        user_list = UserModel.objects.all().exclude(username=request.user.username)
        return render(request, 'user/user_list.html', {'user_list': user_list})



@login_required
def user_follow(request, id):
    me = request.user
    click_user = UserModel.objects.get(id=id) #팔로워할 사용자, 클릭하는 사용자
    #팔로워할 사람들중 사용자가 있으면 클릭하면 취소가 되고 없으면 팔로워패목록이 추가
    if me in click_user.followee.all():
        click_user.followee.remove(request.user)
    else:
        click_user.followee.add(request.user)
    return redirect('/user')
