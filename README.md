# ContentSummarizer
An AI based application which summarizes books, creates content like instagram posts for books. The aim is to develop a complete product where people can subscribe to some topics, books, and the application should post these content that is created by system. The post content is text content initally, later we aim for visual posts, videos.

## Plan

Summarization:

User uploads pdf, pdf is split into chunks and is forwarded to LLM.
LLM should generate summaries of concepts or parts.


# Posts Backend

start mongo db -

dev environment on mac ==============================
brew services start mongodb/brew/mongodb-community@8.0
or
mongod --config /opt/homebrew/etc/mongod.conf --fork
=====================================================
