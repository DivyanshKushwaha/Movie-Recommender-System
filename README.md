
# Movie Recommender System

This project builds a **Movie Recommender System** using **Natural Language Processing (NLP)** techniques like **CountVectorizer** and **PorterStemmer**. The application is developed using **Streamlit** and deployed on **Dockerhub** for public access.


![image](https://github.com/user-attachments/assets/92327917-f6d1-4efd-96cf-c8eb6bab433e)




## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Data Preprocessing](#data-preprocessing)
- [Movie Recommendation Approach](#movie-recommendation-approach)
- [Deployment on Amazon EC2](#deployment-on-amazon-ec2)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **Movie Recommender System** is designed to provide personalized movie recommendations based on content similarity. It utilizes **NLP** techniques to process movie descriptions and provide recommendations based on cosine similarity. The user interface is built using **Streamlit**, and the app is hosted on an Amazon EC2 instance.

## Technologies Used

- **Python** (v3.12)
- **NLP**: 
  - **CountVectorizer**: Transforms text data into a matrix of token counts.
  - **PorterStemmer**: Reduces words to their root forms for better text matching.
- **Streamlit**: A Python library to build web apps for machine learning models.
- **Amazon EC2**: Cloud platform for hosting and deploying the app.
- **Pandas**: For data manipulation.
- **Scikit-learn**: For machine learning and data preprocessing.

## Installation

### Prerequisites

- **Python 3.12** or later
- **Amazon EC2** instance with appropriate permissions and security groups

### Clone the Repository

```bash
git clone https://github.com/username/movie-recommender-system.git
cd movie-recommender-system
```

### Setting up the Environment

1. Create a Python virtual environment:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App Locally

To run the app on your local machine:

```bash
streamlit run app.py
```

### Run app with Docker 

1. **Install docker desktop**:
   - Create account on dockerhub
   - Login in dockerhub in powershell.
   ```bash 
   docker login -u <username>
   (Enter password)
   ```


2. **Pull Image**:
   ```bash
   docker pull jatin723/movie-recommendation:v3
   ```

3. **Run the Image in container**:
   ```bash
   docker run -d --name <container-name> -p 5000:5000 jatin723/movie-recommendation:v3
   ```

4. **Access the app in browser on**:
   ```bash
   localhost:5000
   ```


## Project Structure

```
movie-recommender-system  
      │__ data  
      |     │__ tmdb_5000_credits.csv      # Dataset containing movie credits information.  
      |     │__ tmdb_5000_movies.csv       # Dataset containing movie details.  
      │__ static  
      |     │__ styles.css                 # CSS file for styling the web application.  
      ├── templates  
      |     │__ index.html                 # HTML template for the application's main page.  
      │__ recommender                      # Python virtual environment files
      │__ requirements.txt                 # Dependencies required for the project.  
      │__ README.md                        # Project documentation and overview.  
      │__ Dockerfile                       # Instructions to containerize the application.  
      │__ app.py                           # Main Python file to run the web application.  
      │__ model.ipynb                      # Jupyter Notebook for model development.  
      │__ movies.pkl                       # Pickle file for processed movie data.  
      │__ movie_dict.pkl                   # Pickle file containing the movie dictionary.  
      │__ similarity.pkl                   # Pickle file storing similarity metrics.  
      

```

## Data Preprocessing

- **CountVectorizer**: Converts the text descriptions of movies into a matrix of token counts.
- **PorterStemmer**: Stems words to their base forms to ensure that words like "running" and "run" are treated the same.
- **Cosine Similarity**: Measures the similarity between movie descriptions to provide recommendations.

## Movie Recommendation Approach

1. **Data Loading**: Load the movie dataset from a CSV file.
2. **Text Preprocessing**: Clean and preprocess movie descriptions using **CountVectorizer** and **PorterStemmer**.
3. **Similarity Calculation**: Use cosine similarity to calculate how close one movie's description is to another.
4. **Recommendation**: Based on the cosine similarity scores, recommend the top N similar movies to the user.

## Building Image and pushing it to Dockerhub

This project is pushed on dockerhub as an image for public access. Anyone can download the image by given instructions above and run it on their local machine.

## Usage

1. **Enter a Movie**: The user inputs a movie name.
2. **Get Recommendations**: The system suggests similar movies based on content similarity.
3. **Explore Movies**: The app provides a list of recommendations with details about each movie.

## Contributing

Contributions are welcome! Feel free to submit a pull request or report issues.

## License

This project is licensed under the MIT License.
