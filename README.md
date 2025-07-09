# IMDb-Movie-chat-bot

This project aims to build a Semantic Movie &amp; People Search Engine that
allows users to search for movies, actors, or directors using natural language
queries.The system integrates PostgreSQL with the pgvector extension for vector 
storage and similarity search, utilizes Hugging Face's Sentence Transformer for 
generating embeddings, and employs the free version of OpenAI for language model 
responses. The entire application is deployed using Streamlit to provide an interactive
user interface. 

# Motivation
I chose this project because it offers an opportunity to combine data
engineering (scraping, cleaning, loading), machine learning (embeddings,
semantic search), and application development (Streamlit) into one cohesive
solution. Semantic search and retrieval-augmented generation (RAG)
systems are becoming critical in modern AI applications. By building an end-
to-end semantic search and RAG pipeline, this project will enhance my skills
specifically in RAG workflows, which is an emerging and valuable area in
real-world AI development. 

# Data Question
How can we build a system that allows users to find movies or
actors/directors semantically based on free-text queries, and generate
natural language responses that make recommendations based on
structured database information?

# Minimum Viable Product
1. Load and clean IMDb datasets: title.basics.tsv.gz, name.basics.tsv.gz,
title.ratings.tsv.gz, and title.principals.tsv.gz.
2. Store structured movie and people data in PostgreSQL using pgvector
for embeddings.
3. Generate semantic embeddings using Hugging Face's Sentence Transformer.
4. Allow users to semantically search for movies or actors via a Streamlit
frontend.
5. Pass results context to free version of OpenAI LLM to generate clean, human-readable
answers.

# Data Sources
## IMDb Public Datasets:

https://datasets.imdbws.com/

 **Files to use:**
1. title.basics.tsv.gz (Movie metadata)
2. name.basics.tsv.gz (People metadata)
3. title.ratings.tsv.gz (Movie ratings)
4. title.principals.tsv.gz (People linked to movies)
5. title.crew.tsv.gz (moview crew members)

**Technology Sources**
1. Free OPEN AI via openrouter.ai (for free LLM models)
2. pgvector (for vector embeddings in PostgreSQL)
3. Hugging Face's Sentence Transformer
