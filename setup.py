#!/usr/bin/env python

from setuptools import find_packages, setup

with open('README.md') as f:
    long_description = f.read()

setup(name="pipelinewise-target-snowflake-key-auth",
      version="2.2.0",
      description="Singer.io target for loading data to Snowflake - PipelineWise compatible - Forked from Pipelinewise to add compatibility with key pair auth for Snowflake",
      long_description=long_description,
      long_description_content_type='text/markdown',
      author="Wise",
      url='github.com/JamieSplitit/pipelinewise-target-snowflake-key-auth',
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
      ],
      py_modules=["target_snowflake"],
      python_requires='>=3.7',
      install_requires=[
          'pipelinewise-singer-python==1.*',
          'snowflake-connector-python[pandas]==3.15.*',
          'inflection==0.5.1',
          'joblib==1.2.0',
          'boto3==1.24.*',
          'numpy==1.26.4',
      ],
      extras_require={
          "test": [
              "pylint==2.12.*",
              'pytest==7.1.1',
              'pytest-cov==3.0.0',
              "python-dotenv==0.19.*"
          ]
      },
      entry_points="""
          [console_scripts]
          target-snowflake-key-auth=target_snowflake:main
      """,
      packages=find_packages(exclude=['tests*']),
      )
