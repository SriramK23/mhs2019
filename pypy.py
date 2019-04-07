from picamera import PiCamera
from time import sleep
from google.cloud import vision
from subprocess import call

cmd_beg = 'espeak -ven-us '
cmd_end = ' 2>/dev/null'

camera = PiCamera()




def takephoto():
    camera.start_preview()
    sleep(5)
    camera.capture('picy.jpg')
    camera.stop_preview()


def detect_document():
    takephoto()
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open('picy.jpg', 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
         for block in page.blocks:
             print('\nBlock confidence: {}\n'.format(block.confidence))

         for paragraph in block.paragraphs:
             print('Paragraph confidence: {}'.format(paragraph.confidence))

             for word in paragraph.words:
                 word_text = ''.join([
                 symbol.text for symbol in word.symbols
                     ])
                 call([cmd_beg+word_text+cmd_end], shell=True)
                 sleep(0.5)

                 print('Word text: {} (confidence: {})'.format(
                            word_text, word.confidence))

                 for symbol in word.symbols:
                        print('\tSymbol: {} (confidence: {})'.format(
                            symbol.text, symbol.confidence))
        
                               


while True:
        
     detect_document('picy.jpg')
     sleep(10)
