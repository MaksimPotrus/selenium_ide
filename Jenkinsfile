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
    sh 'pip3 install pytest==4.9.1'
    sh 'pip3 install selenium'
      sh 'pip3 install async-generator'
      sh 'pip3 install attrs'
      sh 'pip3 install certifi'
      sh 'pip3 install cffi'
      sh 'pip3 install charset-normalizer'
      sh 'pip3 install h11'
      sh 'pip3 install idna'
      sh 'pip3 install iniconfig'
      sh 'pip3 install outcome'
      sh 'pip3 install packaging'
      sh 'pip3 install pluggy'
      sh 'pip3 install py'
      sh 'pip3 install pycparser'
        sh 'pip3 install PySocks'
        sh 'pip3 install pytest-html'
        sh 'pip3 install pytest-metadata'
        sh 'pip3 install python-dotenv'
        sh 'pip3 install requests'
        sh 'pip3 install selenium'
        sh 'pip3 install sniffio'
       sh 'pip3 install sortedcontainers'
        sh 'pip3 install tomli'
        sh 'pip3 install tqdm'
        sh 'pip3 install trio'
        sh 'pip3 install trio-websocket'
        sh 'pip3 install webdriver-manager'
        sh 'pip3 install wsproto'
      sh 'pip3 install six'
  }
}
    stage ('Test'){
        steps {
            sh 'pytest test_login.py'
        }
    }
}
}
