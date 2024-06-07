import listenin  # слушает и переводит голос в текстовые значения
import answer  # голосовой ответ
import hello  # отвечает за приветствие

while True:
    voice_input = listenin.record_and_recognize_audio()
    voice_input = voice_input.split(" ")
    check_list = ['ужас', 'страшно', 'пиздец', 'ужасно', 'п*****']
    check_result = sum([voice_input.count(i) for i in check_list])

    if voice_input.count('привет') > 0:
        hello.hello(voice_input)
    elif check_result > 0:
        answer.play_voice_assistant_speech('Простите? Что случилось?')
    elif voice_input.count('хватит') > 0:
        break
    else:
        print(' '.join(voice_input))
