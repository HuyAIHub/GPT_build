# !/usr/bin/python
# -*- coding: utf-8 -*-
#-*-coding:gb2312-*-

# API_KEY='dsfdsfsdffsd'
API_KEY = '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'
ENGINE='text-davinci-003'
TEMPERATURE=0.5
MAX_TOKEN=512
TOP_P=1.0
PRESENCE_PENALTY=2.0
import openai

def chatgpt_process(data):
    openai.api_key = API_KEY
    # list engines
    # engines = openai.Engine.list()
    # print the first engine's id
    # print(engines.data[0].id)
    # create a completion
    completion = openai.Completion.create(
      engine=ENGINE,
      prompt=data,
      temperature=TEMPERATURE,
      max_tokens=MAX_TOKEN,
      top_p=TOP_P,
      # frequency_penalty=abs(0.1),
      presence_penalty=PRESENCE_PENALTY
    )
    # print the completion
    return completion['choices'][0]['text'].strip()



def text_process(data):
    answer_text=''
    if data is None or data =='':
        return 'Mời nhập nội dung'
    else:
        answer_text='ChatGPT: '+chatgpt_process(data)
        return answer_text
if __name__ == '__main__':
    print(text_process('Tôi cần đoạn code automations của home assistant nếu camera phát hiện ra tôi vào lúc 7 giờ đến 9 giờ sáng thì chào tôi và automotions này chỉ chạy 1 lần trong ngày'))
    
