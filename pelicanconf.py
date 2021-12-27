AUTHOR = 'JackDali'
SITENAME = 'JackDali'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

THEME = 'mytheme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('tgicon.png', 'https://telegram.org/'),
          ('tgicon.png', 'https://github.com/jackdali'),
          ('tgicon.png', '#hackthebox'),
          ('tgicon.png', '#'))

DEFAULT_PAGINATION = 10

MENUITEMS = [('Home','index'),('About','pages/about'),('Articles','archives'),('Contact','pages/contact')]
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives'))
PAGINATED_DIRECT_TEMPLATES = (('index', 'archives'))

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True