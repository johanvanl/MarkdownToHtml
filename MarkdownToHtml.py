import os
import logging
import mistune

def saveFile(fileName, content):
    logging.debug('Saving content to {}'.format(fileName))
    with open(fileName, 'w', encoding='utf8') as out:
        out.write(content)
    logging.debug('Done saving content to {}'.format(fileName))

def readFile(fileName):
    '''
    Read the file contents from fileName and returning a string
    '''
    logging.debug('Reading {}'.format(fileName))
    content = ''
    with open(fileName, encoding='utf-8') as f:
        content = f.read()
    return content

# http://mistune.readthedocs.io/en/latest/
def markdownToHtml(text):
    renderer = mistune.Renderer(hard_wrap=True)
    markdown = mistune.Markdown(renderer=renderer)
    return markdown(text)

def markdownFileToHtml(fn):
    out_fn = fn.split('.')[0] + '.html'
    md = readFile(fn)
    saveFile(out_fn, markdownToHtml(md))

def findMarkdownFiles():
    files = []
    for file in os.listdir():
        if os.path.isfile(file) and file.endswith('.md'):
            files.append(str(file))
    return files

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    
    files = findMarkdownFiles()
    for file in files:
        logging.debug('Processing: ' + file)
        markdownFileToHtml(file)
