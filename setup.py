from distutils.core import setup

setup(
    name='sotmjp',
    version='2015-dev',
    packages=['sotmjp',
              'sotmjp.account',
              'sotmjp.profile',
              'sotmjp.registration',
              'sotmjp.schedule', 'sotmjp.sponsorship',
              'sotmjp.sponsorship.management',
              'sotmjp.sponsorship.management.commands',
              'sotmjp.sponsorship.templatetags',
              'sotmjp.tutorials',
              'markedit'],
    url='https://github.com/osmfj/sotmjp-website/',
    license='LICENSE',
    author='Hiroshi Miura',
    author_email='miurahr@osmf.jp',
    description='State of the Map Japan website on Symposion'
)
