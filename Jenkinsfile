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
    sh 'python3 install -r requirements.txt'
    sh 'python3 install pytest'
  }
}
    stage ('Test'){
        steps {
            sh 'python3 test_login.py'
        }
    }
}
}
