import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import mimetypes


# Função para determinar o tipo MIME da imagem
def guess_mime_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        raise TypeError('Could not guess image MIME subtype')
    return mime_type

# Configurações do e-mail
sender_email = "email do remetente"
sender_password = "senha do google para aplicações"
#destinatario do email
recipient_email = "email do destinatario"
subject = "Titulo do email"

# Corpo do e-mail em HTML
html = """
Email em html
"""
# Criar uma nova mensagem para cada destinatário
message = MIMEMultipart("related")
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject

# Anexar o corpo HTML ao e-mail
message.attach(MIMEText(html, "html"))

# Caminho para a imagem
imagens = [(r'caminho_da_imabem','id_da_imagem'),
           (r'caminho_da_imabem','id_da_imagem'),

           ]

for image_path, id_imagem in imagens:
    # Determinar o tipo MIME da imagem
    mime_type = guess_mime_type(image_path)

    # Abrir a imagem e anexá-la ao email
    with open(image_path, 'rb') as img:
        mime_image = MIMEImage(img.read(), _subtype=mime_type.split('/')[1])
        mime_image.add_header('Content-ID', f'<{id_imagem}>')
        message.attach(mime_image)

# Enviar o e-mail
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")

