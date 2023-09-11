import speech_recognition as sr


credenciais_path = r'C:\Estudos\Assistente Virtual\bella\credenciais.json'

with open(credenciais_path, 'r', encoding='utf-8') as credenciais_google:
    credenciais_google = credenciais_google.read()


def monitora_audio():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando o comando: ")
        audio = microfone.listen(source)

    try:
        print(microfone.recognize_google_cloud(
            audio, credentials_json=credenciais_google, language='pt-br'))
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Cloud Speech service; {0}".format(e))


monitora_audio()
