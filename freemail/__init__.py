import os
import tldextract
import subprocess

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
free_file = os.path.join(__location__, './data/free.txt')
disp_file = os.path.join(__location__, './data/disposable.txt')


def is_free(email_address):
    try:
        email_address = str(email_address)
    except:
        raise TypeError('email must be a string')

    with open(free_file, 'r') as free, open(disp_file, 'r') as disposable:
        domain_list = free.read().splitlines() + disposable.read().splitlines()
        domain = tldextract.extract(email_address.split('@')[1]).registered_domain

        return domain in domain_list


def is_disposable(email_address):
    try:
        email_address = str(email_address)
    except:
        raise TypeError('email must be a string')

    with open(disp_file, 'r') as disposable:
        domain_list = disposable.read().splitlines()
        domain = tldextract.extract(email_address.split('@')[1]).registered_domain

        return domain in domain_list


def update():
    try:
        subprocess.call("./update", shell=True)
        return True
    except subprocess.CalledProcessError:
        return False
