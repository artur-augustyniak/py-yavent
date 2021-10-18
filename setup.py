from setuptools import setup

setup(
    name='yavent',
    version='0.1.0',    
    license='BSD 2-clause',
    packages=['yavent'],
    install_requires=[
        'pika==1.2.0'
    ],

    classifiers=[
        'Development Status :: 1 - Yolo',
        'License :: OSI Approved :: BSD License',  
        'Programming Language :: Python :: 3',
    ],
)    
