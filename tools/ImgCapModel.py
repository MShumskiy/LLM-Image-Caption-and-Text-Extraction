
# Ensure that accelerate is imported to enable its features
from accelerate import Accelerator
# Initialize the accelerator
accelerator = Accelerator()

def describe(request,image_path,tokenizer,model):
    query = tokenizer.from_list_format([
        {'image': image_path},
        {'text': '{}:'.format(request)},
    ])
    inputs = tokenizer(query, return_tensors='pt')
    inputs = inputs.to(model.device)
    pred = model.generate(**inputs)
    response = tokenizer.decode(pred.cpu()[0], skip_special_tokens=True)
    #generated_text = response.split(': ')[2]
    return response

def caption_image(image_path,tokenizer,model):
    request_4 = 'Describe the image'
    request_7 = 'Extract the promotions from the image'
    output = []
    i=0
    for i in range(1):
        output.append(describe(request_4,image_path,tokenizer,model))
        i+=1
    i=0
    for i in range(1):
        output.append(describe(request_7,image_path,tokenizer,model))
        i+=1
    return output