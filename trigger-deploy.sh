#! /bin/bash

bumpversion $1 --config-file ./hackoregon_sandbox/setup.cfg  && git push && git push --tags