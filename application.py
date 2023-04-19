import weaviate
import os
import base64
import streamlit as st

client = weaviate.Client("http://localhost:8080")

## Create Schema
schema = {
    "classes": [{
    "class" : "Images",
    "moduleConfig": {
               "img2vec-neural": {
                   "imageFields": [
                       "image"
                   ]
               }
           },
    "vectorIndexType" : "hnsw",
    "vectorizer" : "img2vec-neural",
    "properties": [
        {
            "name": "image",  
            "dataType": [
                "blob"
            ],
            "description": "image",
        },
        {
        "name": "type",  
        "dataType": ["string"],
        "description": "name of dog breed",
        }
        ]
    }]
}

def deleteSchema(): 
    client.schema.delete_class("Images")

def addSchema():
    client.schema.create(schema)

## Add Data to Weaviate
def addDataToWeaviate():
    folder_path = os.getcwd() + '/images'
    for filename in os.listdir(folder_path):
       if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
          with open(os.path.join(folder_path, filename), 'rb') as image_file:
            image_data = image_file.read()
            base64_data = base64.b64encode(image_data).decode()
            data_properties = {
            "image": base64_data,
            "type": "Mamal"
             }
            r = client.data_object.create(
                data_properties,
                "Images",
               )
            print(r)

## Search for a image on Weaviate           
def search_image(image):
    sourceImage = { "image": image}
    image = client.query.get("Images",[ "type", "image" ]).with_near_image(sourceImage, False).with_limit(1).do()
    if image:
        return image["data"]["Get"]["Images"]
    else:
        return None

## Web interface
st.title("Image search engine ⚙️")
st.write("To search for a image start by clicking 'Add schema' then 'Add data'")
st.write("This will add all images in the image folder into Weaviate. Then upload a image and similar images will appear.")
buttonCol1, buttonCol2 = st.columns(2)
with buttonCol1:
    st.button("Add schema", on_click=addSchema)
with buttonCol2:
    st.button("Add data", on_click=addDataToWeaviate)

uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

col1, col2 = st.columns(2)
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    base64_data = base64.b64encode(bytes_data).decode()

    with col1:
        st.image("data:image/jpeg;base64," + base64_data, caption="Uploaded Image", use_column_width=True)
    
    result = search_image(base64_data)
  
    if result is not None:
        for data in result:
             with col2:
                st.image("data:image/jpeg;base64," + data["image"], caption="Result Image", use_column_width=True)
