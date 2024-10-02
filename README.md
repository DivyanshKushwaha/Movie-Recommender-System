
# Movie Recommender System

This project builds a **Movie Recommender System** using **Natural Language Processing (NLP)** techniques like **CountVectorizer** and **PorterStemmer**. The application is developed using **Streamlit** and deployed on an **Amazon EC2** server for real-time recommendations.


![movie](https://github.com/user-attachments/assets/e51faf13-6de5-47a6-bb1a-a5ca56cb2e05)

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

### Deploying on Amazon EC2

1. **Launch an EC2 Instance**:
   - Choose Ubuntu as the operating system.
   - Configure security groups to allow HTTP and HTTPS traffic.

2. **Connect Instance**:
   ```bash
   ssh -i "your-key.pem" ubuntu@your-ec2-instance-public-ip
   ```

3. **Install Python and Streamlit on EC2**:
   ```bash
   sudo apt update
   sudo apt install python3-pip
   pip3 install streamlit
   ```

4. **Transfer the Project to EC2**:
   - Use SCP to copy the project folder to the EC2 instance:
   ```bash
   scp -i "your-key.pem" -r ./movie-recommender-system ubuntu@your-ec2-instance-public-ip:~/.
   ```

5. **Run the Streamlit App on EC2**:
   ```bash
   cd movie-recommender-system
   streamlit run app.py --server.port 80
   ```

6. **Access the App**:
   Open your browser and go to `http://your-ec2-instance-public-ip` to access the Movie Recommender System.

## Project Structure

```
movie-recommender-system/
│
├── tmdb_5000_credits.csv       # Dataset containing credits and description of movies
|── tmdb_5000_movies.csv        # Dataset containing movies 
│                
├── app.py                      # Streamlit app entry point
├── recommender                 # Environment conatining packages and modules 
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation          
├── movies.pkl                  # Pickle file containing movies 
├── movie_dict.pkl              # Movies dictionary pickle file
├── similarity.pkl              # Pickle file containing similar properties among movies 
└── README.md                   # Project documentation
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

## Deployment on Amazon EC2

This project is deployed on an **Amazon EC2** instance. The app is accessible over the web and provides movie recommendations in real-time. Ensure that your EC2 instance has ports 80 and 443 open in the security groups for public access.

## Usage

1. **Enter a Movie**: The user inputs a movie name.
2. **Get Recommendations**: The system suggests similar movies based on content similarity.
3. **Explore Movies**: The app provides a list of recommendations with details about each movie.

## Contributing

Contributions are welcome! Feel free to submit a pull request or report issues.

## License

This project is licensed under the MIT License.
