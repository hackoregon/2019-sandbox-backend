#! /bin/bash

set -x

git archive --format=tar.gz -o $PROJECT_NAME-$TRAVIS_TAG.tar.gz --prefix=$PROJECT_NAME-$TRAVIS_TAG/ $TRAVIS_TAG;