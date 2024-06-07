import answer


def hello(voice_input):
    try:
        ignoring_list = ['меня', 'зовут']
        for i in ignoring_list:
            voice_input.remove(i)
        answer.play_voice_assistant_speech(f'Здравствуйте {voice_input[1]}, меня зовут Jarvis')
    except ValueError:
        print('что то не так с вводом данных')