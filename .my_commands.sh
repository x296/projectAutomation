#!/bin/bash

function create() {
	python3 /Users/piotrzyzinski/pythonProjects/projectAutomation/create.py $1
	cd /Users/piotrzyzinski/pythonProjects/$1
	git init
	git remote add origin https://github.com/x296/$1.git
	touch README.md
	git add .
	git commit -m 'initialization of a new repo'
	git push -u origin master
	subl .
}