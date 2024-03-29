@echo off

cd docs
make html
tar -a -c -f ..\..\..\rcdb-docs.zip *