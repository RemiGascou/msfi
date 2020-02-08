# -*- coding: utf-8 -*-

class VersionInfos(object):
    """docstring for VersionInfos."""
    def __init__(self):
        super(VersionInfos, self).__init__()
        self.name         = 'bioinfoutils',
        self.version      = '0.1.2',
        self.description  = 'Basic tools needed in bioinformatics',
        self.url          = 'http://github.com/Remigascou/bioinfoutils',
        self.author       = 'Remi GASCOU',
        self.author_email = 'remi.gascou@gmail.com',
        self.license      = 'GPL2',
        self.packages     = ['bioinfoutils'],
        self.zip_safe     = False

    def get_name(self):
        return self.name

    def get_version(self):
        return self.version

    def get_description(self):
        return self.description

    def get_url(self):
        return self.url

    def get_author(self):
        return self.author

    def get_author_email(self):
        return self.author_email

    def get_license(self):
        return self.license

    def get_packages(self):
        return self.packages

    def get_zip_safe(self):
        return self.zip_safe
