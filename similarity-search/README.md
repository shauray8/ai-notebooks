
# Clothing Similarity Model

The goal of this project is to create a machine learning model capable of receiving text describing a clothing item and returning a ranked list of links to similar items from different websites. This solution is implemented as a function deployed on Google Cloud, which accepts a text string and returns JSON responses with ranked suggestions. To further improve the results we used a vector database which would in return increase the accuracy of the model.

## Project Overview

The project follows the following steps to achieve the desired functionality:

1. **Data Collection and Preprocessing**: Web scraping tools in this case BeautifulSoup4 and Scrapy for some websites are used to gather a dataset of clothing item descriptions. The text data is then preprocessed by applying cleaning techniques.

2. **Similarity Measurement**: A method is developed to extract useful features from the text descriptions and is then converted to its respective embeddings with MiniLM. These features are used to compute the similarity between the input text and the texts in the database.

3. **Ranked Results**: A function is designed to accept a text string, extract its features, compute similarities with the items in the database, rank them based on similarity, and return the URLs of the top-N most similar items.

4. **Deployment**: The function is deployed on Google Cloud to make it accessible as an API endpoint.

## Data Sources

The project scrapes data from various websites such as Flipkart and Myntraa to collect a diverse range of clothing item descriptions. However, it should be noted that these websites are challenging for scraping due to their complex structures and anti-scraping measures.

## Set up Instructions 

1. Set Up Google Cloud Project
* Create a new project or select an existing project on Google Cloud Console.<br>
* Make sure you have the necessary permissions to create and deploy Cloud Functions.<br>
2. Clone the Repository <br>
``` git clone <repo> --depth 1 ```<br>
3. Set Up Environment
* Install the necessary dependencies by running the following command:<br>
```pip install -r requirements.txt```<br>
4. run the script <br>
```python main.py --mode test --prompt "enter your prompt"```



## Model and Similarity Search

The model used for embedding the clothing item descriptions is MiniLM. This model has been found to be highly effective in generating embeddings for textual data. For similarity search, Faiss is 
used as it provides efficient storage and retrieval of similar items based on embeddings.

## FAISS (Facebook AI Similarity Search)
FAISS is an open-source library developed by Facebook AI Research that enables efficient similarity search and clustering of large datasets. It is widely used in various applications, including recommendation systems, image and text search, and content similarity matching.
<br><br>
### Key Features of FAISS:
<br>
Efficient Similarity Search: FAISS provides highly optimized algorithms and data structures for performing fast and scalable similarity search on large datasets. It offers both exact and approximate search methods, allowing trade-offs between search accuracy and computational efficiency.
<br><br>
Support for Vector Embeddings: FAISS is designed to work with vector embeddings, where each data point is represented as a high-dimensional vector. It offers indexing techniques, such as the Inverted File or Product Quantization, to efficiently store and retrieve embeddings during similarity search.
<br><br>
Multi-GPU and Distributed Support: FAISS supports parallel processing on multiple GPUs, allowing for faster indexing and search operations. It also provides mechanisms for distributed computing, enabling scaling to even larger datasets.
<br><br>
Integration with Deep Learning Libraries: FAISS integrates well with popular deep learning frameworks like PyTorch, allowing seamless integration of similarity search capabilities into existing machine learning pipelines.
<br><br>
Wide Range of Applications: FAISS has been successfully applied in various domains, including text search, image similarity, recommendation systems, and anomaly detection. Its versatility and scalability make it suitable for handling diverse similarity search tasks.
<br><br>
For more information and detailed documentation on FAISS, please refer to the official FAISS repository.
<br><br>

#### Integration with Your Project
In this project, FAISS is utilized to store and retrieve embeddings of clothing item descriptions. By leveraging FAISS, the similarity search functionality becomes highly efficient, enabling the ranking of similar items based on their embeddings.

The FAISS library can be easily integrated into your project's codebase by following the provided documentation and examples. It is recommended to explore the FAISS documentation to understand the different indexing techniques and search algorithms available, and choose the most suitable ones based on the requirements of your clothing similarity model.

## MiniLM
MiniLM is a compact and efficient language model developed by Microsoft Research. It is based on the Transformer architecture and designed to provide strong performance while being lightweight and fast. MiniLM achieves a good balance between model size and language generation capabilities, making it suitable for various natural language processing tasks.
<br><br>
### Key Features of MiniLM:
<br>
Compact Model Size: MiniLM has a smaller model size compared to larger language models like GPT-3, while still delivering impressive performance on various language tasks. This makes it easier to deploy and use in resource-constrained environments.
<br><br>
Efficient Inference: MiniLM is designed to be highly efficient during inference, allowing for faster generation of language outputs. Its architecture and optimizations make it suitable for real-time or low-latency applications.
<br><br>
Language Generation Capabilities: MiniLM is trained on large-scale text corpora, enabling it to generate coherent and contextually relevant text. It can be fine-tuned for specific tasks such as text classification, summarization, or question answering.
<br><br>
Compatibility with Transformer Models: MiniLM follows the Transformer architecture, making it compatible with other Transformer-based models. This allows for easy integration and transfer learning with existing models and frameworks.

## License

This project is licensed under the [MIT License](LICENSE).
