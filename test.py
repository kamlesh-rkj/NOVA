import nova_engine as ne
result=ne.wikipedia.summary("python",kwargs=0)
print(result)
print(type(result))
ne.text_to_speech(result)