# github link: https://github.com/tushar50896/cuss_inspect
# run this command in terminal: $ pip install cuss_inspect
from cuss_inspect import predict, predict_prob

# for simple string
text_0 = "this is simple review. you have done a good job"
print(predict(text_0))
# [0]
print(predict_prob(text_0))
# [0.05]

text_1 = "son of a bitch"
print(predict(text_1))
# [1]
print(predict_prob(text_1))
# [1.]

# for list of inputs
test = ['who are you?' , 'what do you want?' , 'son of a dog' , 'how the hell can you say that' , 'fuck it']
print(predict(test))
# [0 0 1 1 1]
print(predict_prob(test))
# [0.12 0.22 0.55 0.96 1.]