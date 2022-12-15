import gtts                           # um recurso text-to-speech, isto é, transforma texto em áudio
from playsound import playsound       # reproduz audio
import speech_recognition as sr       # reconhecedor de voz

#print(sr.Microphone().list_microphone_names())       # aqui é pra você escolher entre os microfones disponíveis, caso tenha mais de um e opte por mudar
rec = sr.Recognizer()                  # variável 'rec' recebe o reconhecedor de voz para ser identificada por ela
with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)   # comando para reduzir ruído
    print('comando de voz iniciado')    # Diga uma frase assim que vir essa mensagem na tela
    audio = rec.listen(mic)             # variável 'audio' recebe a informação captada pelo microfone
    texto = rec.recognize_google(audio, language='pt-BR')  #aqui entra o gtts. Sua fala será tranformada em texto
    print(texto)                        # Sua fala será mostrada na tela
    frase = gtts.gTTS(texto, lang='pt-br')      # sua fala será gravada e interpretada para o idioma escolhido
    frase.save('frase.mp3')                     # aqui sua fala será salva em um arquivo de áudio
    playsound('frase.mp3')                      # reproduz sua fala
