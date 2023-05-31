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
        sh 'pip3.10 install -r ./requirements.txt'
      }
      stage('Test') {
        steps {
          sh 'pytest --version'
          sh 'pytest test_login.py'
        }
      }
    }
  }