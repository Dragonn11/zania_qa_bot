# zania_qa_bot
Question Answering bot
# Question-Answering API with Langchain and OpenAI

This repository contains a backend API for a Question-Answering (QA) bot designed to answer questions based on the content of a document. The bot leverages the capabilities of large language models, utilizing the Langchain framework and OpenAI's GPT-3.5-turbo model.

## Problem Statement

The goal is to create an API that can receive questions and a reference document as inputs and provide accurate answers to the questions using the context provided by the document.

## Branches

- `main`: Contains the OpenAI implementation of this bot.
- `langchain`: Contains the Langchain implementation of this bot.

## Features

- Supports two types of input files: JSON and PDF.
- Answers questions based on the content of the provided document.
- Outputs answers in a structured JSON format.

## Input Requirements

The API requires two input files:

1. A JSON file containing a list of questions.
2. A PDF or JSON file containing the document over which the questions will be answered.

