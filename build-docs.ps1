#! /usr/bin/pwsh

cd docs
.\make html
cd build\html
Compress-Archive * ..\..\..\rcdb-docs.zip -Force
cd ..\..\..
