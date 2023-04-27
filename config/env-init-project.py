# Use this file to set project specific settings
# "project" here means a fork of the upstream ShahimEssaid/hapi-compose-setup for a use by a project
# This file should focus on setting HS_PROFILES and other variables to values needed by all the "run instances"
# of the project.
# A local "run" of the project can further override the settings for the local "instance" in env-init-local.py
# to set instance specific values.

# See config/env-init-local-example.py for possible values to set here or in the local file.
# The full list of environment variables is in config/env-defaults.py.

import os

os.environ['HS_PROFILES'] = os.environ.get('HS_PROFILES', 'env-defaults,hs-defaults,hs-postgresql,hs-elasticsearch,tims,hs-project,hs-local')

# TIMS uses this port offset
os.environ['HS_PORT_OFFSET'] = os.environ.get('HS_PORT_OFFSET', '10000')

# The following commented out lines can go into local if needed
# # Set the following to your actual environment.
# environ['HS_HAPI_HOST'] = '0.0.0.0'
# environ['HS_HAPI_HOST_PUBLIC'] = '20.3.198.176'


os.environ['HS_HAPI_BUILD_GIT_REPO'] = 'https://github.com/HOT-Ecosystem/tims-hapi-build.git'
os.environ['HS_HAPI_BUILD_GIT_REF'] = 'origin/dev'
os.environ['HS_HAPI_BUILD_CMD'] = 'mvn -U -Dmaven.test.skip clean package'
os.environ['HS_HAPI_BUILD_ALWAYS'] = 'true'

