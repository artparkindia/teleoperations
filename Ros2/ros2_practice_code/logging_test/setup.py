from setuptools import setup

package_name = 'logging_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mysorebharath',
    maintainer_email='gb_mys@hotmail.com',
    description='',
    license='',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'logger=logging_test.logger_demo:main',
        'test_logger=logging_test.test_logger:main'
        ],
    },
)
