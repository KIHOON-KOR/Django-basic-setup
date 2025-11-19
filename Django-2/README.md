## *Chapter 02. Views와 ORM*

> `views.py` 와 `Models.py` 는 Django의 App 구조 안에 들어있습니다.
이번 시간에는 App을 생성하여 views.py와 Models.py를 사용해보겠습니다!
> 

### 앱 생성 및 구조 설명

1. 터미널에 `python3 manage.py startapp bookmark` 명령어를 입력하여 bookmark app을 만듭니다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/33df368c-3e65-46e6-ae43-2f476a479600/Untitled.png)

- `models.py`
    - DB와 관련된 테이블과 컬럼을 관리한다.
- `views.py`
    - 메인 알고리즘을 담당한다
- `tests.py`
    - 테스트 코드를 작성한다.
- `apps.py`
    - Django App 관련 설정 관련 내용.
- `admin.py`
    - 어드민 관련된 설정 관리.
- `__init__.py`
    - 파이썬 패키지를 관리하는 파일.
- `migrations`
    - Model이 수정된 기록이 쌓임.

1. `config/settings.py` INSTALLED_APPS에 생성한 앱을 등록합니다.

```python
## settings.py

# Django에서 기본적으로 제공되는 APP과 본인이 만든 APP을 구분하여 관리하기 위해
# INSTALLED_APPS를 DJANGO_APP과 OWN_APPS로 분리합니다.

DJANGO_APPS = [ 
		'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	]

OWN_APPS = [
	'bookmark',
]

INSTALLED_APPS = DJANGO_APPS + OWN_APPS
```

<aside>
✅

App 구조를 구성하고 만들 때는 **모듈화**를 고려합니다.
1개의 App 생성 기준은 **재사용**이 가능한 단위입니다.
하나의 프로젝트에서 만든 App 기능이 다른 프로젝트에서도 사용될 수 있을 때,
재사용이 가능하다고 표현할 수 있습니다.

</aside>

### Views를 활용하여 페이지 만들기

- http://127.0.0.1:8000/bookmark/
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/c64aa2ba-eef0-4818-94ce-8303b2f7b3cc/Untitled.png)
    
- http://127.0.0.1:8000/bookmark/<int:number>/
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/94de5d89-0b35-4a5c-8ca9-f6bc210f2437/Untitled.png)
    

```python
## views.py

from django.http import HttpResponse
from django.shortcuts import render

def bookmark_list(request):
    return render(request,'bookmark_list.html')

def bookmark_detail(request, number):
    return render(request, 'bookmark_detail.html', {'number': number} )
```

```python
## bookmark_list.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>북마크 리스트 페이지입니다.</h1>
</body>
</html>
```

```python
## bookmark_detail.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>북마크 {{ number }} 번 디테일 페이지입니다.</h1>
</body>
</html>
```

### Model과 Field, Migrations

<aside>
✅ **Model**은 데이터베이스의 **테이블**을 의미합니다.
**Field**는 데이터베이스의 **컬럼**을 의미합니다.

북마크의 필요요소 : 이름, URL 주소

</aside>

[Model field reference | Django documentation](https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-types)

Filed Type이 정리되어있는 공식 문서입니다.

[Downloads - DB Browser for SQLite](https://sqlitebrowser.org/dl/)

해당 공식 문서를 따라 다운로드를 진행해주세요! brew 명령어로 설치해도 무방합니다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/2226f685-0342-4fc3-bf8a-1145898bb94c/Untitled.png)

먼저 기존에 계속 뜨던 migrations 문제를 해결하고 갑시다.

DB Browser for SQLite에서 bookmark 프로젝트의 `db.sqlite3` 파일을 엽니다.

지금은 migrate가 전혀 되지 않은 상황이라 DB Browser for SQLite에서 전부 0으로 나타납니다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/15940d2b-be08-48df-926a-6976bec70609/Untitled.png)

`python manage.py migrate` ****명령어로 마이그레이트를 진행합니다.

![Django에서 기본적으로 migrate 되어야 하는 테이블이 생성되었습니다.](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/ad69a584-4744-41f3-b1d4-9732c7d3e38b/Untitled.png)

Django에서 기본적으로 migrate 되어야 하는 테이블이 생성되었습니다.

<aside>
➡️ makemigrations

- python [manage.py](http://manage.py) makemigrations
- `migrations.py` 파일을 만듭니다.
- migrate 명령어를 사용하기 전까지 데이터베이스에 영향을 주지 않습니다.
- Django 애플리케이션의 모델에 대한 변경 사항을 감지하고, 이를 데이터베이스 스키마로 변환할 수 있는 마이그레이션 파일을 생성합니다.
</aside>

<aside>
➡️ migrate

- python [manage.py](http://manage.py) migrate
- 마이그레이션을 실행하여 데이터베이스에 변경 사항을 적용하는 명령어입니다.
- Django의 ORM(Object-Relational Mapping) 시스템을 통해 데이터베이스 스키마를 최신 상태로 유지합니다.
</aside>

1. bookmark/models.py에 Bookmark 모델을 정의합니다.
    
    ```python
    from django.db import models
    
    class Bookmark(models.Model):
        name = models.CharField('이름', max_length=100)
        url = models.URLField('URL')
        created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
        updated_at = models.DateTimeField(verbose_name='수정일시', auto_now=True)
    
        class Meta:
            verbose_name = '북마크'
            verbose_name_plural = '북마크 목록'
    ```
    
2. `python manage.py makemigrations` 명령어로 마이그레이션 파일을 생성합니다.
3. `python manage.py migrate` 명령어로 데이터베이스에 변경 사항을 적용하면 bookmark_bookmark(App이름_테이블이름) 테이블이 확인된 것을 볼 수 있습니다.
    
    ![bookmark_bookmark는 (App_Table)](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/e965dd99-9cb3-4f45-866b-a6be89d95b3c/Untitled.png)
    
    bookmark_bookmark는 (App_Table)
    

### Django Admin

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/bb25dc50-d0cd-4678-b6d6-457489b80086/Untitled.png)

> Django는 강력한 관리자(어드민) 페이지를 가진 프레임워크입니다. 
로컬서버를 실행하고 127.0.0.1:8000/admin/ 로 접속할 수 있습니다. 
Admin Page를 이용하기 위해서는 접근 권한을 가진 SuperUser가 필요합니다.
> 

1. `python manage.py createsuperuser` 명령어로 슈퍼유저를 생성합니다.

```python
Username : admin # 슈퍼유저의 이름
Email address: # 이메일, 입력하지 않아도 괜찮습니다.
Password: # 비밀번호
Password (again): # 비밀번호 재입력

# Django에서 기본적으로 제공하는 비밀번호 규칙에 의한 메세지입니다.
# 계속하고 싶다면 y를 입력합니다.
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y

# 슈퍼유저가 생성되었습니다.
Superuser created successfully.

```

1. 슈퍼유저 계정으로 로그인합니다.

![로그인된 admin page](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/5ab47db3-adaa-4c29-9ba5-8924579019e4/Untitled.png)

로그인된 admin page

1. Bookmark 앱을 어드민에 등록합니다.

```python
bookmark/admin.py

from django.contrib import admin
from bookmark.models import Bookmark

admin.site.register(Bookmark)
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/6fbe3af9-0133-4844-ac01-100ed8a66d58/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/7c039a67-6976-402a-aee1-f35cf222dd9a/Untitled.png)

<aside>
💡 settings.py에서 LANGUAGE_CODE를 ‘ko-KR’ 로 변경하면 언어 설정이 한글로 변경됩니다.

</aside>

1. 객체를 추가하면 **Bookmark object (n)** 같이 보이는데 `models.py` 에 함수를 추가하여 설정을 변경할 수 있습니다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/583a8625-9ca4-4da1-af68-7ccaf99241db/Untitled.png)

```python
## models.py

class Bookmark(models.Model):
    name = models.CharField('이름', max_length=100)
    url = models.URLField('URL')
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='수정일시', auto_now=True)
		
		# 추가
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '북마크'
        verbose_name_plural = '북마크 목록'
```

![코드 추가 후, 변경된 모습](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/9dc2cc12-9090-430d-947d-d496dcd77bfe/Untitled.png)

코드 추가 후, 변경된 모습

1. `admin.py` 에서 디스플레이 설정을 변경할 수 있습니다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/b554bdd8-258c-4134-a493-f0e886fbd1a2/Untitled.png)

```python
## admin.py

from django.contrib import admin
from bookmark.models import Bookmark

# (A)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'url']
    list_display_links = ['name','url']
    list_filter = ['name','url']

# 하단 코드 대신 @admin.register(Bookmark)를 (A) 위치에 입력해도 됩니다.
admin.site.register(Bookmark, BookmarkAdmin)
```

[The Django admin site | Django documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/)

### 북마크 목록 페이지 만들기

- 북마크 리스트 페이지
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/72fd1b82-f1be-415b-ab73-28f57e426994/Untitled.png)
    
    ```python
    ## views.py
    
    def bookmark_list(request):
        bookmarks = Bookmark.objects.all()  # SELECT * FROM bookmark
        context = {'bookmarks': bookmarks}
        return render(request,'bookmark_list.html',context)
    ```
    
    ```python
    ## bookmark_list.html
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <h1>북마크 리스트 페이지입니다.</h1>
        {%  for bookmark in bookmarks %}
        <p>
            <a href="/bookmark/{{ bookmark.id }}/">
                {{ bookmark.name }}
            </a>
        </p>
        {% endfor %}
    </body>
    </html>
    ```
    
- 북마크 상세 페이지
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/db6ec072-4b55-4f46-bf1c-3d814893d2a5/Untitled.png)
    
    ```python
    ## views.py
    
    def bookmark_detail(request, pk):
        # bookmark 데이터를 가져오지 못했을 경우 404 에러를 발생시킨다.
        try:
            bookmark = Bookmark.objects.get(pk=pk)
        except Bookmark.DoesNotExist:
            raise Http404
    
        context = {'bookmark':bookmark}
        return render(request, 'bookmark_detail.html', context)
    
    # 404 에러를 발생시키는 또 다른 코드 
    from django.shortcuts import get_object_or_404
    
    def bookmark_detail(request, pk):
    	  bookmark = get_object_or_404(Bookmark,pk=pk)
    	
        context = {'bookmark':bookmark}
        return render(request, 'bookmark_detail.html', context)
    
    ```
    
    ```python
    ## bookmark_detail.html
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <h1>{{ bookmark.name }} 페이지입니다.</h1>
        <a href="{{ bookmark.url }}" target="_blank">링크</a>
    </body>
    </html>
    ```
    
    ```python
    ## urls.py
    
    urlpatterns = [
        path('bookmark/<int:pk>/', views.bookmark_detail),
    ]
    ```
    

![404 페이지](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/860fa15b-0c54-44af-a610-3ece7b1cf6d3/Untitled.png)

404 페이지

### ORM

<aside>
💡 **objects**는 쿼리를 할 수 있게 해주는 모델 매니저입니다.

</aside>

`Table.objects.all()` : 테이블의 모든 데이터를 가져옵니다. (SELECT * FROM table 과 동일)

`Table.objects.get(pk=pk)` : pk가 동일한 데이터를 1개 가져옵니다. 2개 이상의 데이터를 가져오려고 하면 오류가 발생합니다. (SELECT * FROM table WHERE id=id LIMIT 1 과 동일)

`Table.objects.filter(pk=pk)` : 개수에 상관없이 리스트 형태로 데이터를 가져옵니다. (SELECT * FROM bookmark WHERE id=id와 동일) 

[QuerySet API reference | Django documentation](https://docs.djangoproject.com/en/5.0/ref/models/querysets/)

```bash
# 보기 편하도록 ipython 패키지 설치
poetry add ipython

# ORM 사용을 위해 대화형 Python 셸을 실행
python manage.py shell

# ORM 작성 후 python shell에서 나올 때
exit
```

```bash
# 
poetry add django-extensions

## Pycharm
# config/settings.py

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

OWN_APPS = [
    'bookmark',
]

# 추가
THIRD_PARTY_APPS = [
    'django_extensions',
]

INSTALLED_APPS = DJANGO_APPS + OWN_APPS + THIRD_PARTY_APPS # 변경
```

```bash
# settings 설정 후 로컬 터미널에 입력
python manage.py shell_plus
```

![ Shell을 더 편리하게 이용할 수 있습니다.](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/bcdeffc1-2148-4fbe-b858-773507bd2335/Untitled.png)

 Shell을 더 편리하게 이용할 수 있습니다.

```bash
## shell_plus

### 객체 조회

# bookmark App의 모델인 Boormark를 import
from bookmark.models import Bookmark

# Bookmark 테이블의 모든 객체를 가져오기
Bookmark.objects.all()

# Bookmark 테이블에서 id가 2인 객체만 가져오기
# 조회된 객체가 2개 이상일 경우 오류 발생
Bookmark.objects.get(id=2)

# 모든 객체를 bookmark_list 변수에 할당
bookmark_list = Bookmark.objects.all()

# 첫번째 객체 가져오기
bookmark_list[0]
Bookmark.objects.first()

# 마지막 객체 가져오기
Bookmark.objects.last()

# 객체의 아이디
bookmark_list[0].id

# id가 2이상인 객체 불러오기

# gte: greater than or equal (이상)
# gt: greater than (초과)
# lt: less than (미만)
# lte: less than or equal to (이하)
Bookmark.objects.filter(id__gte=2)

# name이 네이버인 객체 가져오기
Bookmark.objects.filter(name='네이버')

## like 검색
# DB에 부담을 많이 주기 때문에 너무 짧은 검색어 사용은 지양

# 검색어가 포함된 객체 찾기
Bookmark.objects.filter(name__icontains='네')

# 검색어로 시작하는 객체 찾기
Bookmark.objects.filter(name__startswith='다')

# 검색어로 끝나는 객체 찾기
Bookmark.objects.filter(name__endswith='글')

# 지정된 리스트 내의 값들 중 하나와 일치하는 객체 찾기
Bookmark.objects.filter(name__in=['구글','네이버'])

# , 로 and 조건 검색 가능
Bookmark.objects.filter(name='네이버', url__startswith="https://naver")

```

```bash
### 객체 추가

# 기본
Bookmark.objects.create(name='야후', url='https://yahoo.com')

# 새로운 Bookmark 객체를 생성하고 데이터베이스에 저장
bookmark = Bookmark(name='야후2', url='https://yahoo.com')
bookmark.save()

## id값을 변경하여 새로운 데이터 만들기

# _를 쓰기 위해 모든 객체를 조회합니다.
# _는 마지막 Output값을 가져옵니다.
Bookmark.objects.all()

# b에 첫번째 데이터를 할당합니다.
b = _.first()   

# b의 id를 None으로 변경합니다.
# 첫번째 데이터에는 영향이 없습니다.
b.id = None

# id값이 없는 b 객체를 저장합니다.
# DB에서는 b를 새로운 데이터로 인식합니다.
b.save()

# b의 id가 새롭게 생겼습니다.
b.id
# b 객체의 name을 변경하면 차이를 알기 쉽습니다.
b.name = '네이버2'

# 다시 모든 객체를 불러옵니다
# b가 Bookmark에 추가되었습니다.
Bookmark.objects.all()
```

```bash
## 객체 업데이트

# url에 'naver.com'이 포함된 객체들의 name을 '네이버'로 업데이트합니다.
# Output에는 변경된 객체의 수가 출력됩니다.
Bookmark.objects.filter(url__icontains='naver.com').update(name='네이버')
```

```bash
## 객체 삭제

# b 객체를 삭제합니다.
# 메모리에서는 사라지지 않지만, b.id 값은 존재하지 않습니다.
# Django는 id값 유무에 따라 DB 저장 유무를 판단합니다.
b.delete()

# 여러개를 한 번에 삭제
Bookmark.objects.filter(name__icontains='야후').delete()
```

---

## 🔥 Mini Project. 북마크 목록 페이지에 ORM 활용하기

> **목표**
✅ 북마크 100개 만들기
✅ 북마크 목록에서 북마크의 id가 50이상인 것들만 추출해서 보여주기
> 

북마크 100개 만들기

1. 터미널에 `python manage.py shell_plus` 명령어를 입력하여 Python Django Shell로 접속합니다.
ls 명령어를 사용해 현재 경로에 manage.py가 있는지 확인해보는 것을 추천합니다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/9b6ce694-27c8-47de-83bc-f4d6b6fe78b1/Untitled.png)

1. for문을 사용하여 북마크 데이터 100개를 만듭니다. `Shift + Enter` 로 줄바꿈을 할 수 있습니다. 

```bash
for i in range(10):
   ...:      Bookmark.objects.create(name=f'테스트네이버{i}', url=f'https://naver.com')
  
# 데이터 개수 확인
Bookmark.objects.count()

## 리스트 컴프리헨션으로 데이터 만들기
## 대용량 데이터를 생성하거나 업데이트 할 때, 
## 요청횟수가 적어 DB에 부담이 적은 **bulk_create** 방식을 사용하는 것을 추천 
bookmark_list = [Bookmark(name=f'테스트 구글 {i}', url=f'https://google.com') for i in range(100)]
Bookmark.objects.bulk_create(bookmark_list)
```

1. id가 50이상인 데이터들만 추출합니다.

```python
## views.py

def bookmark_list(request):
    bookmarks = Bookmark.objects.filter(id__gte=50) # 수정
    # SELECT * FROM bookmark
		
    context = {
        'bookmarks': bookmarks
    }
    return render(request, 'bookmark_list.html', context)
```