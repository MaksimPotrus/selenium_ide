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
    sh 'pip3 install pytest'
    sh 'pip3 install selenium'
  }
}
    stage ('Test'){
        steps {
            sh 'pytest test_login.py'
        }
    }
}
}
