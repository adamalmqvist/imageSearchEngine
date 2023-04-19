# Image Search Engine with Weaviate

This is a Python script that creates an image search engine using [Weaviate](https://www.semi.technology/documentation/weaviate/current/), a graph-based search engine.

The script allows users to add images to the search engine and search for similar images by uploading a new image. The images are stored in Weaviate, and their similarity is computed using a pre-trained neural network.

## Prerequisites

To run this script, you will need to have the following installed:

- Python 3.7+
- Weaviate
- Streamlit

## Installation

1. Clone this repository:

```
git clone https://github.com/username/image-search-engine.git

```

2. Install the required Python packages:

```
pip install weaviate streamlit

```

## Usage

1. Click the "Add schema" button to create the schema in Weaviate.

2. Click the "Add data" button to add images to the search engine. The images should be stored in a folder called "images" in the same directory as the script.

3. Upload an image to search for similar images. The script will display the uploaded image and the most similar image in the search engine.
