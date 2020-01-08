# 순서
1. Django 프로젝트를 생성한다.
2. GDAL을 설치한다.
 
    brew install gdal --HEAD
    
    sudo easy_install GDAL

3. settings.py에  'django.contrib.gis', 를 추가한다.

4. https://postgresapp.com/downloads.html 에서 다운로드

5. pip install psycopg2-binary

6. settings.py에 추가
~~~~
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # 'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_test',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',

    },
}
~~~~
7. psql command line 입력

8. create user root with password 'password';

9. 원하는대로 Database 만들기
