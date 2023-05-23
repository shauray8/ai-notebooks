
# Clothing Similarity Model

The goal of this project is to create a machine learning model capable of receiving text describing a clothing item and returning a ranked list of links to similar items from different websites. This solution is implemented as a function deployed on Google Cloud, which accepts a text string and returns JSON responses with ranked suggestions.

## Project Overview

The project follows the following steps to achieve the desired functionality:

1. **Data Collection and Preprocessing**: Web scraping tools are used to gather a dataset of clothing item descriptions. The text data is then preprocessed by applying cleaning techniques.

2. **Similarity Measurement**: A method is developed to extract useful features from the text descriptions. These features are used to compute the similarity between the input text and the texts in the database.

3. **Ranked Results**: A function is designed to accept a text string, extract its features, compute similarities with the items in the database, rank them based on similarity, and return the URLs of the top-N most similar items.

4. **Deployment**: The function is deployed on Google Cloud Functions or Google Cloud Run to make it accessible as an API endpoint.

## Project Rubric

The project is evaluated based on the following criteria:

1. **Completeness**: Did the engineer implement all components of the project and carefully follow the instructions?

2. **Performance**: How well does the project achieve its intended goal? Is the implementation efficient?

3. **Documentation**: The code is well-documented with meaningful comments. Additionally, this README file provides an overview of the project and instructions for deployment.

## Model and Similarity Search

The model used for embedding the clothing item descriptions is MiniLM. This model has been found to be highly effective in generating embeddings for textual data. For similarity search, Faiss is used as it provides efficient storage and retrieval of similar items based on embeddings.

## Data Sources

The project scrapes data from various websites such as Flipkart and Myntraa to collect a diverse range of clothing item descriptions. However, it should be noted that these websites are challenging for scraping due to their complex structures and anti-scraping measures.

## Deployment

To deploy the function on Google Cloud, follow these steps:

1. Set up a Google Cloud project and enable necessary APIs.
2. Prepare the function code and dependencies.
3. Create a Cloud Function or Cloud Run service.
4. Configure the endpoint URL and other settings.
5. Deploy the function to the cloud platform.

For detailed instructions on deploying the function, please refer to the [Deployment Guide](deployment.md).

## License

This project is licensed under the [MIT License](LICENSE).

