# Cài đặt Netbox trên CentOS 7 

```
hostnamectl set-hostname netbox
```

```
yum -y install epel-release
```


```
yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
```

```
yum install -y postgresql96 postgresql96-server postgresql96-libs postgresql96-contrib postgresql96-devel
``` 

```
/usr/pgsql-9.6/bin/postgresql96-setup initdb
```

```
systemctl start postgresql-9.6
```

```
systemctl enable postgresql-9.6
```

```
sudo -u postgres psql
```
Sau đó thực hiện các câu lệnh sau để tạo cơ sở dữ liệu cho netbox

```
CREATE DATABASE netbox;
CREATE USER netbox WITH PASSWORD '<strong_pass>';
GRANT ALL PRIVILEGES ON DATABASE netbox TO netbox;
\q
```


# Cài đặt Redis

```
yum install -y redis
```
```
systemctl start redis
```

```
systemctl enable redis
```


# Install netbox 

```
yum install -y gcc python36 python36-devel python36-setuptools libxml2-devel libxslt-devel libffi-devel openssl-devel redhat-rpm-config
```

```
cd
wget https://github.com/netbox-community/netbox/archive/vX.Y.Z.tar.gz
```

```
tar -xzf vX.Y.Z.tar.gz -C /opt
cd /opt/
ln -s netbox-X.Y.Z/ netbox
cd /opt/netbox/
```

```
yum install -y git
```
```
git clone -b master https://github.com/netbox-community/netbox.git .
```

Tạo user netbox 

```
adduser --system --group netbox
chown --recursive netbox /opt/netbox/netbox/media/
```

Thiết lập môi trường python 


```
python3 -m venv /opt/netbox/venv
```


```
source venv/bin/activate

pip3 install -r requirements.txt
```


Cấu hình

```
cd netbox/netbox
```
```
cp configuration.example.py configuration.py
```

```
vi configuration.py
```

Sau đó chỉnh sửa các thông số sau : 
```
ALLOWED_HOSTS = ['netbox.example.com', '192.0.2.123']
```
```
DATABASE = {
    'NAME': 'netbox',               # Database name
    'USER': 'netbox',               # PostgreSQL username
    'PASSWORD': 'J5brHrAXFLQSif0K', # PostgreSQL password
    'HOST': 'localhost',            # Database server
    'PORT': '',                     # Database port (leave blank for default)
    'CONN_MAX_AGE': 300,            # Max database connection age
}
```

```
REDIS = {
    'tasks': {
        'HOST': 'redis.example.com',
        'PORT': 1234,
        'PASSWORD': 'foobar',
        'DATABASE': 0,
        'DEFAULT_TIMEOUT': 300,
        'SSL': False,
    },
    'caching': {
        'HOST': 'localhost',
        'PORT': 6379,
        'PASSWORD': '',
        'DATABASE': 1,
        'DEFAULT_TIMEOUT': 300,
        'SSL': False,
    }
}
```
Tạo khóa : 



```
cd /opt/netbox/netbox/
python3 manage.py migrate
```


```
python3 manage.py admin
```


```
python3 manage.py collectstatic --no-input
```

Chạy dịch vụ netbox

```
python3 manage.py runserver 0.0.0.0:8000 --insecure
```

