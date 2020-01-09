import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()
try:
    with open(os.path.join(base_path, 'requirements.txt'), encoding='utf-8') as f:
        REQUIREMENTS = f.read().split('\n')

except Exception:
    REQUIREMENTS = []


setuptools.setup(

     name='m2dp',  

     version='0.1.2',

     scripts=['m2dp/__init__.py','m2dp/M2DP.py'],
     author="Adnan64",
     description="A python implementation of M2DP .",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url='https://github.com/adnan33/M2DP-python',
     packages=setuptools.find_packages(),
     
     license = 'MIT',
     install_requires=REQUIREMENTS,
     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )
