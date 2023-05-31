pipeline {
	agent any
	stages {
		stage('GIT Checkout') {
			steps {
				git changelog: false, poll: false, url: 'https://github.com/MaksimPotrus/selenium_ide.git'
			}
		}

		stage('build') {
			steps {
			    sh 'python3.10 -m pip install --upgrade pip'
				sh 'pip3 install -r ./requirements.txt'
			}
		}
			stage('Test') {
				steps {
					sh 'python3.10 pytest --version'
					sh 'python3.10 -m pytest test_login.py'
				}
			}
		}
	}