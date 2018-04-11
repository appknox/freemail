[![Build Status](https://travis-ci.org/wearespindle/freemail.svg?branch=master)](https://travis-ci.org/wearespindle/freemail)

# freemail

A database of free and [disposable](http://en.wikipedia.org/wiki/Disposable_email_address)
email domains and a handy Node.js module for querying it.

Install via npm or pip or access the files in the `./data` directory and parse
with your language of choice.

In an effort to create the most up-to-date list of domains, the database can be
synchronized with various lists from around the web. You can also add new
domains directly by opening a pull request.

## Database

There are three key data files in this project:

- [free.txt](https://github.com/wearespindle/freemail/blob/master/freemail/data/free.txt) contains a list of domains that are known to provide free email service
- [disposable.txt](https://github.com/wearespindle/freemail/blob/master/freemail/data/disposable.txt) contains a list of domains that are known to provide disposable email service
- [blacklist.txt](https://github.com/wearespindle/freemail/blob/master/freemail/data/blacklist.txt) contains a list of domains that this project will refuse to add to either list

Domains may only be a member of one list.

## Updating the database

Run `./update` to pull in the latest domains from the sources listed in
`sources.txt`. All new domains will be placed in `free.txt` by default.
If any domains provide disposable email service, they may be moved to
`disposable.txt`.

## Python

### Install

```
pip install freemail
```

```python
>>> import freemail
>>> freemail.is_free('smith@gmail.com')
True
>>> freemail.is_free('jack@mailinater.com')
True
>>> freemail.is_disposable('smith@gmail.com')
False
>>> freemail.is_disposable('jack@mailinater.com')
True
```

## Other

- [freemail-cli](https://github.com/danielstjules/freemail-cli) is a CLI tool for filtering free and disposable emails
