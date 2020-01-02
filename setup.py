import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()
try:
    with open(os.path.join(base_path, 'requirements.txt'), encoding='utf-8') as f:
        REQUIREMENTS = f.read().split('\n')

except Exception:
    REQUIREMENTS = []


setuptools.setup(

     name='mobilenet-v3',  

     version='0.1.4',

     scripts=['mobilenet_v3/__init__.py','mobilenet_v3/LR_ASPP.py','mobilenet_v3/mobilenet_base.py','mobilenet_v3/mobilenet_v3_large.py','mobilenet_v3/mobilenet_v3_small.py','mobilenet_v3/layers/bilinear_upsampling.py'] ,

     author="xiaochus",
     description="A Keras implementation of MobileNetV3.",
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
