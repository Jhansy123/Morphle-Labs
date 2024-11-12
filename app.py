from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Fetch username from system
    user = os.getenv("USER", "codespace")
    
    # Get the current time in IST
    ist_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    
    # Run the `top` command and capture the output
    top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    
    # Format the output as an HTML page
    html_content = f"""
    <html>
    <head><title>HTop Endpoint</title></head>
    <body>
        <h1>Name: Madamanchi Jhansy</h1>
        <h2>User: {user}</h2>
        <h3>Server Time (IST): {ist_time}</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
