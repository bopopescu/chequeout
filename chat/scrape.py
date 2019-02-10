import json

def detect_items(input_text):
    import six
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types

    text = input_text

    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    entities = client.analyze_entities(document).entities

    for entity in entities:
        entity_type = enums.Entity.Type(entity.type)
        print('=' * 20)
        print(u'{:<16}: {}'.format('name', entity.name))
        print(u'{:<16}: {}'.format('type', entity_type.name))
        print(u'{:<16}: {}'.format('salience', entity.salience))
        print(u'{:<16}: {}'.format('wikipedia_url',
              entity.metadata.get('wikipedia_url', '-')))
        print(u'{:<16}: {}'.format('mid', entity.metadata.get('mid', '-')))
    return entities
def walmart_prices():
    api_key = ''
    base_url = 'http://api.walmartlabs.com/v1/search?apiKey=' + api_key

def return_card_string():
    with open('chat/output.json') as f:
        data = json.load(f)
        product_url = data.get('1',{}).get('product_url',0)
        title = data.get('1',{}).get('title',0)
        imgsrc = data.get('1',{}).get('image_url',0)
        price = data.get('1',{}).get('prices').get('0',0)
        if product_url:
            cardtext = """
            <div class="container justify-content-center row">
                <div class="card" style="width: 18rem;">
                    <img class="card-img-top" src=""" + "'" + imgsrc + """'alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title">""" + title + """</h5>
                        <p class="card-text"> Price: """ + price + """</p>
                        <a href=""" + "'" + product_url + """' class="btn btn-primary">Open in new tab</a>
                    </div>
                </div>
            </div>
            """
        else:
            cardtext = """
            <div class="container justify-content-center row">
                <div class="card" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title"> Could not be found </h5>
                        <p class="card-text"> Try refreshing the page, or being more specific with your items</p>
                    </div>
                </div>
            </div>
            """
        return cardtext


# if worst comes to worst, you just hardcode the crap
