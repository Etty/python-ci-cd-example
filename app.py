from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """Hello, I am Anastasiia Yermolik!<br> 
    Yes, I'm an experienced Magento developer, 
    but now I'm looking for new oppoptunities and discovering another directions.<br>    
    This sample project demonstrates my knowledge of CI/CD technology and Python fundamentals.<br>
    Also I learn Java and gained OCA certification<br>
    Also I am a beginner Blockchain developer<br>
    And also continue learning AI-driven development<br>
    Please follow my 
    <a href='https://www.linkedin.com/in/anastasiia-yermolik-b39140b9/' target='_blank'>
    LinkedIn profile</a>
    for more info"""
