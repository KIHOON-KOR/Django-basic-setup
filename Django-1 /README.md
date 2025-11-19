## *Chapter 01. Django 환경 설정과 Template*

## 강의 환경 소개

1. **MacOS**

백엔드 서버의 경우 주로 리눅스로 되어있다. MacOS가 리눅스와 유사한 환경이기 때문에 MacOS 환경을 추천.

1. **Python 가상환경** - pyenv virtualenv (설치 방법 안내 : https://github.com/pyenv/pyenv-virtualenv)

폴더 별로 여러 개의 환경을 관리할 수 있기 때문에 폴더에 shell로 접속 시, 자동으로 Python 가상환경이 잡혀 편하게 사용할 수 있는 것이 강점.

1. **Poetry** (https://python-poetry.org/) 

Package Manager. 의존성을 가진 각종 패키지들의 버전을 맞춰주는 작업을 도와주는 개발을 위한 강력한 도구로 설치하는 패키지들이 많아질수록 진가를 발휘.

1. **Pycharm Professional** (https://www.jetbrains.com/ko-kr/pycharm/download/?section=mac)

IDE. Visual Studio Code(VSC)보다 무겁지만 장고 환경에 맞춰 설정이 가능하기 때문에 편하게 사용가능. 

## 강의 소개 (강의 목표)

총 3개의 사이트, 1개의 REST API 서버를 만들어보겠습니다 :)

1. 북마크 사이트 (기초)
2. 블로그 사이트 (기본)
3. 인스타그램 클론 사이트 (확장)
4. 블로그 REST API 
5. 배포 - EC2, RDS, S3

### *소스코드*

[GitHub - Isaccchoi/OZ_Django: OZ코딩스쿨 Django 소스코드](https://github.com/Isaccchoi/OZ_Django)

오류는 대부분 **오타**의 문제입니다!

오류가 발생했을 시, 무조건 깃허브에서 가져오지마시고 최대한 에러메세지를 바탕으로 해결을 해보시고 챕터별 커밋을 통해 코드를 확인하고 틀린 부분을 수정하면서 강의를 따라오시길 바랍니다😎

## pyenv

- Homebrew가 아직 설치되지 않았다면?
    
    ### 'Homebrew'란?
    
    MacOS, Linux에서 프로그램을 설치/삭제할 수 있도록 해주는 패키지 관리 어플리케이션입니다.
    
    [Homebrew 공식 홈페이지](https://brew.sh/)에서 설치 명령어를 직접 복사하여 터미널에 입력하면 Homebrew를 설치하고 이용할 수 있습니다
    
    ![](https://velog.velcdn.com/images/slight-snow/post/c3564d7c-f1e3-43ae-b701-49b9adcf238a/image.png)
    
    - 설치 명령어
    
    ```
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
    
    설치 명령어를 입력하고 조금만 기다리면,
    
    **`==> Installation successful!`** 이라는 문구와 함께 설치가 완료됩니다.
    
    - 아래의 명령어를 추가해주셔야 홈브류가 정상적으로 작동합니다.
        
        ```python
        # zshrc에 homebrew path 추가하기
        echo 'export PATH=/opt/homebrew/bin:$PATH' >> ~/.zshrc
        
        # zshrc 반영
        source ~/.zshrc
        ```
        
    
    - brew 버전 확인
        
        ```python
        brew --version
        ```
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/36348ab9-834d-4731-a5e8-283c2ae09b8b/Untitled.png)
        
        위의 사진처럼 버전 숫자가 뜨면 홈브류설치 완료입니다 😊
        

### pyenv 설치방법

1. 터미널에 **`brew install pyenv`** 명령어로 **pyenv**를 설치합니다.
2. 터미널에 **`brew install pyenv-virtualenv`** 명령어로 **pyenv-virtualenv**를 설치합니다.
3. **`which $SHELL`** 명령어로 본인이 사용하는 **Shell**을 확인합니다. (bash 또는 zsh)
4. **`echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc`** 명령어로 Pyenv에서 **가상환경의 자동화**를 설정합니다.
    1. bash을 사용하는 경우 **`echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc`**
5. **`source ~/.zshrc`** 명령어로 Shell을 다시 실행합니다.(터미널 껐다 켜도 됩니다!)
    1. bash를 사용할 경우 **`source ~/.bashrc`** 
6. **`pyenv --version`** 명령어로 pyenv가 설치됐는지 확인합니다. *(pyenv 2.4.0 등 버전 정보가 나오면 설치완료!)*
7. **`pyenv`** 명령어로 pyenv virtualenv가 설치됐는지 확인합니다. 
*(pyenv-virtualenv 1.2.4 (python3 -m venv) 등 버전 정보가 나오면 설치 완료!)*

💡 **pyenv virtualenv**는 폴더 기준으로 관리되기 때문에 최상위 경로에서 작업 X ! 여기부터 새로 만든 폴더에서 테스트 해주세요. 

---

1. **`pyenv install --list` 또는 `pyenv install 원하는 버전`** 명령어로 설치 가능한 버전 확인
2. **`pyenv virtualenv 직전설치버전 pyenv-test`** 명령어로 Python 3.12.2 버전을 설치하고,
pyenv-test라는 가상환경을 만듭니다. 
직전에 설치한 것과 동일한 버전만 설치가 가능하며, 다른 버전을 설치하려면 직전 명령어를 통해 타 버전을 설치한 후 진행해야합니다. `pyenv-test` 라는 이름은 자유롭게 변경할 수 있으나 강의와 동일하게 진행하는 것을 권장합니다. 
3. **`pyenv local pyenv-test`** 명령어로 가상환경을 활성화 합니다. 
터미널에 자신의 경로 앞에 (가상환경이름) 이 나타나야합니다. 
    
    ```bash
    (가상환경이름) a1@1ui-MacBookAir pyenv-test % 
    ```
    
4. **`ls -al`** 명령어를 입력하면 `.python-version` 파일이 생긴 것을 확인할 수 있습니다.
5. **`python --version`** 을 다시 입력해보면 의도적으로 설치한 **Python 3.12.2**을 확인할 수 있습니다. 
    1. zsh: command not found: python 에러 메세지가 뜬다면 **`python3 --version`** 명령어를 사용해보세요!
6. **`pip install django`** 명령어로 Django를 설치합니다
    1. zsh: command not found: pip 에러 메세지가 뜬다면 **`pip3 install django`** 명령어를 사용해보세요!
7. **`pip list`** 명령어로 Django가 설치되었는지 확인합니다. 
폴더 기준으로 관리되기 때문에 다른 폴더에는 Django가 설치되어있지 않습니다. 

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/d2f734cf-d31d-47a9-b8fa-d49b85cec93d/Untitled.png)

> **가상환경을 사용하는 이유 ?**
> 
> 
> 프로젝트마다 격리된 환경(즉, 가상 환경)을 생성함으로써 프로젝트별로 패키지를 관리하기 위해서입니다. 예를 들어 Python 3.11.2과 Django 5.0.7이 설치된 컴퓨터가 있습니다. 이 컴퓨터로 입사한 회사의 프로젝트 A를 진행하려고 합니다. 
> A 프로젝트는 Python 3.9.0과 Django 4.8.2 버전을 사용하여 진행되어 왔습니다. 
> 그렇다면 컴퓨터에 Python 3.9.0와 Django 4.8.2 를 설치하면 될까요? 
> 만약 앞서 설치한 버전과 다른 버전을 사용하는 프로젝트 B도 같은 기간동안 진행해야한다면 어떨까요? 
> 
> 이처럼 가상환경은 프로젝트 별로 상이한 개발 환경을 분리하여 관리할 수 있습니다.
> 

- python3, pip3 을 python, pip 로 사용하고 싶을 경우
    
    ```python
    vi ~/.zshrc
    ```
    
    `i`눌러서 `INSERT` 로 수정모드를 만든 후에 (터미널 하단에서 확인 가능)
    
    → 한글 일때는 insert 안먹습니다. 
    → 키보드가 영어로 되어있는지 확인 필수
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/0422f993-f040-422d-a67e-6b3541e90311/Untitled.png)
    
    ```python
    alias python="python3"
    alias pip="pip"
    ```
    
    입력 후
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/9380398c-66aa-4e23-aa42-a20a4daabd81/Untitled.png)
    
    ```python
    ESC → :wq → source ~/.zshrc
    ```
    
    위의 사진에서 `.zprofile` 인 이유는 .. 저장 하는 곳의 차이 입니다.
    
    `.zshrc` ||  `.zprofile` 둘 다 가능
    

## Pycharm

### Pycharm 설치방법

1. 하단 사이트 링크에 접속해 Pycharm을 설치해주세요.

[PyCharm 다운로드: 데이터 과학 및 웹 개발을 위해 JetBrains가 만든 Python IDE](https://www.jetbrains.com/ko-kr/pycharm/download/?section=mac)

**Professional** 버전으로 다운받아주세요 !

→ 인텔인지 m1인지 확인 후에 본인의 맥북에 맞는 버전으로 다운받기~

**Professional** 무료 체험 코드는 조교 에게 부탁하세요! (6개월 사용 가능)

---

## Pycharm 설정

1. 사용할 가상환경 만들기

```bash
# 사용할 폴더에서 작업
# pycharm_study라는 가상환경 만들기
pyenv virtualenv 3.12.1 pycharm_study

# 가상환경 실행
pyenv local pycharm_study
```

1. `command + ,` 로 설정 탭을 열고 가상환경을 설정한다.

```bash
# 인터프리터 설정 열기
project: myproject > Python Interpreter > Add Interpreter > Add Local Interpreter

# 가상환경 만들기
Virtualenv Environment 선택 > Environment 설정 중 Existing 선택 > 만든 가상환경 선택
```

1. 터미널을 열면 자동으로 가상환경이 잡힌 것을 확인할 수 있다.

💡경로가 제대로 잡히지 않는 경우

```bash
Users > 로그인하는 유저 > .pyenv > versions > pycharm_study > bin > python
```

1. Django 프로젝트 세팅 (Pycharm 터미널에서 작업)
    1. `pip install django` 로 Django를 설치합니다. 
    (Setting의 Python Interpreter에 Django가 설치된 것을 볼 수 있습니다.)
    2. `django-admin startproject mysite .` 로 Django를 실행합니다. 
    (mysite는 앞으로 만들게 될 프로젝트 명입니다.)
    `django-admin startproject config .` 도 가능
    3. Setting의 Languages & Frameworks > Django > Enable Django Support 체크합니다.
    4. Languages & Frameworks > Django > Django project root, Settings, Main script를 설정합니다.

## Django

### Django의 기능

- DB구조와 쿼리를 할 수 있는 ORM(Object relational Mapping) 기능
- 인증 허가(=로그인) 관련 기능 (Authentication & Authorization)
- 관리자 인터페이스 (Admin Interface)
- 국제화, 번역 기능 (Internationalization)
- URL을 이용한 페이지 처리 기능 (URL Routing)
- Template Engine

### MVT 구조

- Model : DB관련 기능 수행
- View : 실질적인 메인 알고리즘
- Template : 유저들에게 보여주는 화면단

### 장점

- Django 자체가 가진 기능이 많아서 개발 속도가 빠르다.
- 코드 재사용 및 모듈화가 유연하다.
- 기본적인 보안이 갖춰져있어 안정성 높은 웹 애플리케이션 구축이 가능하다.

### 단점

- 효과적으로 활용하기 위해 숙련 및 개념 탑재가 필요하다.
- Django적인 개발 문법이 필요하여 별도의 공부가 필요하다.
- 익혀야 하는 개념이 복잡하다.

### Django를 사용하는 이유

- Flask나 FastAPI는 여러 패키지를 설치하여 사용해야하지만, Django는 기본적으로 탑재되어있다.
- 개발 시간이 많이 소요되는 관리자 페이지를 Django에서 제공하기 때문에 개발 시간을 줄여준다.
- 모듈화를 통해 코드 재사용 효율성이 높기 때문에 개발 시간이 단축된다.
- 획일화된 구조로 코드의 가독성이 좋다.
- 다양한 패키지가 있어 사용할 수 있는 소스가 많다.
- 잘 구축된 커뮤니티에서 빠르게 질 좋은 응답을 받을 수 있다.

### 구조도

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/826b7570-aeec-40aa-870d-94a47a8c7c78/Untitled.png)

- Model.py
    - DB와 연결됨
- Views.py
    - 알고리즘 담당
- URLs.py
    - URL에 따라 설정된 뷰(View)로 연결되는 작업을 수행
- Template
    - 화면단(Html)을 담당
- Web Server(ngnix, apache 등)
    - Python과 브라우저 요청 사이에서 요청은 Python 코드로 바꿔줌
    - Django 개발서버에서는 Django가 대신 역할 수행

```bash
## 일반적인 순서

1. 브라우저에서 웹서버로 요청이 들어옴
2. urls에서 view로 연결
3. view에서 알고리즘에 따라서 필요한 데이터를 Model을 통해서 가져옴
4. 가져온 데이터를 Template를 이용해 화면단에 보여줌
```

## Django 프로젝트 설치 및 시작

```bash
 # oz라는 이름으로 가상환경 생성
 pyenv virtualenv 3.12.1 oz
 
 # 가상환경 실행
 pyenv local oz
 
 # poetry 설치
 brew install poetry
 
 # poetry 초기화
 # Package name은 oz_bookmark로 설정
 # Author에만 n을 입력하고 나머지는 전부 Enter를 눌러 진행합니다.
 poetry init
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/acefeecb-d2c3-413f-98c1-dcd60d6a7a9d/Untitled.png)

- Poetry란?
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/1902e49a-8b64-4aef-8489-31f46f273d18/Untitled.png)
    
    [Introduction | Documentation | Poetry - Python dependency management and packaging made easy](https://python-poetry.org/docs/)
    
    **`poetry init`** 명령을 실행하면, **`pyproject.toml`** 파일을 설정하는 과정이 시작됩니다.
    
    **`pyproject.toml`** 파일은 프로젝트의 메타데이터와 의존성을 관리하는 데 사용되며, Poetry를 사용하는 Python 프로젝트의 핵심 구성 파일입니다.
    
    1. **Package Name**: 프로젝트 또는 패키지의 이름입니다. 일반적으로 프로젝트의 디렉토리 이름을 기본값으로 사용합니다.
    2. **Version**: 패키지의 시작 버전입니다. 일반적으로 **`0.1.0`**으로 시작하며, 개발 진행에 따라 버전을 업데이트합니다.
    3. **Description**: 프로젝트의 간단한 설명입니다. 이 내용은 PyPI 등의 패키지 저장소에 표시됩니다.
    4. **Author Name**: 패키지의 작성자 또는 유지 관리자의 이름입니다. 이 정보는 선택 사항이지만, 공개 패키지의 경우 중요할 수 있습니다.
    5. **License**: 프로젝트에 적용할 라이선스입니다. Open Source 프로젝트의 경우, 일반적으로 MIT, GPL, Apache 등의 라이선스를 사용합니다.
    6. **Compatible Python versions**: 프로젝트가 호환되는 Python 버전을 지정합니다. 예를 들어, **`^3.7`**은 Python 3.7 이상의 버전과 호환됨을 의미합니다.
    
    설정이 완료되면, **`pyproject.toml`** 파일이 프로젝트의 루트 디렉토리에 생성됩니다. 이 파일은 프로젝트의 구성을 정의하고, Poetry가 패키지 관리를 수행하는 데 필요한 모든 정보를 포함합니다.
    
    추가적으로, Poetry는 **`poetry.lock`** 파일을 생성하여 프로젝트의 의존성 트리를 정확하게 재현할 수 있게 해줍니다. 이는 프로젝트가 다양한 환경에서도 동일한 방식으로 작동하도록 보장합니다.
    

<aside>
📌 터미널에서  `charm .` 명령어 또는 PyCharm에서 작업폴더를 연 뒤, 해당 폴더 경로에서 작성하는 명령어는 **로컬 터미널과 파이참 터미널** 두 곳에서 모두 적용이 가능합니다! 두 터미널의 경로가 동일할거에요☺️ 강의 영상에서는 대부분 로컬 터미널에 작성하고 있습니다.

![PyCharm 터미널과 로컬 터미널의 경로가 같은 경우의 예시](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/d31eca8a-891d-4d68-ac9a-5dee5b56d26c/Untitled.png)

PyCharm 터미널과 로컬 터미널의 경로가 같은 경우의 예시

</aside>

```bash
# Django 설치
poetry add django

# 설치된 Django 버전이 5미만인 경우
poetry add django==5.0.3

# PyCharm에서 작업 폴더를 열고 Python Interpreters를 만들었던 oz 가상환경으로 설정한다.

# 기초적인 설정 파일이 들어간 폴더 config를 생성
django-admin startproject config .

# 로컬 개발 서버 실행 후 http://127.0.0.1:8000 로 접속합니다
python3 manage.py runserver

```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/a3cdffc0-fcb8-4e7a-81ee-07e36086e720/Untitled.png)

### PyCharm 설정

```bash
Setting > Languages & Frameworks > Django 에서
Django projet root의 Settings를 설정한다.
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/e356218e-1e75-4fa7-b066-9fa2bbfbee59/Untitled.png)

- 기본 파일 구조
    
    ```markdown
    	config : 기초적인 설정 파일이 들어간 폴더
    	├── 	__init__.py : Python 패키지를 만들어주는 파일
    	├──	 asgi.py, wsgi.py : 웹 서버와 Django가 통신할 때 연결해주는 역할
    	├──	 settings.py : 각종 설정 파일들
    	└──	 urls.py : url 설정들. 기본적으로 admin만 설정되어있다.
    	manage.py : Django를 실행시키는 명령어를 입력하는 파일
    ```
    

## 간단한 HTTP 응답 만들어보기

- 127.0.0.1:8000 (기본 페이지)
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/b247a6d8-7fef-45f3-aa9d-4540d6361db2/Untitled.png)
    
- 127.0.0.1:8000/book_list/
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/b2ead2dd-e754-42b0-a7e6-2fd1a9c4877c/Untitled.png)
    
- 127.0.0.1:8000/book_list/<int:num>
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/c08447e0-62a0-4748-a400-bbed9339dbed/Untitled.png)
    
- 127.0.0.1:8000/language/<str:lang>/
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/1edfbf84-4f5f-4c3e-9b3b-d78e67c0b2db/Untitled.png)
    
- 완성 코드
    
    ```python
    # config > urls.py
    
    from django.contrib import admin
    from django.urls import path
    from django.http import HttpResponse # HttpResponse 모듈 import
    
    def index(request):
    	return HttpResponse('<h1>hello</h1>')
    	
    	
    def book_list(request):
        book_text = ''
    
        for i in range(0,10):
            book_text += f'book {i}<br>'
    
        return HttpResponse(book_text)
        
        
    def book(request, num):
        book_text = f'book {num}번 페이지입니다'
        return HttpResponse(book_text)
        
        
    def language(request, lang):
        return HttpResponse(f'<h1>{lang} 언어 페이지입니다.')
    
    urlpatterns = [
    		path('admin/', admin.site.urls), # 기본적으로 Django에서 제공하는 관리자페이지 url
    		path('', index), 
    		path('book_list', book_list), 
    		path('book_list/<int:num>/', book), 
    		path('language/<str:lang>/', language),
    ]
    ```
    

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/f879c997-c7a9-4e19-9d71-be610d502a14/Untitled.png)

<aside>
⚠️ urlpatterns에 등록되지 않은 url을 조회할 경우 Not found 404 에러!

</aside>

## 가짜 DB 활용해보기

### 가짜 DB를 추가하고 활용해보기

- http://127.0.0.1:8000/movie/
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/948ae9a0-0bc1-44b5-be6d-8310fb47d283/Untitled.png)
    
- http://127.0.0.1:8000/movie/<int:index>
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/34f66db7-5fe3-4ec5-92ea-5ba33495ea25/Untitled.png)
    
- 완성 코드
    
    ```python
    from django.contrib import admin
    from django.urls import path
    from django.http import HttpResponse, Http404
    
    # 가짜 DB
    movie_list = [
        {'title': '파묘', 'director': '장재현'},
        {'title': '웡카', 'director': '폴 킹'},
        {'title': '듄: 파트 2', 'director': '드니 빌뇌브'},
        {'title': '시민덕희', 'director': '박영주'},
    
    ]
    
    def movies(request):
        movie_titles = [movie['title'] for movie in movie_list]
    
        response_text = '<br>'.join(movie_titles)
        return HttpResponse(response_text)
        
        
    def movie_detail(request, index):
    		# 예외처리
    		# movie_list의 데이터 개수보다 큰 index 입력 시
    		# 404 Error를 보여줍니다.
    		
        if index > len(movie_list) - 1: 
        raise Http404
        
        movie = movie_list[index]
    
        response_text = f'<h1>{movie["title"]}</h1> <p>감독: {movie["director"]}</p>'
        return HttpResponse(response_text)
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('movie/', movies),
        path('movie/<int:index>/', movie_detail),
    ]
    
    ```
    

---

### 영화 제목을 클릭하면 해당 영화의 상세페이지로 이동하는 기능 구현

~~결과물의 폰트와 크기가 다른 것은 Safari / Chrome 브라우저의 차이니 신경쓰지 말아주세요!~~

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/653036ce-b29d-48fc-85fd-b8e2bf856e4d/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/18b4c749-ad33-4d05-8231-7b2ab5fd1185/Untitled.png)

- 완성 코드
    
    ```python
    def movies(request):
        movie_titles = [movie['title'] for movie in movie_list]
    
        response_text = ''
    
        for index, title in enumerate(movie_titles):
            response_text += f'<a href="/movie/{index}/">{title}</a><br>'
        return HttpResponse(response_text)
    
    def movie_detail(request, index):
        if index > len(movie_list) - 1:
            raise Http404
        movie = movie_list[index]
    
        response_text = f'<h1>{movie["title"]}</h1> <p>감독: {movie["director"]}</p>'
        return HttpResponse(response_text)
        
        
    # movie 함수 같은 결과를 보여주는 다른 코드
    def movies(request):
        movie_titles = [
            f'<a href="/movie/{index}/">{movie['title']}</a>'
            for index, movie in enumerate(movie_list)
        ]
    
        response_text = '<br>'.join(movie_titles)
    
        return HttpResponse(response_text)
    ```
    

## Django Template 설정 및 문법

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/bbec122d-8eac-4bac-9230-3b0c27325348/Untitled.png)

1. `manage.py` 파일이 있는 경로에 `templates` 폴더를 만든 후 `movies.html` 파일을 생성합니다.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/c8306a4f-bfb7-4fac-94b7-f1bd073792d8/Untitled.png)
    

```python
## urls.py

from django.shortcuts import render

def movies(request):
    return render(request, 'movies.html', {'movie_list':movie_list})
```

1. `setting.py` 에서 Template 경로를 설정합니다.

```python
## settings.py

# BASE_DIR의 경로를 복사하여
# TEMPLATES 설정의 DIRS에 붙여넣습니다.

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

<aside>
💡 **BASE_DIR** 
manage.py 파일을 포함하고 있는 프로젝트 경로를 의미한다. (여기서는 bookmark 프로젝트의 경로)

</aside>

1. `movies.html` 파일을 작성합니다

```html
## movies.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    {% for movie in movie_list %}
        {% if forloop.counter <= 3 %}
            {{ forloop.counter }}위: <a href="/movie/{{ forloop.counter0 }}">{{ movie.title }}</a><br>
        {% endif %}
    {% endfor %}
</body>
</html>
```

<aside>
☝ enumerate 함수는 Temaplate 문법에서는 사용할 수 없어요!
대신 Django 환경에서는 `forloop.counter` 를 제공합니다.
단,  `forloop.count` 는 1번부터 돌아가기 때문에 그대로 사용하면 
웹페이지에서 ‘파묘’의 링크가 </movie/1>로 설정되어,
눌렀을 때 ‘웡카’의 상세페이지로 이동하게 됩니다! 
0을 붙여 `forloop.count0` 로 올바르게 사용할 수  있습니다.

</aside>

```html
## 파이프(|) 이용해서 forloop.counter 에 연산하기

# 덧셈
{{ forloop.counter | add:5 }}

# 뺄셈
{{ forloop.counter | add:-3 }}
```

## Django Template을 이용한 페이지 만들기

### 영화 페이지 만들기

- http://127.0.0.1:8000/movie/0/
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/be6bfad2-003a-41d2-9a68-1684e6963007/Untitled.png)
    
1. 기존 `urls.py` 를 활용하여 코드를 수정합니다.

```python
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, Http404

def movie_detail(request, index):
    if index > len(movie_list) - 1:
        raise Http404

    movie = movie_list[index]

    context = {'movie': movie}
    return render(request, 'movie.html', context)
```

1. Templates 폴더에 `movie.html` 을 생성합니다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>{{ movie.title }}</h1>
    <p>감독: {{ movie.director }}</p>
</body>
</html>
```

### 도서 페이지 만들기

- http://127.0.0.1:8000/book_list/
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/d5d88860-088b-442c-b491-0bdd784622e5/Untitled.png)
    
- http://127.0.0.1:8000/book_list/<int:num>/
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/c9e52e12-00a7-4e6c-b29a-4f9cfd3cb214/Untitled.png)
    
1. 기존 `urls.py` 를 활용하여 코드를 수정합니다.

```python
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, Http404

    
def book_list(request):
    book_text = ''

    return render(request, 'book_list.html', {'range': range(0, 10)})

def book(request, num):

    return  render(request, template_name='book_detail.html', context={'num': num})
```

1. Templates 폴더에 `book_list.html` 을 생성합니다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    {% for num in range %} 
        <h1> Book {{ num }}</h1>
    {%  endfor %}
</body>
</html>
```

1. Templates 폴더에 `book_detail.html` 을 생성합니다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title </title>
</head>
<body>
    <h1>book {{ num }}번 페이지입니다.</h1>
</body>
</html>
```

---

## 🔥 Mini Project! Django Template을 이용한 구구단 페이지 만들기

<aside>
✅ localhost:8000/gugu/n/ 에 접속했을 때 구구단 n단이 출력되도록 만들어주세요.

</aside>

### 완성 예시

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/00feaf78-d356-41ee-90f9-616e7f73fd77/e2969e6c-d00b-4dda-bbaf-b6d3006e387c/Untitled.png)

- 완성 예시 코드
    
    예시 코드와 똑같을 필요 없습니다! 다양한 방법으로 구구단 페이지를 만들어주세요☺️ 
    
    ```python
    ## urls.py
    
    def gugu(request, num):
        context = {
            'num': num,
            'results': [num * i for i in range(1, 10)]
        }
        return render(request, 'gugu.html', context)
        
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('gugu/<int:num>/', gugu),
    ]
    
    ```
    
    ```html
    ## gugu.html
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <h1>{{ num }}단</h1>
        {% for result in results %}
            <p>{{ num }} x {{ forloop.counter }} = {{ result }}</p>
        {% endfor %}
    </body>
    </html>
    ```