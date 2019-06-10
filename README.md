## KHUropbox

<p align="center"><img width="200" src="static/image/header.png" /></p>

클라우드 플랫폼을 사용한 2019년 1학기 클라우드 컴퓨팅 과목 팀 프로젝트입니다. 팀원 들의 원할한 소통을 위해 영어보다 한국어로 작성되었습니다.



##### Notice

- 새로운 기능 구현 시 branch로 관리 혹은 fork에서 자신 repository에서 구현 후 Pull Request로 합쳐주세요.
- 버그, Trouble Shooting은 Issue를 활용해주세요.



##### 구현 목록(및 예정)

- [x] 로그인, 회원가입  

- [x] 비밀번호 수정

- [x] S3 기반 파일 업로드, 삭제

- [x] AWS 플랫폼 DB 기반(MySQL 예정) migration 연동

- [x] 외부인과 파일 공유, Session Problem

- [x] Auto Scaling Group와 Elastic Load Balancing을 사용한 부하분산처리

- [x] 게시판 및 댓글 기능, DB 구조화

- [x] S3에서 파일 이름으로 인한 검색

- [x] 사용자 마다 Bucket 폴더 나누기, 회원가입시 고유 Bucket 폴더 생성

- [x] 대용량 파일 업로드에 대한 aws cognito 설정

  

**추후에 AWS 이용할 때 AWS 키 안올리도록 주의해주세요.**



## Quick Start

```shell
$ git clone https://github.com/khuropbox/khuropbox && cd khuropbox
$ sudo apt install virtualenv python3-pip
$ pip3 install virtualenv

$ ln -s /home/ubuntu/.local/bin/virtualenv virtualenv
$ ./virtualenv env
$ source env/bin/activate

$ pip3 install -r requirement.txt

$ vim config.ini
[db]
ENGINE = django.db.backends.postgresql
HOST = RDS_hostnae
PORT = RDS_port
NAME = RDS_name
USER = RDS_user
PASSWORD = RDS_password

[aws]
AWS_ACCESS_KEY_ID = your_key
AWS_SECRET_ACCESS_KEY = your_secret_key
AWS_STORAGE_BUCKET_NAME = your_bucket_name

[cognito]
region = ap-northeast-2
user_pool_id = 
app_client_id = 
identity_pool_id = 
account_id = 

$ python manage.py migrate
$ python manage.py runserver 0:8000
```

## Multi-Part Upload를 위한 S3 Policy 설정
```xml
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>POST</AllowedMethod>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>PUT</AllowedMethod>
    <AllowedMethod>DELETE</AllowedMethod>
    <AllowedMethod>HEAD</AllowedMethod>
    <ExposeHeader>ETag</ExposeHeader>
    <AllowedHeader>*</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```

## Dependancy

- boto3==1.9.145
- botocore==1.12.146
- Django==2.1.7
- djangorestframework==3.9.2
- docutils==0.14
- jmespath==0.9.4
- Pillow==5.4.1
- psycopg2==2.8.2
- python-dateutil==2.8.0
- pytz==2019.1
- s3transfer==0.2.0
- six==1.12.0
- urllib3==1.24.3




## Team Members

- 정다은
- 정의동 
- 정태환(@graykode)
- 조아진