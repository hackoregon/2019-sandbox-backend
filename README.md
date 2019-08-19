# hackoregon_sandbox

![PyPI version](https://badge.fury.io/py/2019-sandbox-backend.svg) | [![Build Status](https://travis-ci.org/hackoregon/2019-sandbox-backend.svg?branch=master)](https://travis-ci.org/hackoregon/2019-sandbox-backend)

2019 Sandbox Backend

# Documentation

The full documentation is at http://hackoregon.github.io/2019-sandbox-backend


# Features

> -   TODO (add what your project does)

# Data Sources

This API package in this repo is based on the Data Science work in the following projects:

* [2019-sandbox-data-science](https://github.com/hackoregon/2019-sandbox-data-science)

# Quickstart to install package in your own Django Project (Non-Hack Oregon Workflow)

* Install hackoregon_sandbox:  
  `pip install hackoregon_sandbox`

* Add subpackages to your `INSTALLED_APPS`:

  ```python
  INSTALLED_APPS = [     
                      ...     
                      'api',     
                      ...
                    ]
  ```

* Add hackoregon_sandbox's URL patterns:

  ```python
  from hackoregon_sandbox.api
  import urls as api_urls   

  urlpatterns = [     
                  ...     
                  url(r'^', include(api_urls)),     
                  ...
                ]
  ```

* Setup your database with a matching schema

* Run the project

# Running Tests

This repo uses pytest and pytest-django to run tests.

For project development work, tests will be run in docker container
using the bin/test.sh script:

# Deployment

This repo is intended to be used in conjunction with a Travis CI based automated deploy chain to push projects to an AWS Fargate cluster

Prerequisites:

* [bumpversion](https://github.com/peritus/bumpversion#installation) - install on local computer, used for version management

Basic Steps:

1. Branches can be pushed/merged in Github. Automated tests will be run. Unless a tagged push is made, app will not deploy
2. When ready to deploy a new version, you'll confirm you have merged all latest code into your deployment branch (perhaps master?) and have this pulled to your local computer

3. Create a tagged commit using bumpversion, following semantic versioning:
v[major].[minor].[patch]

Lets take an example:
If the current version was `v1.10.4` and you wanted to update the minor portion (ie: a non-breaking but significant change), you will run the following command:

```
bumpversion minor --config-file ./hackoregon_sandbox/setup.cfg
```

this would then update the version to `v1.11.0`

to then create a patch update,

```
bumpversion patch --config-file ./hackoregon_sandbox/setup.cfg
```
Version will then become: `v1.11.1`

In the background - `bumpversion` checks in the `setup.cfg` file for any `bumpversion:file` entries for which to regex for the version tag syntax, which in this case is the VERSION file which contains the current version. Bumpversion then looks at the part you specify and updates that portion accordingly

Additionally and importantly for the deploy chain, it will also add a `git tag` with the version number.

4. Once you have created the new tagged version of your repo, you can go ahead and push a tagged release to github:

```
git push origin <version-tag>
```
5. Once you push this, Travis should run through it's testing/build cycle and then provided necessary env variables are configured in Travis and AWS services, deploy to the cloud.


# Credits

Tools used in rendering this package:

 * [Cookiecutter](https://github.com/audreyr/cookiecutter)
 * [cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage)
