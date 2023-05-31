pipeline {
agent any
stages {
    stage ('GIT Checkout'){
        steps {
            git changelog: false, poll: false, url: 'https://github.com/MaksimPotrus/selenium_ide.git'
        }
    }
    
    stage('build') {
  steps {
      sh '/usr/bin/python3 -m pip3.10 install --upgrade pip'
    sh 'pip3.10 install -r requirements.txt'
  }
}
    stage ('Test'){
        steps {
            sh 'pytest test_login.py'
        }
    }
}
}
