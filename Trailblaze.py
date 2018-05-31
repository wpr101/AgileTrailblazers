from flask import Flask, request, abort
from gevent.pywsgi import WSGIServer
import os, json
from difflib import SequenceMatcher

app = Flask(__name__)

@app.route('/lcs', methods=['POST'])
def LCS():

    data = json.loads(request.data.decode("utf-8"))
    strings = []
    sub_sequence = ""
    

    try:
        print(data["setOfStrings"])
    except:
        abort(400, 'Post body is missing or in incorrect format')

    counter = 0
    for item in data["setOfStrings"]:
        strings.append(item["value"])
        counter += 1

    if counter == 0:
        abort(400, 'setOfStrings was empty')

    if counter == 1:
        sub_sequence = strings[0]
        return_json = '{"lcs" : [{"value": "' + sub_sequence + '"}]}'
        return(return_json)

    else:
    first_string = strings[0]
    second_string = strings[1]
    match = SequenceMatcher(None, first_string, second_string).find_longest_match(0, len(first_string), 0, len(second_string))
    sub_sequence = first_string[match.a: match.a + match.size]
    for i in range(2, len(strings)):
        next_string = strings[i]
        match = SequenceMatcher(None, sub_sequence, next_string).find_longest_match(0, len(sub_sequence), 0, len(next_string))
        sub_sequence = sub_sequence[match.a: match.a + match.size]

    return_json = '{"lcs" : [{"value": "' + sub_sequence + '"}]}'
    return (return_json)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    WSGIServer(('', port), app).serve_forever()
