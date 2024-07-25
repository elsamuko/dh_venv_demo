#!/usr/bin/env bash

cd weather || exit
dpkg-buildpackage -us -uc -b
