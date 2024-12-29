@echo off

cd docs
make html
make latexpdf
cd build\html
if exist rcdb-docs-html.zip del rcdb-docs-html.zip
for /r %%i in (*) do (
    echo %%i >> filelist.txt
)
makecab /d compress=ON /d cabinet=off /f filelist.txt rcdb-docs-html.zip
move rcdb-docs-html.zip ..\..\..
cd ..\latex
move rcdb-docs.pdf ..\..\..
cd ..\..\..
