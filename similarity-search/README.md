
# Clothing Similarity Model

The goal of this project is to create a machine learning model capable of receiving text describing a clothing item and returning a ranked list of links to similar items from different websites. This solution is implemented as a function deployed on Google Cloud, which accepts a text string and returns JSON responses with ranked suggestions. To further improve the results we used a vector database which would in return increase the accuracy of the model.

## Project Overview

The project follows the following steps to achieve the desired functionality:

1. **Data Collection and Preprocessing**: Web scraping tools in this case BeautifulSoup4 and Scrapy for some websites are used to gather a dataset of clothing item descriptions. The text data is then preprocessed by applying cleaning techniques.

2. **Similarity Measurement**: A method is developed to extract useful features from the text descriptions and is then converted to its respective embeddings with MiniLM. These features are used to compute the similarity between the input text and the texts in the database.

3. **Ranked Results**: A function is designed to accept a text string, extract its features, compute similarities with the items in the database, rank them based on similarity, and return the URLs of the top-N most similar items.

4. **Deployment**: The function is deployed on Google Cloud to make it accessible as an API endpoint.

## Model and Similarity Search

The model used for embedding the clothing item descriptions is MiniLM. This model has been found to be highly effective in generating embeddings for textual data. For similarity search, Faiss is used as it provides efficient storage and retrieval of similar items based on embeddings.

## Data Sources

The project scrapes data from various websites such as Flipkart and Myntraa to collect a diverse range of clothing item descriptions. However, it should be noted that these websites are challenging for scraping due to their complex structures and anti-scraping measures.

## License

This project is licensed under the [MIT License](LICENSE).

