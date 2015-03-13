from setuptools import setup, find_packages

setup(
  name = 'qrgen',
  packages = find_packages(),
  version = '0.5',
  description = 'Turn a URL into a QR code',
  author = 'Roy Keys',
  author_email = 'roy.coding@gmail',
  url = 'https://github.com/RJ-Skunkworks/qr',
  download_url = 'https://github.com/RJ-Skunkworks/qr/tarball/v0.5',
  keywords = ['qr', 'url', 'qrcode'], 
  classifiers = [],
  install_requires=['qrcode'],
)