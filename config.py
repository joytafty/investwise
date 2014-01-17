import os

_basedir = os.path.abspath(os.path.dirname(__file__))

# mysql database
DATABASE = 'insightdata'
DB_USER = os.getenv('DB_USER')
DB_PWD = os.getenv('DB_PWD')

# flask
DEBUG = True

SECRET_KEY = 'SecretKeyForSessionSigning'

CSRF_ENABLED = True
CSRF_SESSION_KEY = 'somethingimpossibletoguess'

SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{pwd}@localhost/insightdata?charset=utf8'.format(user=DB_USER, pwd=DB_PWD)
DATABASE_CONNECT_OPTIONS = {}

# json files folders
CB_COMPANY_FOLDER = 'scraper/scraper/crunchbase_company_json'
CB_PEOPLE_FOLDER = 'scraper/scraper/crunchbase_people_json'
CB_FINANCIAL_FOLDER = 'scraper/scraper/crunchbase_financial_json'

AL_COMPANY_FOLDER = 'scraper/scraper/angellist_company_json'
AL_PEOPLE_FOLDER = 'scraper/scraper/angellist_people_json'

# API keys
LINKEDIN_API_KEY = os.getenv('LINKEDIN_API_KEY')
LINKEDIN_SECRET_KEY = os.getenv('LINKEDIN_SECRET_KEY')

TWITTER_CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_TOKEN_SECRET')

ANGELLIST_TOKEN = os.getenv('ANGELLIST_TOKEN')	
CRUNCHBASE_API_KEY = os.getenv('CRUNCHBASE_API_KEY')

BITLY_ACCESS_TOKEN = os.getenv('BITLY_ACCESS_TOKEN')