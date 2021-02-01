from setuptools import setup, find_packages
print(find_packages())
setup( 
    name='face_toolbox_keras', 
    version='1.0', 
    packages=find_packages(), 
    python_requires='>=3.6, <3.8',
    install_requires=['tensorflow-gpu==1.13.1', 'keras==2.2.4', 'opencv-python'],  # Optional
    include_package_data=True,
)