import flask
from PIL import Image
# import json
# import os
# # from PIL import Image
# import base64
# import io
# from colormap import rgb2hex
# from config import *
# from functionsLabels import *
# from azureml.core import Workspace,Dataset,Datastore
# import tensorflow
# from tensorflow.keras.preprocessing.image import load_img, img_to_array
#from segmentation_models.metrics import IOUScore
#from segmentation_models.losses import JaccardLoss

# Initializing flask app
app = flask.Flask(__name__)
# app.secret_key = SECRET_KEY

# from flask import Flask, request,render_template,flash,make_response
# Adding cors to flask
#CORS(app)

# Controller-1
@app.route("/", methods=['GET'])
def hello():
    return "Hellooooo"

# def get_home():
#     # afficher le formulaire
#     return render_template('index.html',imagename='',image_origine='',image_segment = '',labels = '',result = False)


# # Controller-2
# @app.route("/", methods=['POST'])
# def get_result():
#     result = request.form
#     imageId = result['imageId'] # on récupère  imageId'
#     if len(imageId) > 0:
#         #flash(u'Your request is in process...')
#         imagename,image_origine,image_load,image_masque  = get_image_and_mask(imageId)
#         if image_origine is not None:
#             #image_segment = predict(image_origine)
#             labels = get_labels()
#             return render_template("index.html",imagename=imagename,image_origine=get_encode_image(image_load),
#                                    image_segment = get_encode_image(image_load),image_masque=get_encode_image(image_masque),labels = labels,result = True)
#         else:
#             flash(u'Image id number not find. Please enter another image id')
#             return render_template('index.html',imagename='',image_origine='',image_segment = '',image_masque='',labels = '', result = False)
            

#     else:
#         flash(u'Error in the sent data.')
#         return render_template('index.html',imagename='',image_origine='',image_segment = '',image_masque='',labels = '', result = False)
    
#     #data = flask.request.data
#     #body = json.loads(data)
#     #print(data)
#     #return 
#     # "Hello, I am {}!".format(body)
#     # traiter les données reçues
#     # afficher : "Merci de m'avoir laissé un message !"
    
# def get_image_and_mask(id):
#     sbc = SUBSCRIPTION_ID
#     name = NAME
#     group = RESOURCE_GROUP
#     datastore = DATASTORE
#     data_dir =DATADIR
#     ws = Workspace.get(name=name, subscription_id=sbc, resource_group=group)
#     data_ds = Datastore(ws,name=datastore)
#     dataset = ['train','val','test']
#     for data in dataset: 
#         src_folder = os.path.join(data_dir, data,"images")
#         print(src_folder)
#         imagename,image,image_load = find_image(id,data_ds,src_folder)
#         #print(image)
#         if image is not None:
#             mask_folder = os.path.join(data_dir, data,"masks")
#             print(mask_folder)
#             _,mask, mask_load = find_image(id,data_ds,mask_folder)
#             if mask is not None:
#                 return imagename,image,image_load,mask_load
#     return None, None, None, None
    
# def get_image(id):
#     dataset = ['train','val','test']
#     for data in dataset: 
#         src_folder = os.path.join(data_dir, data,"images")
#         image = find_image(id,data_ds,src_folder)
#         if image is not None:
#               return image

# def find_image(id,data_ds,src_folder):
#     image_size = IMAGE_SIZE
#     files = Dataset.File.from_files(path=(data_ds, src_folder))
#     rel_filepaths = files.to_path()
#     abs_filepaths = [src_folder + path for path in rel_filepaths if path.find(id)!=-1]
#     if len(abs_filepaths)>0:
#         imagename = abs_filepaths[0].replace(src_folder+"/",'')
#         file = Dataset.File.from_files(path=(data_ds, abs_filepaths[0]))
#         tmp = file.download() 
#         image_load = Image.open(tmp[0])
#         #img = Image.Image.resize((image_size,2*image_size), image_load)
#         img = img_to_array(load_img(tmp[0],target_size=(image_size,2*image_size,3)))/255
#         #img = img_to_array(img)/255
#         #image_load = cv2.imread(tmp[0])
#         return imagename,img,image_load
#     else:
#         return None, None, None
    
# def make_prediction(model,img):
#     img = np.expand_dims(img,axis=0)
#     labels = model.predict(img)
#     labels = np.argmax(labels[0],axis=2)
#     return labels

# def form_colormap(prediction,mapping):
#     h,w = prediction.shape
#     color_label = np.zeros((2*h,4*w,3),dtype=np.uint8)    
#     color_label = mapping[prediction]
#     color_label = color_label.astype(np.uint8)
#     return color_label

# def get_label_values():
#     labels = get_label_info()
#     label_values, colors_replacements = get_labels_mapping(labels)
#     return label_values
        
# def predict(img):
#     model_path = MODEL_PATH
#   #  model = tensorflow.keras.models.load_model(model_path, custom_objects = {"jaccard_loss":JaccardLoss, "IOUScore": #IOUScore})
#     model = tensorflow.keras.models.load_model(model_path, compile=False)
#     pred_label = make_prediction(model, img)
#     pred_colored = form_colormap(pred_label,np.array(get_label_values()))
#     load_predict = Image.fromarray(pred_colored, "RGB")
    
#     return load_predict

# def get_encode_image(img):
#     #Convertir l'image au format envoyable et la stocker en JSON
#     data = io.BytesIO()
#     img.save(data, "png")
#     encoded_img_data = base64.b64encode(data.getvalue())
#     img_byte = encoded_img_data.decode("utf-8")
#     return img_byte
        
# def traiter_donnees(id):
#     image, mask = get_image_and_mask(id)
#     if image is not None:
#         # Predict 
#         label = predict(image)
#         return label
 
    

# def get_json_image(img,imageName):
#     #Convertir l'image au format envoyable et la stocker en JSON
#     _, encimg = cv2.imencode(".png ", img)
#     img_str = encimg.tostring()
#     img_byte = base64.b64encode(img_str).decode("utf-8")
#     img_json = json.dumps({imageName: img_byte}).encode('utf-8')
#     return img_json
    
   
        
# def display_image(imagename):    
#     file_path = os.path.join(DATA_DIRECTORY, imagename)
#     im = Image.open(file_path)
#     # Get the in-memory info using below code line.
#     data = io.BytesIO()
#     #First save image as in-memory.
#     im.save(data, "png")
#     #Then encode the saved image file.
#     encoded_img_data = base64.b64encode(data.getvalue())
#     return encoded_img_data.decode('utf-8')
#     #render_template("index.html", img_data=encoded_img_data.decode('utf-8'))
    
#     #image = cv2.imread(file_path)
#     #mon_image = base64.b64encode(cv2.imencode('.png', image)[1]).decode()#"utf-8"
#     #with open(file_path, "rb") as f:
#      #   image_binary = f.read()
#     #image = b64encode(image_binary).decode("utf-8")
#     #image = Image.open(file_path) 
#     #reponse = make_response(mon_image)
#     #reponse.mimetype = "text/png"#image.get  # à la place de "text/html"
#     #return reponse
    
# def get_labels():
#     label_map = {'void': (0, 0, 0),
#   'flat': (128, 64, 128),
#   'construction': (70, 70, 70),
#   'object': (153, 153, 153),
#   'nature': (107, 142, 35),
#   'sky': (70, 130, 180),
#   'human': (220, 20, 60),
#   'vehicle': (0, 0, 142)}
#     result = []
#     for label, col in label_map.items():
#         print(label, col)
#         result.append((label.upper(),rgb2hex(col[0],col[1],col[2])))
#     return result
    
# Running the api
if __name__ == '__main__':
     app.run(debug=True)

        
