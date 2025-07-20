from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("""
    <html>
        <head>
            <title>Welcome - Rama Krishna Palnati</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    line-height: 1.6;
                }
                .container {
                    max-width: 800px;
                    margin: 0 auto;
                }
                .contact-info {
                    margin-top: 20px;
                }
                a {
                    color: #0066cc;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to My Django AWS Project</h1>
                <p>Hello! I'm <strong>Rama Krishna Palnati</strong>, and this is my AWS ECS deployment project.</p>
                
                <div class="contact-info">
                    <h2>Connect with me:</h2>
                    <p>📧 Email: <a href="mailto:Ramakrishnap4121@gmail.com">Ramakrishnap4121@gmail.com</a></p>
                    <p>💼 LinkedIn: <a href="https://www.linkedin.com/in/rama-palnati-530165376/" target="_blank">Rama Palnati</a></p>
                </div>
            </div>
        </body>
    </html>
    """)