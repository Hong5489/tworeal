#!/bin/bash

cd /2real/ICSharpCode.Decompiler.Console
dotnet tool install ilspycmd -g
chmod +x ~/.dotnet/tools/ilspycmd
echo "export PATH=~/.dotnet/tools:\$PATH" >> ~/.bashrc
cd /2real
uwsgi --socket 0.0.0.0:80 --protocol=http -w wsgi:app --logto /tmp/log
