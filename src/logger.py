import logging

logging.basicConfig(filename='app.log', level=logging.INFO, format=' %(asctime)s : %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

type_switch = { 'info': logging.info, 'warning': logging.warning, 'error': logging.error }
'''Function switcher'''


def info_log(message):
    '''Default info log message writer'''
    __show_log(message, 'info')


def error_log(message):
    '''Default error log message writer'''
    print("An error has ocurred, check the app logs for more information.")
    __show_log(message, 'error')
    

def warning_log(message):
    '''Default warning log message writer'''
    __show_log(message, 'warning')


def __show_log(message, type):
    '''Default type message switcher'''
    type_switch[type](message)