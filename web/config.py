import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="techconfdbserver.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="azureuser@techconfdbserver" #TODO: Update value
    POSTGRES_PW="2991@Thandar"   #TODO: Update value
    POSTGRES_DB="techconf-db"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://servicebus-notificationqueue.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=lkjbRGXXf0jbHuDcL2DIaQ0JsGCrdk0Ngocx/43m8Q0=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'info@techconf.com'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig): 
    DEBUG = False