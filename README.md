## KHUropbox

<p align="center"><img width="200" src="static/image/header.png" /></p>

클라우드 플랫폼을 사용한 2019년 1학기 클라우드 컴퓨팅 과목 팀 프로젝트입니다. 팀원 들의 원할한 소통을 위해 영어보다 한국어로 작성되었습니다.



##### Notice

- 새로운 기능 구현 시 branch로 관리 혹은 fork에서 자신 repository에서 구현 후 Pull Request로 합쳐주세요.
- 버그, Trouble Shooting은 Issue를 활용해주세요.



##### 구현 목록(및 예정)

- [x] 로그인, 회원가입  

- [ ] 비밀번호 수정

- [ ] S3 기반 파일 업로드, 삭제

- [ ] AWS 플랫폼 DB 기반(MySQL 예정) migration 연동

- [ ] 외부인과 파일 공유, Session Problem

- [ ] 도커 가상화(Dockerfile) 예정

- [ ] Elastic Beanstalk와 Elastic Load Balancing을 사용한 부하분산처리

  

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

$ python manage.py migrate
$ python manage.py runserver
```



## Dependancy

- django==2.1.7
- Pillow==5.4.1
- djangorestframework==3.9.2



## Team Members

- 정다은
- 정의동
- 정태환(@graykode)
- 조아진