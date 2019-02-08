#!/bin/bash
for dir in $(find -L -name "migrations")
do
  rm -Rf $dir/*
done
