import setuptools
from scrapyhttppipeline.version import Version

setuptools.setup(name='scrapy-http-pipeline',
                 version=Version('0.1.5').number,
                 description='Scrapy HTTP POST items pipeline',
                 long_description=open('README.md').read().strip(),
                 author='Vladimír Kuchár',
                 author_email='kuchar.vladimir@gmail.com',
                 url='https://github.com/thecodecook/scrapy-http-pipeline',
                 py_modules=['scrapyhttppipeline'],
                 install_requires=[
                     'scrapy',
                     'requests>=2.23.0',
                     'six>=1.14.0',
                 ],
                 packages=setuptools.find_packages(),
                 license='MIT License',
                 long_description_content_type='text/markdown',
                 keywords='scrapy http pipeline export items',
                 classifiers=['Development Status :: 3 - Alpha',
                              'Environment :: No Input/Output (Daemon)',
                              'License :: OSI Approved :: MIT License',
                              'Operating System :: OS Independent',
                              'Programming Language :: Python'
                              ])
