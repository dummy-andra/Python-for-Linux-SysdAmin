import logging

applog = logging.getLogger("app")
#applog.setLevel(logging.INFO)
applog.addHandler(logging.FileHandler('app.log'))

applog.info('info message')
applog.critical('critical message')
