from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Deployed on ECS with EC2 via CodePipeline!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
