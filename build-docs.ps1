#!/usr/bin/pwsh

cd docs
& .\make html
& .\make latexpdf
cd build\html
Compress-Archive -Path * -DestinationPath rcdb-docs-html.zip
Move-Item rcdb-docs-html.zip -Destination ..\..\..
cd ..\latex
Move-Item rcdb-docs.pdf -Destination ..\..\..
cd ..\..\..
