import os
from flask import request
from flask import  render_template
from flask import Flask
from api.api_request import authorization, create_document, doc_list, get_doc, insert_block, token
from segmentator.processing import process as segm_proc
from classifier.processing import process as class_proc
from convert import bilou

from segmentator import crf
from classifier import max_ent

app = Flask(__name__)


def markup_content(text):
    result1 = segm_proc(text)
    result2 = class_proc(result1)
    res_text = ''
    print(result2)
    for sent in result2:
        for token in sent:
            if token['cls'] != '_':
                if token['tag'] == bilou.find('B'):
                    res_text += '<span class=' + token['cls'] + '>' + token['content'] + ' '
                elif token['tag'] == bilou.find('L'):
                    res_text += token['content'] + '</span> '
                elif token['tag'] == bilou.find('U'):
                    res_text += '<span class=' + token['cls'] + '>' + token['content'] + '</span> '
            else:
                res_text += token['content'] + ' '
    return res_text




@app.route('/', methods=['GET', 'POST'])
def list_docs():
    if token == '':
        return 'Not authorization user'
    if request.method == 'POST':
        result = request.form
        create_document(result['name'])
    docs = doc_list()
    return render_template('doc_list.html', docs=docs)


@app.route('/doc/<int:doc_id>', methods=['GET', 'POST'])
def document(doc_id):
    doc = get_doc(doc_id)
    if request.method == 'POST':
        result = request.form
        # TODO: mark up named entities
        if 'blocks' in doc:
            print(doc['blocks'])
        else:
            doc['blocks'] = []
        insert_block(doc_id, result['name'], markup_content(result['content']), len(doc['blocks']) + 1)
        doc = get_doc(doc_id)
    return render_template('document.html', doc=doc)


if __name__ == '__main__':
    # app.debug = True
    os.chdir('testset')
    files = os.listdir()
    crf.train_model(files)
    max_ent.train_model(files)
    authorization()
    app.run()

