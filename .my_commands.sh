#!/bin/bash

function create() {
	python3 /Users/piotrzyzinski/pythonProjects/projectAutomation/create.py $1
	cd /Users/piotrzyzinski/pythonProjects/$1
	# git init
}