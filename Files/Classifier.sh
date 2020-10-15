#!/bin/bash
#A simple bash script to setup, train, and extract the results of 
#a Text Classifier using AWS Comprehend

#Create the custom document classifier and point the output to s3
aws comprehend create-document-classifier --document-classifier-name \"financial-news-classifier\" --data-access-role-arn arn:aws:iam::433118033358:role/ComprehendBucketAccessRole --input-data-config S3Uri=s3://433118033358-comprehend/financial_news_train.csv --output-data-config S3Uri=s3://433118033358-comprehend/TrainingOutput/ --language-code en

#Confirm that the classifier has been created
aws comprehend describe-document-classifier --document-classifier-arn arn:aws:comprehend:us-east-2:433118033358:document-classifier/financial-news-classifier

#Create an inference job to test classifier
aws comprehend start-document-classification-job --document-classifier-arn arn:aws:comprehend:us-east-2:433118033358:document-classifier/financial-news-classifier --input-data-config S3Uri=s3://433118033358-comprehend/financial_news_test.csv,InputFormat=ONE_DOC_PER_LINE --output-data-config S3Uri=s3://433118033358-comprehend/InferenceOutput/ --data-access-role-arn arn:aws:iam::433118033358:role/ComprehendBucketAccessRole

#Confirm that inference job was succesfully created
aws comprehend describe-document-classification-job --job-id df6b17808f6f32cc6ceeb846fb4261ae

#Extract results from s3 bucket to local directory
aws s3 cp s3://433118033358-comprehend/InferenceOutput/433118033358-CLN-df6b17808f6f32cc6ceeb846fb4261ae/output/output.tar.gz
