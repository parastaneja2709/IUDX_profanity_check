# run this command in terminal: $ pip install cuss_inspect
# github link: https://github.com/tushar50896/cuss_inspect

from cuss_inspect import predict, predict_prob
from update_database import update

def profanity_check(index_name,id,comment):
    modeloutput = predict(comment)
    if modeloutput==1:
        status='Denied'
    else:
        status = 'Aprooved'
    print("verification result:",status)
    update(index_name,id,status)    