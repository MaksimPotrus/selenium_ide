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
				sh 'python3.10 -m pip install -r ./requirements.txt'
			}
		}
			stage('Test') {
				steps {
					sh 'python3.10 -m pytest test_login.py --html=reports/report.html --self-contained-html'
				}
			}
		}
	}